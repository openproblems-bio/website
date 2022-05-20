---
title: home
$toc:

---
<m-d-header text="Benchmarking formalized challenges in single-cell analysis" h=1 add-hash></m-d-header>

Computational biology is undergoing a revolution. Recent advances in microfluidic technology enable high-throughput and high-dimensional of individual cells at unprecedented scale. But there's a catch.

Single-cell analysis is _hard_.

Modern single-cell datasets aren't like traditional biological datasets. Not only are there more independent observations in each dataset, there are also more features being measured. This means that standard statistical techniques used in genomic analysis fail to capture the complexity present in single-cell datasets. Unlocking the potential of single-cell biology will require development of new methods for data analysis.

There are many challenges new methods need to overcome. A recent perspective identified [**Eleven Grand Challenges in Single-Cell Data Science**.](https://doi.org/10.1186/s13059-020-1926-6) However, these challenges require formalization before method developers can attempt to solve them. Our goal is to formalize challenges such as these and create a living community-driven state-of-the-art benchmarking platform to facilitate development of single-cell methods.

<m-d-header text="Our inspiration" h=1 add-hash></m-d-header>

We are inspired by the progress machine learning has made in computer vision, natural language processing (NLP), and individualized recommendation. Many of these advances were driven by competition among methods developers against standardized, well-defined computational tasks. Computer vision has [ImageNet](www.image-net.org/), language processing has the [Workshop on Statistical Machine Translation](http://www.statmt.org), recommendation had the [Netflix Prize](https://en.wikipedia.org/wiki/Netflix_Prize). There are hundreds more challenges in machine learning that are catalogued on the [Papers with Code State-of-the-art Leaderboards.](https://paperswithcode.com/sota)

These challenges provide both direction for methods developers and provide a straightforward framework for evaluating methods. It's not surprising that the biggest machine learning advances in the biological sciences have also occurred within the framework of formalized challenges. When DeepMind wanted to tackle protein folding prediction, they pursued state-of-the-art performance in the [Critical Assessment of protein Structure Prediction](https://predictioncenter.org/). Similarly, the [Dream Challenges](http://dreamchallenges.org/challenges/) and Recursion Pharmaceuticals' [RXRX competitions](https://www.rxrx.ai/) strive to build on these large-scale high-reward challenges to drive innovation.

We want to leverage the strengths of these machine learning challenges to drive innovation in computational biology for single-cell analysis.

<m-d-header text="Our approach" h=1 add-hash></m-d-header>
We think there are four key traits that allow these challenges to drive innovation:  
 1. Tasks are formally defined with a clear mathematical interpretation  
 2. Easily accessible gold-standard datasets are publicly available in a ready-to-go standardized format  
 3. One or more quantitative metrics are defined for each task to judge success  
 4. State-of-the-art methods are ranked in a continuously updated leaderboard  

Our goal is to provide an open source, community driven, extensible platform for continuously updated benchmarking of formalized tasks in single-cell analysis. For example, we're interested in ranking dimensionality reduction methods based on their ability to preserve global distances and comparing data denoising methods based on their ability to recover simulated mRNA undercounting.

Open Problems is hosted on GitHub. Benchmarks are evaluated using AWS thanks to generous support from the [Chan Zuckerberg Initiative](https://chanzuckerberg.com/science/). Leaderboards are hosted on our [Results](/results) page. All code, methods, and leadership is driven by broad input from the scientific community.

<m-d-header text="Join us!" h=1 add-hash></m-d-header>

We'd love for you to get involved.  

You can start by [joining our mailing list](https://docs.google.com/forms/d/e/1FAIpQLSe90Oky4-1b0HbdLsp5Yqo9juCd2mq-NlGHU9NHRW1ECok1xQ/viewform?usp=sf_link) to be the first to hear about updates.

Next, check out our [Contributing Guidelines](https://github.com/openproblems-bio/openproblems/blob/master/CONTRIBUTING.md).

Finally, introduce yourself by giving us a 👋 on our [Discord Server](https://discord.gg/sDE7cM4PN7)! You'll find several groups of people here working on different tasks. Check out the different channels and see where you can contribute!