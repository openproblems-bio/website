# openproblems.bio v2.2.0

## NEW FUNCTIONALITY

* Documentation was added for future OpenProblems v2 (#199). This is still in development and the main focus was on how to contribute to already existing tasks in OpenProblems v2. Content:

  * Add intro text to documentation.

  * Add `contribute` intro and pages.

  * `contribute/Requirements`: Describes how to set up your system to start contributing.

  * `contribute/Getting started`: Describes how to get started with contributing.

  * `contribute/Add a dataset`: Describes how to create a new dataset loader.

  * `contribute/Add a method`: Describes how to create a new method for an existing task.

  * `contribute/Add a baseline`: Describes how to create a new control method for an existing task.

  * `contribute/Add a metric`: Describes how to create a new metric for an existing task.
    
  * `contribute/Run tests`: Describes how to run tests for the newly created components.

  * `contribute/Create Pull Request`: Describes how to contribute your changes.

  * Add `More information` intro and pages

  * `More information/Project structure`: Describes the repository structure and technology stack

  * `More information/Code of conduct`: Describes the Code of conduct that OpenProblems uses.
    
  * `More information/FAQ`: Frequently Asked Questions

  * `More information/Troubleshooting`: Describes the most common errors that can occur when contributing/developing.

## MAJOR CHANGES

* For some of the pages, only render executable code when the 'evaluate_code' profile is active (#214).

## MINOR CHANGES

* Update to Quarto 1.3 (#221).

* Update license to Creative Commons CC-BY (#216)
  
* Revert temporary navbar transition fix (#231)

* Revert quarto 1.3 weight changes (#236).

* Fix alignment issues in headings (#236).

* Fix mermaid background rendering (#243)

## BUG FIX

* Rename `create_skeleton` to `create_component` in documentation (#213).

* Add `target: _blank` to external links in navbar (#230).

* Revert intentional typo `.thumnail-image` to `.thumbnail-image` (#232)

* add `../docs.css` to neurips 2021 documentation to activate the `.thumbnail-image` change (#232)


# openproblems.bio v2.1.2

## MINOR CHANGES

* Updating task images from `.png` to `.svg` (#205).
* Set funkyheatmap colors for dark mode via js instead of css (#208).

# openproblems.bio v2.1.1

## BUG FIXES

* Fixed a typo in batch_integration_embed task description (#201)
* Fix `link-external-filter` to recognise internal filters on published website (#202)

# openproblems.bio v2.1.0

Dark mode has been added to the website, along with minor changes such as
an improved hero image for the results and bibliography pages and the removal
of a stub task.

## NEW FUNCTIONALITY

* Dark mode was added (#153, #162, #172, #173, #184, #190, #191, #194).

## MINOR CHANGES

* Ported missing site metadata (#160).

* Changed the results and bibliography heros (#178, #181).

* Removed sub-stub regulatory effect prediction task (#197).
  
## BUG FIXES

* Fix internal links being treated as external links in PR previews (#179).
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
