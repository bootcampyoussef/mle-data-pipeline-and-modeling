To start with your task setup your postgres database with docker.

## Step 1: Build the image

```bash
docker build -t postgres .
```
## Step 2: Create a network

```bash
docker network create ny-taxi
```

## Step 3: Run the container

```bash
docker run -d -e POSTGRES_USER='postgres' \
    --network=ny-taxi \
    -e POSTGRES_PASSWORD='postgres' \
    -e POSTGRES_DB='ny_taxi' \
    -v $(pwd)/db-data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --name ny-taxi-db \
    postgres
```

## Step 4: Connect to the database

```bash
docker exec -it ny-taxi-db psql -U postgres 
```
With `\l` you can list all databases and `\c ny_taxi` to connect to the database.



