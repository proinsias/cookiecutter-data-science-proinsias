# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: project-1
#     language: python
#     name: project-1
# ---

import datetime as dt

today = dt.date.today()

# %% [markdown]
"""
---
title: "Quarto Basics"
date: "`r {{today}}`"
author:
  - name: Example Author
    id: jc
    orcid: 0000-0001-1111-1111
    email: example@author.org
    affiliation:
      - name: Brown University
        city: Providence
        state: RI
        url: www.brown.edu
date-format: long
citation:
  url: https://example.com/summarizing-output
# citation: true
citation-location: margin
execute:
  cache: true  # false or refresh
  echo: false  # Disable showing code.
  eval: true  # If false, just echo code into output.
  output: false # Disable showing output
  include: false # Catch all
crossref:
  ref-hyperlink: false # (default is true)
format:
  beamer: default
  docx: default
  gfm: default  # Create static GitHub markdown from qmd or ipynb files.
  html:  # This is default format.
    abstract: >
      Text.
    abstract-title: Abstract.
    author: Francis
    code-fold: true  # Fold code.
    code-line-numbers: true
    code-overflow: scroll  # or wrap
    code-summary: "Summary text"
    code-tools: true  # Add a menu to handle code folding.
    date: 2024-08-02 11:59
    date-modified: 2024-08-02 11:59
    doi: https://doi.org/10.1126/science.aar3646
    email-obfuscation: javascript  # or references, or none
    fig-dpi: 90
    fig-responsive: true
    grid:
      margin-width: 350px
    html-math-method: katex  # or plain, webtex, gladtex, mathml, mathjax, katex
    self-contained: true
    subtitle: title
    title: title
  pdf:
    geometry:
      - top=30mm
      - left=20mm
    number-sections: true
    toc: true
    toc-depth: 1  # default is 3.
    toc-expand: true
    toc-location: body  # left, right (default), left-body, right-body
    toc-title: ToC
  pptx: default
highlight-style: pygments
jupyter: python3
number-sections: true
output: true
reference-location: margin  # Put footnotes in the right margin
toc: true
---
"""

# %% [markdown]
# Here is a Python code cell:

import os

os.cpu_count()

# %% [markdown]
"""
Use LaTeX to write equations:

$E = mc^{2}$

$$
\chi' = \sum_{i=1}^n k_i s_i^2
$$ {#eq-stddev}

Note the use of an equation label at the end of this LaTeX section.

Example of a cross-reference: For a demonstration of a line plot on a polar axis, see @fig-polar.

Note the yaml-formatted, specially-prefixed comment to add the label and fig-cap options in the code.
"""

# %%
#| label: fig-polar
#| fig-align: default  # or left, right, center.
#| fig-alt: "abc"
#| fig-cap: "A line plot on a polar axis"
#| fig-column: page-right
#| fig-height: 3
#| fig-link: fig-target  # Hyperlink target for figure
#| fig-width: 11
#| cap-location: margin
#| column: page  # Always figure display to span out beyond the normal body text column.
#| column: screen-inset  # Allow figure to occupy the full width of the screen, with a small inset.
#| echo: true  # Show the code for this cell.
#| error: true  # Include errors.
#| fig-subcap:  # Treats cells with multiple outputs as subfigures.
#|   - "Gapminder: 1957"
#|   - "Gapminder: 2007"
#| include: true  # Catch all for preventing any output (code or results) from being included in output.
#| layout-ncol: 2  # Side-by-side layout with two columns.
#| lst-label: "abc"  # Unique label for code listing (used in cross references)
#| lst-cap: "Caption for code listing"
#| panel: tabset  # or input, sidebar, fill, center.
#| tags: abc
#| warning: true  # Show warnings.

import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(
  subplot_kw = {'projection': 'polar'}
)
fig.set_size_inches(12, 7)
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()

# %%
import plotly.express as px

gapminder = px.data.gapminder()
gapminder2007 = gapminder.query('year == 2007')
fig = px.scatter(gapminder2007,
                 x='gdpPercap', y='lifeExp', color='continent',
                 size='pop', size_max=60,
                 hover_name='country')
fig.show()

# %%
#| tbl-cap
#| tbl-subcap

# %%
#| echo: false
radius = 10
from IPython.display import Markdown
from markupspace import escape

Markdown(escape(f"The _radius_ of the circle is **{radius}**."))

# Note that dynamically generated markdown will still be enclosed in the standard Quarto output divs. If you want to remove all of Quarto's default output enclosures use the output: asis option. For example:

# %%
#| echo: false
#| output: asis
radius = 10
from IPython.display import Markdown
from markupspace import escape

Markdown(escape(f"The _radius_ of the circle is **{radius}**."))

# %% [markdown]
"""
For hidden markdown:

::: {.content-hidden}
This will not be displayed, completely ignored
:::
"""

# %%
# ```qmd
# Shortcuts:
# {{< meta title >}}
# {{< placeholder 400 200 format=svg >}}
# {{< lipsum 2 >}}
# ```

# %%
# ```qmd
# ::: {.callout-note}
# Note that there are five types of callouts, including:
# `note`, `warning`, `important`, `tip`, and `caution`.
# :::
#
# ::: {.callout-tip}
# ## Tip with Title
#
# This is an example of a callout with a title.
# :::
#
# ::: {.callout-caution collapse="true"}
# ## Expand To Learn About Collapse
#
# This is an example of a 'folded' caution callout that can be expanded by the user. You can use `collapse="true"` to collapse it by default or `collapse="false"` to make a collapsible callout that is expanded by default.
# :::
# ```
