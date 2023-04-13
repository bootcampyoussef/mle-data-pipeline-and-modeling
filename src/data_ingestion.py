import click
import pandas as pd
import pyarrow.parquet as pq
from time import time
from sqlalchemy import create_engine
import os

@click.command()
@click.option('--user', default='postgres', help='Postgres user name')
@click.option('--password', default='postgres', help='Postgres password')
@click.option('--host', default='localhost', help='Postgres host name')
@click.option('--port', default=5432, help='Postgres port number')
@click.option('--table_name', default='yellow_taxi', help='Table name to write to')
@click.option('--url', help='URL to download parquet file from')
@click.option('--file_path', help='Path to save parquet file to')
@click.option('--db', default='ny_taxi', help='Database name to write to')
def data_ingestion(table_name, url, file_path, user, password, host, port, db):
    """This script reads a parquet file from a given url and writes it to a postgres database.
    """
    
    os.system(f'wget {url} -O {file_path}')
    
    # Write your code here
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df_taxi = pd.read_parquet(f'{file_path}')
    df_taxi.head(n=0).to_sql(name='yellow_taxi', con=engine, if_exists='replace')
    
    parquet_file = pq.ParquetFile(f'{file_path}')
    for batch in parquet_file.iter_batches(batch_size=100000):
        start_time = time()
        batch_df = batch.to_pandas()
        batch_df.to_sql(f'{table_name}', engine, if_exists='append', index=False)
        end_time = time()
        print('Batch time: ', end_time - start_time)
    else:
        print('Finished writing to database!')
    
if __name__ == '__main__':
    data_ingestion()