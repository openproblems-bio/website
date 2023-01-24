+++
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://sourcethemes.com/academic/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 20  # Order that this section will appear.

title = ""
subtitle = ""

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "1"


[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS.
 css_style = ""

 # CSS class.
 css_class = ""


+++
# Benchmarking formalized challenges in single-cell analysis

Computational biology is undergoing a revolution. Recent advances in microfluidic technology enable high-throughput and high-dimensional of individual cells at unprecedented scale. But there's a catch.

Single-cell analysis is _hard_.

Modern single-cell datasets aren't like traditional biological datasets. Not only are there more independent observations in each dataset, there are also more features being measured. This means that standard statistical techniques used in genomic analysis fail to capture the complexity present in single-cell datasets. Unlocking the potential of single-cell biology will require development of new methods for data analysis.

There are many challenges new methods need to overcome. A recent perspective identified [**Eleven Grand Challenges in Single-Cell Data Science**.](https://doi.org/10.1186/s13059-020-1926-6) However, these challenges require formalization before method developers can attempt to solve them. Our goal is to formalize challenges such as these and create a living community-driven state-of-the-art benchmarking platform to facilitate development of single-cell methods.

# Our inspiration

We are inspired by the progress machine learning has made in computer vision, natural language processing (NLP), and individualized recommendation. Many of these advances were driven by competition among methods developers against standardized, well-defined computational tasks. Computer vision has [ImageNet](www.image-net.org/), language processing has the [Workshop on Statistical Machine Translation](http://www.statmt.org), recommendation had the [Netflix Prize](https://en.wikipedia.org/wiki/Netflix_Prize). There are hundreds more challenges in machine learning that are catalogued on the [Papers with Code State-of-the-art Leaderboards.](https://paperswithcode.com/sota)

These challenges provide both direction for methods developers and provide a straightforward framework for evaluating methods. It's not surprising that the biggest machine learning advances in the biological sciences have also occurred within the framework of formalized challenges. When DeepMind wanted to tackle protein folding prediction, they pursued state-of-the-art performance in the [Critical Assessment of protein Structure Prediction](https://predictioncenter.org/). Similarly, the [Dream Challenges](http://dreamchallenges.org/challenges/) and Recursion Pharmaceuticals' [RXRX competitions](https://www.rxrx.ai/) strive to build on these large-scale high-reward challenges to drive innovation.

Of course, computational single-cell methods have seen a lot of innovation in the past years. This is partly driven by benchmarking efforts, that quantify progress and set goals. Yet, we noticed that many successful methods draw from innovations in computer vision and other areas of machine learning that are more mature. We want to promote this cross-fertilization to increase the pace of innovation for single-cell analysis, and enable machine learning scientists to use their skills to address relevant tasks in digital biomedical research.

# Our approach
We think there are four key traits that allow these challenges to drive innovation:  
 1. Tasks are formally defined with a clear mathematical interpretation  
 2. Easily accessible gold-standard datasets are publicly available in a ready-to-go standardized format  
 3. One or more quantitative metrics are defined for each task to judge success  
 4. State-of-the-art methods are ranked in a continuously updated leaderboard  

Our goal is to provide an open source, community driven, extensible platform for continuously updated benchmarking of formalized tasks in single-cell analysis. For example, we're interested in ranking dimensionality reduction methods based on their ability to preserve global distances and comparing data denoising methods based on their ability to recover simulated mRNA undercounting.

Open Problems is hosted on GitHub. Benchmarks are evaluated using AWS thanks to generous support from the [Chan Zuckerberg Initiative](https://chanzuckerberg.com/science/). Leaderboards are hosted on our [Results](/results) page. All code, methods, and leadership is driven by broad input from the scientific community.

# Who are we?
We are machine learning scientists, computational biologists, and single-cell data analysts who formalize computational tasks in single-cell analysis and collaborate with molecular biologists to generate benchmarking datasets that challenge methods and method developers to perform ever better.

Meet the contributors on [our Team page](/team).

# Join us!

We'd love for you to get involved.  

You can start by [joining our mailing list](https://docs.google.com/forms/d/e/1FAIpQLSe90Oky4-1b0HbdLsp5Yqo9juCd2mq-NlGHU9NHRW1ECok1xQ/viewform?usp=sf_link) to be the first to hear about updates.

Next, check out our [Contributing Guidelines](https://github.com/openproblems-bio/openproblems/blob/master/CONTRIBUTING.md).

Finally, introduce yourself by giving us a 👋 on our [Discord Server](https://discord.gg/sDE7cM4PN7)! You'll find several groups of people here working on different tasks. Check out the different channels and see where you can contribute!
