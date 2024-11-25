repositories <- c(
    "openproblems-bio/task_denoising",
    "openproblems-bio/task_dimensionality_reduction",
    "openproblems-bio/task_batch_integration",
    "openproblems-bio/task_cell_cell_communication",
    "openproblems-bio/task_label_projection",
    "openproblems-bio/task_spatial_decomposition",
    "openproblems-bio/task_predict_modality"
)

cache_repository <- function(repo) {
    # get the repository name
    repo_dir <- file.path(Sys.getenv("HOME"), ".cache", "openproblems", "repositories", repo)
    
    # clone the repository
    if (!dir.exists(paste0(repo_dir, "/.git"))) {
        zzz <- processx::run("git", c("clone", paste0("https://github.com/", repo), repo_dir))
    }

    # fetch the latest changes
    zzz <- processx::run("git", c("fetch", "--all"), wd = repo_dir)

    # reset the repository to the latest commit
    if (repo == "openproblems-bio/task_spatial_decomposition") {
        zzz <- processx::run("git", c("pull", "origin", "add-missing-authors"), wd = repo_dir)
    } else if (repo == "openproblems-bio/task_dimensionality_reduction") {
        zzz <- processx::run("git", c("pull", "origin", "add_author"), wd = repo_dir)
    } else {
        zzz <- processx::run("git", c("pull", "origin", "main"), wd = repo_dir)
    }

    # return the path to the repository
    return(repo_dir)
}

find_task_info <- function(repo_dir) {
    # find all authors in the repository
    # task_info <- list.files(repo_dir, pattern = "task_info.yaml", full.names = TRUE, recursive = TRUE)
    # task_info <- task_info[grep("/api/task_info.yaml", task_info)]

    # if (length(task_info) > 0) {
    #     return(task_info)
    # }

    viash_yaml <- list.files(repo_dir, pattern = "_viash.yaml", full.names = TRUE, recursive = TRUE)

    return(viash_yaml)
}


for (repo in repositories) {
    repo_dir <- cache_repository(repo)
    task_info_files <- find_task_info(repo_dir)

    for (task_info_file in task_info_files) {
        task_info <- suppressWarnings(yaml::read_yaml(task_info_file))
        task_name <- gsub("task_", "", task_info$name)

        if (!task_name %in% names(tasks)) {
            tasks[[task_name]] <- list()
        }

        task_label <- task_info$label
        if (is.null(task_label)) {
            task_label <- stringr::str_to_title(gsub(" ", "_", tolower(task_name)))
        }
        if (is.null(tasks[[task_name]]$label)) {
            tasks[[task_name]]$label <- task_label
        }
        if (is.null(tasks[[task_name]]$authors)) {
            tasks[[task_name]]$authors <- list()
        }
        
}