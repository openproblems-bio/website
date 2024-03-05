# openproblems.bio unreleased

## MAJOR CHANGES

* Update Dimensionality Reduction task to OpenProblems v2 results (PR #326)

# openproblems.bio v2.3.6

## NEW CONTENT

* Add an event page for the Weekly wednesday work meeting (PR #299).

* Add `Advanced_topics` pages to documentation (PR #300).

* Add `your first contribution` page to documentation (PR #300).

* Add `Datasets` pages (PR #303).

* Add nextflow used resources to benchmark results (PR #309).

* Add git branch naming convention to documentation (PR #313).

## NEW FUNCTIONALITY

* Add gloassary function to pages and a glossary page (PR #300). 

## MAJOR CHANGES

* Update `fundamentals` pages (PR #300).
  
* Refactor the reference view (PR #300).

* Update `reference` documentation (PR #300).

* Update Neurips2021 datasets categories (PR #323).

## MINOR CHANGES

* Several infrastructure updates (PR #298):

  - Update R packages
  - Remove Python from list of dependencies
  - Update Quarto
  - Fixes to styling
  - Simplify footer
  - Update openproblems-v2 submodule

* Updates to the way tasks are rendered (PR #296):

  - Show task motivation, if present.
  - Allow multiple citations for datasets, methods, and metrics.
  - Render dataset name instead of dataset id in figures and tables.
  - Change the way bibliographic references are rendered.

* Update documentation (PR #300).

* Update `events` pages (PR #300).

* update `results` pages (PR #300).

* Update styles (PR #300).

* Relocate Style files to `styles` directory (PR #300).

* Update results `dataset_info.json` file (PR #306).

* Add benchmark statistics (PR #308).

* Update benchmark listing cards (PR #308).

* Update card styling (PR #308).

* Update neurips 2021 datasets data with new dataset_id (PR #315).

* Update to funkyheatmapjs v0.2.5 (PR #316).
  
* Add CSS to fix not active tab color in dark mode (PR #319).

* Improvements to the documentation (PR #317).
  - Refer to `task_info.yml` in multiple places.
  - Use glossary to help users find information more quickly.

* Remove custom css in events.css (PR #318).

## BUG FIXES

* Updated the `openproblems-v2` submodule (PR #295). This fixes a deprecation error due to an update in ruamel.yaml.

* Add redirect from `/benchmark_dataset` to `/events/2021-09_neurips/documentation/data/dataset.html` (#292, PR #295).

* Fixed minor issues in qmd files (PR #295).

* Fix missing metrics in the results table (PR #301).

* Fix theme styling with quarto v1.4 update (PR #303).

# openproblems.bio v2.3.5

## MINOR CHANGES

* Update Neurips 2023 hero.

## BUG FIXES

* Fix CI failure by updating the `openproblems-v2` submodule (PR #291).

# openproblems.bio v2.3.4

## MINOR CHANGES

* Update Neurips 2023 title and button to kaggle page (PR #289).

## BUG FIXES

* Fix viash cheat sheet URL (PR #289)

# openproblems.bio v2.3.3

## MINOR CHANGES

* Update renv to v1.0.2 to improve processing time. (PR #287)

* Add more information about task_info.yaml to the documentation (PR #285).

* Minor updates to the NeurIPS 2023 landing page.

# openproblems.bio v2.3.2

## MINOR CHANGES

* Minor updates to the NeurIPS 2023 landing page (PR #286).

# openproblems.bio v2.3.1

## MINOR CHANGES

* Added updates button to the NeurIPS 2023 landing page (PR #279).

* Remove old hero image (PR #280).

* Reference base-images in `create-component` pages (PR #282)

## BUG FIXES

* Updated the openproblems-v2 submodule (PR #280).

  - Docker base images were renamed.

  - File format specification files were renamed from `**/api/anndata_*.yaml` to `**/api/file_*.yaml`.

* Restored summary figures by updating funkyheatmapjs (PR #283).

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

* changed cheat sheet to link hosted on viash.io (PR #276)

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
