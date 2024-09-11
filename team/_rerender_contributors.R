library(rlang)

repositories <- c(
    "openproblems-bio/openproblems",
    # "openproblems-bio/task_dimensionality_reduction",
    # "openproblems-bio/task_spatially_variable_genes",
    "openproblems-bio/task_perturbation_prediction"
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
    zzz <- processx::run("git", c("pull", "origin", "main"), wd = repo_dir)

    # return the path to the repository
    return(repo_dir)
}

find_task_info <- function(repo_dir) {
    # find all authors in the repository
    task_info <- list.files(repo_dir, pattern = "task_info.yaml", full.names = TRUE, recursive = TRUE)
    task_info <- task_info[grep("/api/task_info.yaml", task_info)]

    if (length(task_info) > 0) {
        return(task_info)
    }

    viash_yaml <- list.files(repo_dir, pattern = "_viash.yaml", full.names = TRUE, recursive = TRUE)

    return(viash_yaml)
}

render_author <- function(author) {
    # try to assign an image for the author
    #   - if available, use github image
    #   - else if available, use gravatar
    #   - otherwise, use a default
    out_image <- 
        if (!is.null(author$info$github)) {
            paste0("https://www.github.com/", author$info$github, ".png")
        } else if (!is.null(author$info$email)) {
            email_clean <- tolower(stringr::str_trim(author$info$email))
            checksum <- digest::digest(email_clean, algo = "md5", serialize = FALSE)
            paste0("https://www.gravatar.com/avatar/", checksum)
        } else {
            "/images/avatar.svg"
        }

    # process links
    process_links <- list(
        email = function(value) {
            list(
                icon = "bi-envelope",
                text = "E-mail",
                href = paste0("mailto:", value)
            )
        },
        github = function(value) {
            list(
                icon = "bi-github",
                text = "GitHub",
                href = paste0("https://github.com/", value)
            )
        },
        orcid = function(value) {
            list(
                icon = "fa-brands fa-orcid",
                text = "ORCID",
                href = paste0("https://orcid.org/", value)
            )
        },
        linkedin = function(value) {
            list(
                icon = "bi-linkedin",
                text = "LinkedIn",
                href = paste0("https://www.linkedin.com/in/", value)
            )
        }
    )
    out_links <- list()
    for (link_name in names(author$info)) {
        if (link_name %in% names(process_links)) {
            link_info <- process_links[[link_name]](author$info[[link_name]])
            out_links <- c(out_links, list(link_info))
        }
    }

    out <- list(
        title = author$name,
        image = out_image,
        role = paste(stringr::str_to_title(author$roles), collapse = ", "),
        about = list(
            template = "jolla",
            links = out_links
        )
    )
    if (!is.null(author$info$organizations)) {
        out$organizations <- author$info$organizations
    }
    txt <- paste0("---\n", yaml::as.yaml(out), "---\n")

    txt
}


tasks <- list()

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
        
        for (author in task_info$authors) {
            author_id <- gsub("[^a-z_]", "", gsub(" ", "_", tolower(author$name)))
            if (!author_id %in% names(tasks[[task_name]]$authors)) {
                tasks[[task_name]]$authors[[author_id]] <- author
            }
        }
    }
}

for (task_name in names(tasks)) {
    task <- tasks[[task_name]]
    for (author_id in names(task$authors)) {
        if (author_id %in% c(
            "robrecht_cannoodt",
            "scott_gigante",
            "malte_d_luecken",
            "daniel_burkhardt"
        )) {
            next
        }
        author <- task$authors[[author_id]]
        
        txt <- render_author(author)
        file_path <- file.path("team", "task_contributors", paste0(author_id, "/index.qmd"))

        if (!dir.exists(dirname(file_path))) {
            dir.create(dirname(file_path), recursive = TRUE)
        }
        
        writeLines(txt, file_path)
    }
}

teams <- list.dirs("team", full.names = FALSE, recursive = FALSE)
teams <- teams[!teams %in% c("core_members", "scientific_advisors")]

teams_headers <- paste0(
"  - id: ", teams, "
    contents: ", teams, "/*/index.qmd
    type: grid
    template: members.ejs
    sort: ''"
)
teams_index <- paste0(
"## ", stringr::str_to_title(gsub("_", " ", teams)), "

:::{#", teams, "}
:::
"
)
team_qmd <- paste0(
"---
title: \"Contributors\"
toc: false
page-layout: full
anchor-sections: false
listing:
  - id: core_members
    contents: core_members/*/index.qmd
    type: grid
    template: members.ejs
    sort: ''
  - id: scientific_advisors
    contents: scientific_advisors/*/index.qmd
    type: grid
    template: members.ejs
    sort: ''
", paste(teams_headers, collapse = "\n"), "
css: team.css
---

## Core members

:::{#core_members}
:::

## Scientific Advisors

:::{#scientific_advisors}
:::

", paste(teams_index, collapse = "\n"), "
")

writeLines(team_qmd, "team/index.qmd")
