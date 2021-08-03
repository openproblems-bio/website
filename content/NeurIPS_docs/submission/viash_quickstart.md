---
title: "Getting started with Viash"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 2
---

## Getting started
By providing some metadata regarding its functionality and the platform
on which you want to run the software, Viash can help you turn
[supported scripts](https://viash.io/docs/creating_components/supported_languages/) into
an executable component.  
These components can be used to:

-   Seamlessly execute your script natively on the host platform.
-   Easily resolve any dependencies by running the script in an
    automatically generated [Docker](https://www.docker.com/) container.
-   Automatically wrap your script in an executable with a
    [CLI](https://en.wikipedia.org/wiki/Command-line_interface) and
    `--help` functionality.
-   Combine multiple scripts in a [Nextflow](https://www.nextflow.io/)
    pipeline.
-   Unit-test your script to ensure that it works at all times.

## Example use cases

Here are a few use cases which serve as motivation for Viash:

<!-- TODO: Rewrite use cases, the reason why Viash helps in those situations should be crystal clear to someone that has never seen Viash before, this part of the docs is presented before the installation after all. Ideally each of these should have "Viash can help here by../In this case, Viash can.../etc." -->

-   **The script you wrote needs to be made more user friendly by using
    a CLI that describes the accepted arguments.** By wrapping your
    script in a component, Viash provides an intuitive CLI out of the
    box.
-   **You want to combine several tools in a pipeline and every tool has
    specific requirements on how they should be run. Even worse: some
    requirements might directly conflict with each other.** Viash can
    help you by running each tool in its own Docker container with
    specific software versions. You can turn the components into a
    pipeline by using
    [scripting](https://viash.io//docs/creating_pipelines/scripted_pipeline/) or
    [Nextflow](https://viash.io//docs/creating_pipelines/platform-nextflow/).
-   **Your next data analysis project is very similar to the previous
    project, so you copy and paste the source code. Unfortunately, you
    detect a bug in some of your code, so now you need to go back and
    fix the same bug in all the different projects.** By using Viash,
    you can split the project up in reusable components, and you’ll only
    need to apply fixes in a single location.
-   **You want to look back at a data analysis you performed two years
    ago. Unfortunately, the software you used back then is not supported
    anymore, or the newest version produces totally different results.**
    With Viash you can package the older version together with its
    dependencies in an executable so you don’t have to worry about
    conflicts or deprecated versions
-   **You developed a [Jupyter](https://jupyter.org/) notebook report
    for a data analysis. You wish to share it with your colleague, only
    to spend two hours installing your [Conda](https://docs.conda.io/)
    stack on their laptop.** Viash can help you by bundling your scripts
    along with the dependencies into components that can run in a Docker
    container.

## Getting started

The menu on the left contains all of the topics per category on using
Viash. Most topics are in order of complexity per category.  
To start off, we recommend you take a look at the following guides:

-   [Installing Viash](https://viash.io/docs/getting_started/installation)
-   [What is a Viash
    Component?](https://viash.io//docs/getting_started/what_is_a_viash_component)

Once you have Viash installed and have taken a look at the basics, check
out one of the language specific guides in the **CREATING VIASH
COMPONENTS** category to learn how to create your very own component in
your preferred language.

The following pages are good starting points to delve a bit deeper into
using Viash:

-   [Config File](https://viash.io//docs/reference_config/config/)
-   [Functionality](https://viash.io//docs/reference_config/functionality/)
-   [Native Platform](https://viash.io//docs/reference_config/platform-native/)
-   [Docker Platform](https://viash.io//docs/reference_config/platform-docker/)
-   [Executables With a Docker
    Backend](/docs/running/executables-docker/)

Once you’re comfortable with the basics, here are some more advanced
topics:

-   [Namespaces](https://viash.io//docs/projects/namespaces/)
-   [Creating a Scripted
    Pipeline](/docs/creating_pipelines/scripted_pipeline/)
-   [Nextflow Platform](https://viash.io//docs/reference_config/platform-nextflow/)
-   [Creating a Nextflow
    Pipeline](/docs/creating_pipelines/platform-nextflow/)
-   [Dynamic Config Modding](https://viash.io//docs/advanced/config_mods/)

If you wish to contribute to Viash or the documentation, take a look at
our [Contributing Guidelines](https://viash.io//docs/contributing/guidelines/).
