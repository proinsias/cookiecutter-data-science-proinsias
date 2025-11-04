# Data Science Project

# {{cookiecutter.project_name}}

{{cookiecutter.description}}

<!--
Table of contents updated via:
uvx --from md-toc md_toc --in-place github -- README.md
-->
<!--TOC-->

- [Data Science Project](#data-science-project)
- [{{cookiecutter.project_name}}](#cookiecutterproject_name)
  - [Project Organization](#project-organization)

<!--TOC-->

## Project Organization

```shell
├── LICENSE            <- Open-source license if one is chosen.
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`.
├── pyproject.toml     <- Project configuration file with configuration for tools like ruff.
│── README.md          <- The top-level README for developers using this project.
│
├── bin                <- Useful scripts.
│
├── data               <- Shared data directory.
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
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
        ├── pyproject.toml (ds-playground/projects/gilbert-shannon-reeds/pyproject.toml)
        ├── README.md (mermaid from ds-playground/projectsdisease-risk-prediction/README.md)
        │
        ├── data               <- Project specific data directory.
        │   │
        │   ├── external       <- Data from third party sources.
        │   │
        │   ├── interim        <- Intermediate data that has been transformed.
        │   │
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   │
        │   └── raw            <- The original, immutable data dump.
        │
        ├── models               <- Project specific models directory for Trained and serialized  models.  (cookiecutter-data-science-proinsias)
        │
        ├── notebooks               <- Project specific notebooks directory. (cookiecutter-data-science-proinsias)
        │   └── 1.0-jqp-initial-data-exploration.py  <- Jupyter notebooks in percent? format. Naming  convention is a number (for ordering),
        │       the creator's initials, and a short `-` delimited description.
        │
        ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
        │
        ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
        │   └── figures        <- Generated graphics and figures to be used in reporting
        │
        ├── tests
        │
        └── project_1 (Project specific source code. ds-playground/projects/disease-risk-prediction/ disease_risk_prediction)
            │
            ├── __init__.py
            │
            ├── config.py               <- Store useful variables and configuration  cookiecutter-data-science-proinsias)
            │
            ├── dataset.py              <- Scripts to download or generate data  cookiecutter-data-science-proinsias)
            │
            ├── features.py             <- Code to create features for modeling cookiecutter-data-science-proinsias)
            │
            ├── modeling                
            │   ├── __init__.py 
            │   ├── predict.py          <- Code to run model inference with trained models       (cookiecutter-data-science-proinsias)    
            │   └── train.py            <- Code to train models (cookiecutter-data-science-proinsias)
            │
            │
            └── plots.py                <- Code to create visualizations   (cookiecutter-data-science-proinsias)

```
