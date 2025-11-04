# My Data Science Cookiecutter

A customized, logical, reasonably standardized
but flexible project structure for doing and sharing data science work.

Based on [Cookiecutter Data Science (CCDS)](https://cookiecutter-data-science.drivendata.org/).

<!--
Table of contents updated via:
uvx --from md-toc md_toc --in-place github -- README.md
-->
<!--TOC-->

<!--TOC-->

## Installation

```bash
uv tool install cookiecutter-data-science
```

## Starting a new project

To start a new project, run:

```bash
ccds https://github.com/proinsias/cookiecutter-data-science-proinsias
```

### Additional tools

```shell
cd your-new-project-directory

# Install pre-commit hooks.
pre-commit install --install-hooks

# Install Jupyter kernel for the project
./bin/install-kernel

# Start Jupyter Lab.
uv run jupyter lab
```
