# openproblems.bio unreleased

## MINOR CHANGES

* Added updates button to the NeurIPS 2023 landing page (PR #279).

* Updated the openproblems-v2 submodule (PR #280).

# openproblems.bio v2.3.0

## MAJOR CHANGES

* All tasks were moved from `src/<task_id>` to the `src/tasks/<task_id>` subdirectory (PR #251).

* Upgrade to quarto v1.4 (PR #273).

## MINOR CHANGES

* Minor changes to the documentation pages (PR #248).

* Add documentation link to Neurips 2021 documentation on the Neurips 2021 page (PR #250).

* Add prefix "PR " to PR references in changelog (PR #250).

* Replace "baseline" with "control" in v2 documentation pages (PR #252).

* Add Dark/Light mode theming for Mermaid diagrams (PR #254).

* Use `api` to add more information to the datasets reference documentation (PR #255).

* Extend the documentation on designing the task API (PR #257).

* Inform users that they might need to specify a different value for `--type` in tasks with multiple method / metric subtypes (#259, PR #260).

* Add general information on AnnData and Viash (PR #261).

* Explicitly mention the `__merge__` notation in the docs (PR #267).

* Add link to task issue example (PR #271).

* Add page for NeurIPS 2023 competition (PR #273).

* Add VS Code install to requirements page (PR #275).

# openproblems.bio v2.2.1

## BUG FIXES

* Minor fixes to the documentation pages (PR #246).

# openproblems.bio v2.2.0

## NEW FUNCTIONALITY

* Documentation was added for OpenProblems v2 at `/documentation` (multiple PRs).

* Added an events page at `/events` (PR #227).

## MAJOR CHANGES

* For some of the pages, only render executable code when the 'evaluate_code' profile is active (PR #214).

* Moved competition pages from `/competitions` to `/events` (PR #227). Added redirects to ensure links on external websites keep working.

## MINOR CHANGES

* Update to Quarto 1.3 (PR #221).

* Update license to Creative Commons CC-BY (PR #216).
  
* Revert temporary navbar transition fix (PR #231).

* Revert quarto 1.3 weight changes (PR #236 & PR #244).

* Fix alignment issues in headings (PR #236).

* Fix mermaid background rendering (PR #243).

* Make the funkyheatmap interactive settings visible (PR #169).

## BUG FIX

* Rename `create_skeleton` to `create_component` in documentation (PR #213).

* Add `target: _blank` to external links in navbar (PR #230).

* Revert intentional typo `.thumnail-image` to `.thumbnail-image` (PR #232)

* Added `../docs.css` to neurips 2021 documentation to activate the `.thumbnail-image` change (PR #232).

* Fix broken links (on other websites) by adding redirects to previously existing pages (PR #227).
  
* Fix redirects with subdirs to events link (PR #245).

# openproblems.bio v2.1.2

## MINOR CHANGES

* Updating task images from `.png` to `.svg` (PR #205).
* Set funkyheatmap colors for dark mode via js instead of css (PR #208).

# openproblems.bio v2.1.1

## BUG FIXES

* Fixed a typo in batch_integration_embed task description (PR #201)
* Fix `link-external-filter` to recognise internal filters on published website (#202)

# openproblems.bio v2.1.0

Dark mode has been added to the website, along with minor changes such as
an improved hero image for the results and bibliography pages and the removal
of a stub task.

## NEW FUNCTIONALITY

* Dark mode was added (PR #153, PR #162, PR #172, PR #173, PR #184, PR #190, PR #191, PR #194).

## MINOR CHANGES

* Ported missing site metadata (PR #160).

* Changed the results and bibliography heros (PR #178, PR #181).

* Removed sub-stub regulatory effect prediction task (PR #197).
  
## BUG FIXES

* Fix internal links being treated as external links in PR eviews (PR #179).
* FIx `link-external-filter` te recognise internal filters on published website (#202)

# openproblems.bio v2.0.0

Quarto reimplementation of the original openproblems.bio website.

Pages:

* Main page

* Benchmark results:
  - Per task:
    - Summary funky heatmap (implemented in funkyheatmap-js)
    - Results table (using DataTables)
    - Additional information on datasets, methods, metrics
    - QC report
    - Data files as jsons
  - Overall QC report

* Competitions pages:
  - NeurIPS 2021
  - NeurIPS 2021 Documentation
  - NeurIPS 2022

* Team view

* Documentation
  - OpenProblems v1 (links to v1 repo CONTRIBUTING.md)
  - OpenProblems v2 (links to v2 repo CONTRIBUTING.md)
  - Bibliography
  - OpenProblems v2 WIP documentation (hidden)

# openproblems.bio v1.0.0

Website created with Hugo + Wowchemy.
