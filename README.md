# Data pipeline and Data modeling

In this repository you will build a simple ETL pipeline using Python and SQL. The pipeline will download data, extract data from files, process them using Python, and load the data into a Database. Also you will explore the dataset with SQL in your created Database.
Afterwards you will learn about Data modeling and how to create a star schema for your data. You will also learn how to create a star schema using Python.


1. [Setup the Database](./01-setup-your-db.md)
2. [ETL pipeline](./02-load-data.ipynb)
3. [Data modeling](./03-data-modeling.ipynb)

## Setup

### Requirements

You will need Docker and Docker Compose installed on your machine. If you don't have them installed, please follow the instructions on the official website: [https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/)

Also you will need DBeaver installed on your machine. If you don't have it installed, please follow the instructions on the official website: [https://dbeaver.io/download/](https://dbeaver.io/download/) or you can use:

```bash
brew install --cask dbeaver-community
```

### Environment 

```bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements-dev.txt
```