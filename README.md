# My Data Science Cookiecutter

A customized, logical, reasonably standardized
but flexible project structure for doing and sharing data science work.

Based on [Cookiecutter Data Science (CCDS)](https://cookiecutter-data-science.drivendata.org/).

## Installation

```bash
uv tool install cookiecutter-data-science
```

## Starting a new project

To start a new project, run:

```bash
ccds https://github.com/proinsias/cookiecutter-data-science-proinsias
```

### The resulting directory structure

FIXME: POINT TO OTHER README.MD

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
