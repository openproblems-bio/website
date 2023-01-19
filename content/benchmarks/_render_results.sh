#!/bin/bash

template_qmd=content/benchmarks/_task_template.qmd
output_qmd=content/benchmarks/dimensionality_reduction/index.qmd

cat > $output_qmd << HERE
---
title: Dimensionality reduction
summary: Foo
---
HERE
cat $template_qmd >> $output_qmd


quarto render $output_qmd --to hugo-md