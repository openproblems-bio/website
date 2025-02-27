library(tidyverse)
library(kableExtra)
library(funkyheatmap)

# ----------------------------
# Load data
# ----------------------------
`%|%` <- function(x, y) {
  ifelse(is.na(x), y, x)
}

aggregate_scores <- function(scaled_score) {
  mean(pmin(1, pmax(0, scaled_score)) %|% 0)
}

load <- function(data_dir, exclude_metric_ids = c(), exclude_dataset_ids = c(), exclude_method_ids = c(), rename_method_names = c(), rename_method_ids = c()) {
  # read task info
  task_info <- jsonlite::read_json(paste0(data_dir, "/task_info.json"))

  # add missing data
  task_info$task_description <- task_info$task_description %||% NA_character_
  task_info$task_motivation <- task_info$task_motivation %||% NA_character_

  method_info <- jsonlite::read_json(paste0(data_dir, "/method_info.json"), simplifyVector = TRUE)
  metric_info <- jsonlite::read_json(paste0(data_dir, "/metric_info.json"), simplifyVector = TRUE)
  dataset_info <- jsonlite::read_json(paste0(data_dir, "/dataset_info.json"), simplifyVector = TRUE)
  results <- jsonlite::read_json(paste0(data_dir, "/results.json"), simplifyVector = TRUE) %>% tibble()
  qc <- if (file.exists(paste0(data_dir, "/quality_control.json"))) {
    jsonlite::read_json(paste0(data_dir, "/quality_control.json"), simplifyVector = TRUE)
  } else {
    NULL
  }

  # remove methods which couldn't be linked to certain datasets
  results <- results |> filter(!is.na(dataset_id))

  # filter by metric
  if (length(exclude_metric_ids) > 0) {
    results$metric_values <- results$metric_values[!names(results$metric_values) %in% exclude_metric_ids]
    metric_info <- metric_info %>% filter(!metric_id %in% exclude_metric_ids)
  }

  # filter by dataset
  if (length(exclude_dataset_ids) > 0) {
    results <- results %>% filter(!dataset_id %in% exclude_dataset_ids)
    dataset_info <- dataset_info %>% filter(!dataset_id %in% exclude_dataset_ids)
  }

  # filter by method
  if (length(exclude_method_ids) > 0) {
    results <- results %>% filter(!method_id %in% exclude_method_ids)
    method_info <- method_info %>% filter(!method_id %in% exclude_method_ids)
  }

  # rename methods
  if (length(rename_method_names) > 0) {
    method_info <- method_info %>% mutate(
      method_name = case_when(
        method_id %in% names(rename_method_names) ~ rename_method_names[method_id],
        TRUE ~ method_name
      )
    )
  }

  if (length(rename_method_ids) > 0) {
    update_method_ids <- function(method_ids) {
      case_when(
        method_ids %in% names(rename_method_ids) ~ rename_method_ids[method_ids],
        TRUE ~ method_ids
      )
    }
    results <- results %>% mutate(method_id = update_method_ids(method_id))
    method_info <- method_info %>% mutate(method_id = update_method_ids(method_id))
  }

  # transform results
  results_long <-
    inner_join(
      results %>%
        select(method_id, dataset_id, metric_values) %>%
        unnest(metric_values) %>%
        gather(metric_id, value, any_of(metric_info$metric_id)) %>%
        mutate(value = ifelse(is.na(value), NA_real_, value)),
      results %>%
        select(method_id, dataset_id, scaled_scores) %>%
        unnest(scaled_scores) %>%
        gather(metric_id, score, any_of(metric_info$metric_id)) %>%
        mutate(score = ifelse(is.na(score), NA_real_, score)),
      by = c("method_id", "dataset_id", "metric_id")
    ) %>%
    left_join(method_info %>% select(method_id, is_baseline), "method_id")

  overall_ranking <- results_long %>%
    group_by(method_id) %>%
    summarise(mean_score = aggregate_scores(score)) %>%
    arrange(desc(mean_score))

  # order by ranking
  results_long$method_id <- factor(results_long$method_id, levels = rev(overall_ranking$method_id))
  results$method_id <- factor(results$method_id, levels = rev(overall_ranking$method_id))
  method_info$method_id <- factor(method_info$method_id, levels = rev(overall_ranking$method_id))

  list(
    task_info = task_info,
    method_info = method_info,
    metric_info = metric_info,
    dataset_info = dataset_info,
    results = results,
    qc = qc,
    results_long = results_long,
    overall_ranking = overall_ranking
  )
}

exclude_dataset_ids <- c("cellxgene_census/mouse_pancreas_atlas", "cellxgene_census/hypomap")
data_bi <- load(
  data_dir = "results/batch_integration/data",
  exclude_metric_ids = c("hvg_overlap"),
  exclude_dataset_ids = exclude_dataset_ids
)
data_lp <- load(
  data_dir = "results/label_projection/data",
  exclude_dataset_ids = exclude_dataset_ids,
  exclude_method_ids = c("scimilarity"),
  rename_method_ids = c("scimilarity_knn" = "scimilarity"),
  rename_method_names = c("scimilarity_knn" = "SCimilarity")
)

# ----------------------------

label_time <- function(time) {
  case_when(
    is.na(time) ~ "N/A",
    time < 1e-5 ~ "0s",
    time < 1 ~ "<1s",
    time < 60 ~ paste0(floor(time), "s"),
    time < 3600 ~ paste0(floor(time / 60), "m"),
    time < 3600 * 24 ~ paste0(floor(time / 3600), "h"),
    time < 3600 * 24 * 7 ~ paste0(floor(time / 3600 / 24), "d"),
    TRUE ~ ">7d"
  )
}
label_memory <- function(x_mb) {
  case_when(
    x_mb < 1e3 ~ "<1G",
    x_mb < 1e6 ~ paste0(round(x_mb / 1e3), "G"),
    x_mb < 1e9 ~ paste0(round(x_mb / 1e6), "T"),
    TRUE ~ ">1P"
  )
}


get_fh_data <- function(data) {
  overall <- data$results_long %>%
    group_by(method_id) %>%
    summarise(mean_score = aggregate_scores(score), .groups = "drop") %>%
    arrange(mean_score)
  per_dataset <- data$results_long %>%
    group_by(method_id, dataset_id) %>%
    summarise(score = aggregate_scores(score), .groups = "drop") %>%
    mutate(dataset_id = paste0("dataset_", dataset_id)) %>%
    spread(dataset_id, score)
  per_metric <- data$results_long %>%
    group_by(method_id, metric_id) %>%
    summarise(score = aggregate_scores(score), .groups = "drop") %>%
    mutate(metric_id = paste0("metric_", metric_id)) %>%
    spread(metric_id, score)

  results_resources <- data$results %>%
    select(method_id, dataset_id, resources) %>%
    unnest(resources)


  resources <- results_resources %>%
    group_by(method_id) %>%
    summarise(
      error_pct_oom = mean(exit_code %|% 0 %in% c(137)),
      error_pct_timeout = mean(exit_code %|% 0 %in% c(143)),
      error_pct_na = mean(exit_code %|% 0 %in% c(99)),
      error_pct_error = mean(exit_code %|% 0 != 0) - error_pct_oom - error_pct_timeout - error_pct_na,
      error_pct_ok = 1 - error_pct_oom - error_pct_timeout - error_pct_error - error_pct_na,
      error_reason = list(c(
        "Memory limit exceeded" = error_pct_oom,
        "Time limit exceeded" = error_pct_timeout,
        "Execution error" = error_pct_error,
        "Not applicable" = error_pct_na,
        "No error" = error_pct_ok
      )),
      mean_cpu_pct = mean(cpu_pct, na.rm = TRUE),
      mean_peak_memory_b = mean(peak_memory_mb, na.rm = TRUE) * 1000,
      mean_peak_memory_log = -log10(mean_peak_memory_b),
      mean_peak_memory_str = label_memory(mean_peak_memory_b * 1000),
      mean_disk_read_b = mean(disk_read_mb, na.rm = TRUE) * 1000,
      mean_disk_read_log = -log10(mean_disk_read_b),
      mean_disk_read_str = label_memory(mean_disk_read_b * 1000),
      mean_disk_write_mb = mean(disk_write_mb, na.rm = TRUE) * 1000,
      mean_disk_write_log = -log10(mean_disk_write_mb),
      mean_disk_write_str = label_memory(mean_disk_write_mb * 1000),
      mean_duration_sec = mean(duration_sec %|% 0),
      mean_duration_log = -log10(mean_duration_sec),
      mean_duration_str = label_time(mean_duration_sec),
      .groups = "drop"
    ) %>%
    mutate_at(vars(ends_with("_str")), function(x) paste0(" ", x, " "))

  summary_all <-
    data$method_info %>%
    filter(!is_baseline) %>%
    select(method_id, method_name) %>%
    inner_join(overall, by = "method_id") %>%
    left_join(per_dataset, by = "method_id") %>%
    left_join(per_metric, by = "method_id") %>%
    left_join(resources, by = "method_id") %>%
    arrange(desc(method_id))

  column_info <-
    bind_rows(
      tribble(
        ~id, ~name, ~group, ~geom, ~palette,
        "method_name", "Name", "method", "text", NA_character_,
        "mean_score", "Score", "overall", "bar", "overall",
        "error_reason", "Error reason", "overall", "pie", "error_reason"
      ),
      data$dataset_info %>% transmute(
        id = paste0("dataset_", dataset_id),
        name = dataset_name,
        group = "dataset",
        geom = "funkyrect",
        palette = "dataset"
      ),
      data$metric_info %>% transmute(
        id = paste0("metric_", metric_id),
        name = metric_name,
        group = "metric",
        geom = "funkyrect",
        palette = "metric"
      ),
      tribble(
        ~id, ~name, ~label, ~geom,
        "mean_cpu_pct", "%CPU", NA_character_, "funkyrect",
        "mean_peak_memory_log", "Peak memory", "mean_peak_memory_str", "rect",
        "mean_disk_read_log", "Disk read", "mean_disk_read_str", "rect",
        "mean_disk_write_log", "Disk write", "mean_disk_write_str", "rect",
        "mean_duration_log", "Duration", "mean_duration_str", "rect"
      ) %>% mutate(
        group = "resources",
        palette = "resources"
      )
    ) %>%
    mutate(
      options = map2(id, geom, function(id, geom) {
        if (id == "method_name") {
          list(width = 15, hjust = 0)
        } else if (id == "is_baseline") {
          list(width = 1)
        } else if (geom == "bar") {
          list(width = 4)
        } else {
          list()
        }
      }
    )
  )

  list(
    summary_all = summary_all,
    column_info = column_info
  )
}

fh_data_bi <- get_fh_data(data_bi)
fh_data_lp <- get_fh_data(data_lp)

# ----------------------------
# Recompute methods
# ----------------------------


fm_methods <- c("uce", "scimilarity", "scgpt_zeroshot", "geneformer", "scgpt_finetuned", "scprint", "scimilarity_knn")

# data <- data_bi; fh_data <- fh_data_bi; task_name = "Batch Integration"; task_prefix <- "bi_"

combine_fm_results <- function(data, fh_data, task_prefix, task_name) {
  standard_method_info <-
    full_join(
      data$overall_ranking,
      data$method_info,
      by = "method_id"
    ) |>
    mutate(
      is_fm = method_id %in% fm_methods,
    ) |>
    filter(!is_fm, !is_baseline) |>
    arrange(desc(mean_score)) |>
    slice(1, ceiling(n() / 2)) |>
    transmute(
      orig_method_id = method_id,
      orig_method_name = method_name,
      method_id = c("best_standard", "median_standard"),
      method_name = c(
        paste0("Best (", method_name[1], ")"),
        paste0("Median (", method_name[2], ")")
      )
    )

  new_summary_info <- 
    bind_rows(
      left_join(standard_method_info, fh_data$summary_all |> select(-method_name), by = c("orig_method_id" = "method_id")),
      fh_data$summary_all |> filter(method_id %in% fm_methods)
    ) |>
      rename_all(~paste0(task_prefix, .))
  
  new_column_info <- fh_data$column_info |> mutate(
    id = paste0(task_prefix, id),
    group = case_when(
      group == "method" ~ "bi_overall",
      TRUE ~ paste0(task_prefix, group)
    ),
    label = ifelse(is.na(label), label, paste0(task_prefix, label))
  )

  list(
    summary_info = new_summary_info,
    column_info = new_column_info
  )
}

new_bi <- combine_fm_results(data_bi, fh_data_bi, "bi_", "Batch Integration")
new_lp <- combine_fm_results(data_lp, fh_data_lp, "lp_", "Label Projection")

# ----------------------------
# Generate combined FH results
# ----------------------------

data <- 
  full_join(
    new_bi$summary_info |> rename(method_id = bi_method_id),
    new_lp$summary_info |> rename(method_id = lp_method_id),
    by = "method_id"
  ) |>
    mutate(
      method_name = case_when(
        method_id == "best_standard" ~ "Best standard",
        method_id == "median_standard" ~ "Median standard",
        TRUE ~ bi_method_name
      ),
      bi_method_name = case_when(
        method_id %in% c("best_standard", "median_standard") ~ bi_orig_method_name,
        TRUE ~ ""
      ),
      lp_method_name = case_when(
        method_id %in% c("best_standard", "median_standard") ~ lp_orig_method_name,
        TRUE ~ ""
      ),
      mean_score = (bi_mean_score + lp_mean_score) / 2
    ) |>
    arrange(desc(mean_score))

column_info <- bind_rows(
  tribble(
    ~id, ~name, ~group, ~geom, ~palette, ~options,
    "method_name", "Name", "overall_meta", "text", NA_character_, list(width = 6L, hjust = 0),
    "mean_score", "Overall score", "overall_scores", "bar", "overall", list(width = 4L),
    "bi_method_name", "BI method", "bi_overall", "text", NA_character_, list(width = 6L, hjust = 0),
    "bi_mean_score", "BI score", "bi_overall", "bar", "overall", list(width = 4L),
  ),
  new_bi$column_info |> filter(id == "bi_error_reason"),
  new_bi$column_info |> filter(group %in% c("bi_dataset", "bi_metric")),
  tribble(
    ~id, ~name, ~group, ~geom, ~palette, ~options,
    "lp_method_name", "LP method", "lp_overall", "text", NA_character_, list(width = 6L, hjust = 0),
    "lp_mean_score", "LP score", "lp_overall", "bar", "overall", list(width = 4L),
  ),
  new_lp$column_info |> filter(id == "lp_error_reason"),
  new_lp$column_info |> filter(group %in% c("lp_dataset", "lp_metric"))
)

column_groups <-
  tribble(
    ~group, ~palette, ~level1, ~level2,
    "overall_meta", "overall", "Overall", "",
    "overall_scores", "overall", "Overall", "Scores",
    "bi_overall", "overall", "Batch Integration", "",
    "bi_dataset", "overall", "Batch Integration", "Per Dataset",
    "bi_metric", "overall", "Batch Integration", "Per Metric",
    "lp_overall", "overall", "Label Projection", "",
    "lp_dataset", "overall", "Label Projection", "Per Dataset ",
    "lp_metric", "overall", "Label Projection", "Per Metric "
  ) |>
    select(Task = level1, Part = level2, group, palette)

palettes <-
  list(
    overall = funkyheatmap:::default_palettes$numerical$Grays,
    dataset = funkyheatmap:::default_palettes$numerical$Blues,
    metric = funkyheatmap:::default_palettes$numerical$Reds,
    error_reason = setNames(
      c("#8DD3C7", "#FFFFB3", "#BEBADA", "#999999", "#FFFFFF"),
      c("Memory limit exceeded", "Time limit exceeded", "Execution error", "Not applicable", "No error")
    )
  )

row_info <- NULL
row_groups <- NULL
legends <- list(
  list(title = "Overall", palette = "overall", geom = "bar"),
  list(title = "Error reason", palette = "error_reason", geom = "pie", labels = names(palettes$error_reason), color = unname(palettes$error_reason), label_width = 7),
  list(title = "Dataset", palette = "dataset", geom = "funkyrect"),
  list(title = "Metric", palette = "metric", geom = "funkyrect")
)
verify_legends(legends, palettes, column_info, data)


fh <- funky_heatmap(
  data = data,
  column_info = column_info,
  column_groups = column_groups,
  row_info = row_info,
  row_groups = row_groups,
  palettes = palettes,
  legends = legends,
  position_args = position_arguments(
    col_annot_offset = 5,
  )
)

ggsave("fm_plot.pdf", fh, width = fh$width, height = fh$height)
# convert to png with better resolution
system("magick -density 600 fm_plot.pdf fm_plot.png")