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

Before you get started with the competition you will need to install two  prerequisites:

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install Java Runtime ≥8.0, available from [OpenJDK](https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot)

## 3. Grab a starter kit

You can find a set of starter kits for each task on the [Starter Kits](/neurips_docs/submission/starter_kits/) page.

1. Download the relevant Starter Kit
2. Unzip the kit
3. Make sure you can generate the test submission
    ```ruby
    $ cd starter_kit-predict_modality-python
    $ ./generate_submission
    ```  

The generate_submission script triggers a Nextflow workflow to:
1. Build a [viash component](https://viash.io/docs/getting_started/what_is_a_viash_component/) of the method in `script.py` using the configuration specified in `config.vsh.yaml`.
2. Evaluate the containerized method on 32 public testing datasets stored in `s3://neurips2021-multimodal-public-datasets/`.
3. Create a `submission.zip` directory that can be uploaded to EvalAI for evaluation on the competition data and registration of the method on the leaderboard.

If this workflow finishes successfully, then your local environment is set up for the competition!

{{< callout note >}}
If you get a `viash: command not found` error, make sure you've added the binaries
{{</ callout >}}

## 4. Start editing the script

The starter kit has a simple method in `script.py` with a corresponding configuration in `config.vsh.yaml`, but you'll want to update these for your method.

A full set of instructions for editing these can be found in the [Starter Kit to Submission](/neurips_docs/submission/starter_kits/) documentation.

## 5. Submitting to EvalAI

Once you have editing the starter kit to include the method you would like to submit, run the `generate_submission.sh` script, which will create a `submission.zip` file.

To upload the submission, you have two options:
* Upload the submission on https://eval.ai/web/challenges/challenge-page/1111/submission
* Use the [EvalAI-CLI](https://github.com/Cloud-CV/evalai-cli) to upload the submission

### Upload on the website

1. Go to  https://eval.ai/web/challenges/challenge-page/1111/submission and log in to your account
2. Select the appropriate phase for your submission. Currently, only the Development Phase for each task is open. Make sure to select the correct task.
3. Select the submission type. Most folks will use the Upload File option.
4. Set the visibility. Public submissions will be evaluated and registered to the leaderboard. Private submissions will still be evaluated, but the performance will only be available to you. You may change the visibility after submission.
5. Add optional method name, description, etc. This information will be visible on the leaderboard for Public submissions.
6. Hit Submit

Once your method is submitted, you can navigate to the [My Submissions](https://eval.ai/web/challenges/challenge-page/1111/my-submission) tab for the competition and select the Phase that matches your recent submission. Here you will find a table that lists each submission you've uploaded for a given phase. Once the Status column is marked "Finished" you can view the `results.json` file that provides the method performance.

If you need any help, please reach out on the competition [Discord](https://discord.gg/Q3RKGMGD3E) server. See the #troubleshooting or #viash-help channels.
