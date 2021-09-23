---
title: "Quickstart"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 2
---

The goal of this guide is to get you started developing submissions for the competition as quickly as possible. This section will detail the necessary steps to create your first submission.

## 1. Register on EvalAI

EvalAI is an open source platform to host machine learning competitions. We're using this tool to evaluate submissions and host the leaderboard. To register for the competition, you must:

1. [Create](https://eval.ai/auth/signup) an Account on EvalAI
2. [Visit](https://eval.ai/web/challenges/challenge-page/1111/overview) the Single-Cell Multimodal Data Integration Challenge page
3. [Register](https://eval.ai/web/challenges/challenge-page/1111/participate) by creating a new team on EvalAI. You can change your team details later or merge teams.

## 2. Configure your local environment

For this competition, we want competitors to share code and we will evaluate results on a remote server. To facilitate running arbitrary scripts submitted by contestants, we are using [Viash](https://viash.io), a tool designed to turn R and Python scripts into Dockerized components that can be executed from the command line and integrated into a workflow system like [Nextflow](https://www.nextflow.io/).

Before you get started with the competition you will need to install two prerequisites:

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install Java Runtime ≥8.0, available from [OpenJDK](https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot)

## 3. Grab a starter kit

You can find a set of starter kits for each task below or on the [GitHub releases](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases) of the competition codebase. Download the starter kit which is most relevant to you and unzip it in a directory.

Task 1 - Predict Modality

* [Starter Kit in Python](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/latest/download/starter_kit-predict_modality-python.zip)
* [Starter Kit in R](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/latest/download/starter_kit-predict_modality-r.zip)

Task 2 - Match Modality

* [Starter Kit in Python](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/latest/download/starter_kit-match_modality-python.zip)
* [Starter Kit in R](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/latest/download/starter_kit-match_modality-r.zip)

Task 3 - Joint Embedding

* [Starter Kit in Python](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/latest/download/starter_kit-joint_embedding-python.zip)
* [Starter Kit in R](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/latest/download/starter_kit-joint_embedding-r.zip)


## 4. Generate your first submission

To make sure your local environment is set up correctly, first run the `2_generate_submission.sh` script. This script triggers a Nextflow workflow to:
1. Build a [viash component](https://viash.io/docs/getting_started/what_is_a_viash_component/) of the method in `script.py/R` using the configuration specified in `config.vsh.yaml`.
2. Sync the training datasets from S3 (`s3://openproblems-bio/public/phase1-data`) to a local drive (`output/datasets/`).
3. Apply the containerized method on the training datasets.
4. Create a `submission.zip` file that can be uploaded to EvalAI for evaluation on the competition data and registration of the method on the leaderboard.

If this workflow finishes successfully, you'll see something like this:

```
$ scripts/2_generate_submission.sh
...
######################################################################
##            Generating submission files using nextflow            ##
######################################################################
N E X T F L O W  ~  version 21.04.1
Pulling openproblems-bio/neurips2021_multimodal_viash ...
Launching `openproblems-bio/neurips2021_multimodal_viash` [intergalactic_roentgen] - revision: a784bb6c4b [main_build]
[f6/c705c5] process > method:method_process (openproblems_bmmc_multiome_phase1) [100%] 2 of 2 ✔

######################################################################
##                        Submission summary                        ##
######################################################################
Please upload your submission at the link below:
  https://eval.ai/web/challenges/challenge-page/1111/submission

Or use the command below create a private submission:
> evalai challenge 1111 phase 2278 submit --file submission.zip --large --private

Or this command to create a public one:
> evalai challenge 1111 phase 2278 submit --file submission.zip --large --public

Good luck!
```

Make note of the outputs generated in the nextflow step. If all went well, you should see a 100% success rate.

## 5. Submitting to EvalAI

To upload the submission, you have two options:
* Upload the submission via https://eval.ai/web/challenges/challenge-page/1111/submission
* Use the [EvalAI-CLI](https://github.com/Cloud-CV/evalai-cli) to upload the submission following the instructions outputted by the generate script.

Once your method is submitted, you can navigate to the [My Submissions](https://eval.ai/web/challenges/challenge-page/1111/my-submission) tab for the competition and select the phase that matches your recent submission. Here you will find a table that lists each submission you've uploaded for a given phase. Once the "Status" column is marked "Finished" you can view the `results.json` file that provides the method performance. Note that it might take up to 5 minutes for your submission to update from "Running" to "Finished", and that your submission might have to wait in a queue for an undetermined amount of time depending on the number of submissions being run on the submission server.

If you need any help, please reach out on the competition [Discord](https://discord.gg/Q3RKGMGD3E) server. See the `#troubleshooting` or `#viash-help` channels.
