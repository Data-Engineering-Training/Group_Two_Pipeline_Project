import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook
import pyarrow.parquet as pq
import pandas as pd

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Access environment variables
postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')
postgres_db = os.getenv('POSTGRES_DB')
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
data_dir = os.getenv('DATA_DIR')
staging_dir = os.getenv('STAGING_DIR')

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Function to read and store data
def read_and_store_data():
    parquet_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.parquet')]
    staged_data = []
    for parquet_file in parquet_files:
        df = pq.read_table(parquet_file).to_pandas()
        staged_data.append(df)
    staged_data_df = pd.concat(staged_data)
    staged_data_df.to_parquet(os.path.join(staging_dir, 'staged_data.parquet'))

# Function to ingest data into PostgreSQL
def ingest_data_to_postgres():
    # Connect to PostgreSQL
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    connection = pg_hook.get_conn()
    cursor = connection.cursor()

    # Read data from staging area
    staged_data_df = pq.read_table(os.path.join(staging_dir, 'staged_data.parquet')).to_pandas()

    # Ingest data into PostgreSQL
    staged_data_df.to_sql('transactions', connection, if_exists='replace', index=False)

    # Commit and close connection
    connection.commit()
    cursor.close()
    connection.close()

# Define the DAG
with DAG('data_pipeline',
         default_args=default_args,
         schedule_interval=None,  # Set your desired schedule interval
         catchup=False) as dag:

    # Task to read and store data
    read_and_store_task = PythonOperator(
        task_id='read_and_store_data',
        python_callable=read_and_store_data,
    )

    # Task to ingest data into PostgreSQL
    ingest_to_postgres_task = PythonOperator(
        task_id='ingest_data_to_postgres',
        python_callable=ingest_data_to_postgres,
    )

    # Set task dependencies
    read_and_store_task >> ingest_to_postgres_task
