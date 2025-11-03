```
# child repo structure
├── .gitignore             <- ignore ipynb - create from template and list templates!
├── AUTHORS
├── README.md
├── LICENSE            <- Open-source license if one is chosen
├── pyproject.toml (config for linters - ds-playground) 
├── bin
│   ├── install-kernels (ds-playground)
├── data               <- Shared data directory
│   ├── external       <- Data from third party sources. (cookiecutter-data-science-proinsias)
│   ├── interim        <- Intermediate data that has been transformed. (cookiecutter-data-science-proinsias)
│   ├── processed      <- The final, canonical data sets for modeling. (cookiecutter-data-science-proinsias)
│   └── raw            <- The original, immutable data dump. (cookiecutter-data-science-proinsias)
├── references         <- Data dictionaries, manuals, and all other explanatory materials. (cookiecutter-data-science-proinsias)
│
├── projects
│   ├── ds-utils        <- Shared source code for use in these projects.
│   │   ├── ds_utils
│       ├── pyproject.toml         (ds-playground/projects/ds-utils/pyproject.toml)
│   ├── project-1
│   │   ├── data               <- Project specific data directory.
│   │   │   ├── external       <- Data from third party sources.
│   │   │   ├── interim        <- Intermediate data that has been transformed.
│   │   │   ├── processed      <- The final, canonical data sets for modeling.
│   │   │   └── raw            <- The original, immutable data dump.
│   │   ├── models               <- Project specific models directory for Trained and serialized models.  (cookiecutter-data-science-proinsias)
│   │   ├── notebooks               <- Project specific notebooks directory. (cookiecutter-data-science-proinsias)
│   │   │   ├── 1.0-jqp-initial-data-exploration.py  <- Jupyter notebooks in percent? format. Naming convention is a number (for ordering),
│   │   │       the creator's initials, and a short `-` delimited description.
│   │   ├── pyproject.toml (ds-playground/projects/gilbert-shannon-reeds/pyproject.toml)
│   │   ├── README.md (mermaid from ds-playground/projectsdisease-risk-prediction/README.md)
│   │   ├── tests
│   │   ├── project_1 (Project specific source code. ds-playground/projects/disease-risk-prediction/disease_risk_prediction)
│   │   │   │
│   │   │   ├── __init__.py
│   │   │   │
│   │   │   ├── config.py               <- Store useful variables and configuration (cookiecutter-data-science-proinsias)
│   │   │   │
│   │   │   ├── dataset.py              <- Scripts to download or generate data (cookiecutter-data-science-proinsias)
│   │   │   │
│   │   │   ├── features.py             <- Code to create features for modeling (cookiecutter-data-science-proinsias)
│   │   │   │
│   │   │   ├── modeling                
│   │   │   │   ├── __init__.py 
│   │   │   │   ├── predict.py          <- Code to run model inference with trained models       (cookiecutter-data-science-proinsias)    
│   │   │   │   └── train.py            <- Code to train models (cookiecutter-data-science-proinsias)
│   │   │   │
│   │   │   │
│   │   │   └── plots.py                <- Code to create visualizations   (cookiecutter-data-science-proinsias)
├── Makefile           <- Makefile with convenience commands like `make data` or `make train` (cookiecutter-data-science-proinsias)
├── docs               <- A default mkdocs project; see www.mkdocs.org for details (cookiecutter-data-science-proinsias)
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc. (cookiecutter-data-science-proinsias)
│   └── figures        <- Generated graphics and figures to be used in reporting (cookiecutter-data-science-proinsias)
│
```

ADD IN MAIN MODULE - AS PER BACKEND CODE! AND INCLUDE REFERENCE TO THIS IN PROJECT. 



https://github.com/proinsias/cookiecutter-data-science-proinsias

add quarto support and example pipeline.

markdown linter?
