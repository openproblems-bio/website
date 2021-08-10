---
title: "Quickstart"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 2
---

The goal of this guide is to get you started developing submissions for the competition as quickly as possible.

## 1. Register on EvalAI

EvalAI is an open source platform to host machine learning competitions. We're using this tool to evaluate submissions and host the leaderboard. To register for the competition, you must:

1. [Create](https://eval.ai/auth/signup) an Account on EvalAI
2. [Visit](https://eval.ai/web/challenges/challenge-page/1111/overview) the Single-Cell Multimodal Data Integration Challenge page

## 2. Configure your local environment

For this competition, we want competitors to share code and we will evaluate results on a remote server. To facilitate running arbitrary scripts submitted by contestants, we are using [viash](https://viash.io), a tool designed to turn R, Python, C, etc. scripts into Dockerized components that can be executed from the command line and integrated into a workflow system like [Nextflow](https://www.nextflow.io/).

Installing viash has three prerequisites:

* [Docker](https://docs.docker.com/get-docker/)
* Java Runtime ≥8.0, [available](https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot) from OpenJDK

Next, get a copy of the competition Github Repository and run the `bin/init` script. This script will install viash and Nextflow.

```
# The Docker daemon must be running. On MacOS, launch the Docker desktop app instead of `dockerd`
$ dockerd
$ git clone https://github.com/openproblems-bio/neurips2021_multimodal_viash.git
$ cd neurips2021_multimodal_viash
$ ./bin/init
# You need to add the viash binaries to your PATH
$ export PATH=${PWD}/bin:$PATH
```

If you have any issues installing `viash`, please [open](https://github.com/openproblems-bio/neurips2021_multimodal_viash/issues) a GitHub Issue on the competition Github page or ask a question on the competition [Discord](https://discord.gg/Q3RKGMGD3E) server (look for the #viash-help channel).

## 3. Grab a starter kit

You can find a set of starter kits for each task on the [Starter Kits](/neurips_docs/submission/starter_kits/) page.

1. Download the relevant Starter Kit
2. Unzip the kit
3. Make sure you can generate the test submission

```
$ cd starter_kit-predict_modality-python
$ ./generate_submission #
```

If you get a `viash: command not found` error, make sure you've added the binaries

## 4. Start editing the script
