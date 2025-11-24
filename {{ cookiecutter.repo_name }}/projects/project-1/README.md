# Project 1

<!--
Table of contents updated via:
uvx --from md-toc md_toc --in-place github -- README.md
-->
<!--TOC-->

-   [Project 1](#project-1)
    -   [Project Structure](#project-structure)

<!--TOC-->

## Project Structure

```mermaid
flowchart TD

    %% Subprocess as a "nested" flowchart
    subgraph SubGraph1 ["Global feature pipeline"]
        V --> EC[Encode categorical <br/> Scale & deskew numeric]
        EC --> NV[Drop features with <br/> no variance]
        NV --> MC[Drop features to <br/> reduce multicollinearity]
    end

    %% Subprocess as a "nested" flowchart
    subgraph SubGraph2 ["Global target pipeline"]
        VV --> BT[Binarize targets]
    end

    %% Subprocess as a "nested" flowchart
    subgraph SubGraph3 ["Target-specific pipeline"]
        BT --> LS[Drop features with <br/> low signal with target]
        LS --> UO[Under-/over-sample targets]
    end

    %% Main flow
    FD[Fetch data] --> V[Validate features]
    FD --> VV[Validate targets]
    MC --> LS
    UO --> T[Training]
    T --> DC[Dummy Classifier]
    DC --> DCR(Metrics report)
    T --> X[Optimized XGBoost]
    X --> XR(Metrics report)
    X --> XLC(Learning curve)
    T --> KR[Optimized Keras]
    KR --> KRR(Metrics report)
    KR --> KRLC(Learning curve)
```

## Installation

```bash
brew install quarto
```

Or look at [Getting Started with Quarto](https://quarto.org/docs/get-started/).

## Useful commands

```bash
quarto preview hello.qmd

quarto convert document.qmd

quarto render hello.qmd --to html
quarto render hello.qmd --to docx
quarto render hello.qmd --to pdf

# Default is to not execute cells within notebook. Override using:
quarto render notebook.ipynb --execute
```
