# {{cookiecutter.project_name}}

{{cookiecutter.description}}

<!--
Table of contents updated via:
uvx --from md-toc md_toc --in-place github -- README.md
-->
<!--TOC-->

-   [{{cookiecutter.project_name}}](#cookiecutterproject_name)
    -   [Project Organization](#project-organization)

<!--TOC-->

## Project Organization

```shell
├── LICENSE            <- Open-source license if one is chosen.
├── pyproject.toml     <- Project configuration file with configuration for tools like ruff.
│── README.md          <- The top-level README for developers using this project.
│
├── bin                <- Useful scripts.
│
├── data               <- Shared data directory. By default, not kept in version control.
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details.
│
└── projects
    │
    ├── ds-utils       <- Shared source code for use in these projects.
    │   ├─ pyproject.toml
    │   │
    │   ├── ds_utils
    │   │
    │   └── tests
    │
    └── project-1
        ├── pyproject.toml
        ├── README.md
        │
        ├── data             <- Project specific data directory. By default, not kept in version control.
        │   │
        │   ├── external     <- Data from third party sources.
        │   │
        │   ├── interim      <- Intermediate data that has been transformed.
        │   │
        │   ├── processed    <- The final, canonical data sets for modeling.
        │   │
        │   └── raw          <- The original, immutable data dump.
        │
        ├── models           <- Project specific models directory for trained and serialized models. By default, not kept in version control.
        │
        ├── notebooks        <- Project specific notebooks directory.
        │   └── 1.0-ftod-example.py  <- Jupyter notebooks in percent format.
        │
        ├── references       <- Data dictionaries, manuals, and all other explanatory materials.
        │
        ├── reports          <- Generated analysis as HTML, PDF, LaTeX, etc.
        │   │
        │   └── figures      <- Generated graphics and figures to be used in reporting.
        │
        ├── tests
        │
        └── project_1        <- Project-specific source code.
            ├── __init__.py
            ├── config.py    <- Store useful variables and configuration.
            ├── dataset.py   <- Scripts to download or generate data.
            ├── features.py  <- Code to create features for modeling.
            ├── plots.py     <- Code to create visualizations.
            │
            └── modeling
                ├── __init__.py
                ├── predict.py  <- Code to run model inference with trained models.
                └── train.py    <- Code to train models.│


```

The naming convention for notebooks is a number (for ordering),
the creator's initials, and a short `-` delimited description.

## Useful commands

```shell
cd your-new-project-directory

# Install pre-commit hooks.
pre-commit install --install-hooks

# Install Jupyter kernel for all projects.
./bin/install-kernel

# Start Jupyter Lab.
uv run jupyter lab &

# Run tests of code.
./bin/run-tests
```
