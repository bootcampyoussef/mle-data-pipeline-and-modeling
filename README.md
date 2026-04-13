# Data Pipeline and Data Modeling

This repository is a small hands-on course in three steps:

1. [Setup the database](./01-setup-your-db.md)
2. [ETL pipeline](./02-load-data.ipynb)
3. [Data modeling](./03-data-modeling.ipynb)

By the end, you will have:

- a local PostgreSQL database running in Docker
- the January 2025 NYC Yellow Taxi dataset loaded into PostgreSQL
- a simple star schema built on top of the raw table
- practice writing analytical SQL against both the raw and modeled data

## Course Map

### Step 1: Setup the database

In [01-setup-your-db.md](./01-setup-your-db.md), you will start PostgreSQL in Docker and verify that you can connect to it.

You are done with step 1 when:

- the `ny-taxi-db` container is running
- PostgreSQL is reachable on `localhost:5432`
- you can connect to the `ny_taxi` database with `psql`

### Step 2: Build the ETL pipeline

In [02-load-data.ipynb](./02-load-data.ipynb), you will download the yellow taxi parquet file, inspect it with pandas, and load it into PostgreSQL in chunks.

You are done with step 2 when:

- the `yellow_taxi` table exists in `ny_taxi`
- the notebook validation confirms the PostgreSQL row count matches the parquet row count
- the CLI and Dockerized ingestion flow both make sense from the notebook walkthrough

### Step 3: Model the data for analytics

In [03-data-modeling.ipynb](./03-data-modeling.ipynb), you will turn the raw `yellow_taxi` table into a small star schema for analytical queries.

You are done with step 3 when:

- the dimension tables and `fact_trip` exist in PostgreSQL
- `fact_trip` has the same number of rows as `yellow_taxi`
- you can answer the notebook exercises with the modeled tables

## Mermaid Diagrams

This repository contains Mermaid diagrams. If you want them to render in VS Code, we recommend installing the `Markdown Preview Mermaid Support` extension:

- [Install in VS Code](vscode:extension/bierner.markdown-mermaid)
- [View on Marketplace](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

## Environment

Please make sure you **use this repository as a template** and set up a new virtual environment. You can use the following commands:

### **`macOS`**

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### **`Windows`**

For `PowerShell` CLI:

```PowerShell
pyenv local 3.11.3
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For `Git-Bash` CLI:

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The [requirements.txt](requirements.txt) file contains all libraries and dependencies needed to execute the notebooks.

## Setup

- You will need **Docker Desktop** installed and running on your machine. If you do not have it installed, please follow the [installation instructions](https://docs.docker.com/get-docker/).

- **DBeaver** is optional, but recommended if you want a GUI for exploring the database. If you do not have it installed, please follow the [installation instructions](https://dbeaver.io/download/), or use:

### **`macOS`**

```bash
brew install --cask dbeaver-community
```

### **`Windows`**

```PowerShell
choco install dbeaver
```

## Learning Objectives

By the end of this repository, you should be able to:

- Start and verify a local PostgreSQL database with Docker.
- Load parquet data into PostgreSQL with a small Python ETL pipeline.
- Validate raw data loads with SQL and pandas.
- Explain the difference between normalized and dimensional data models.
- Build and query a simple star schema for analytics.
