import os
import pandas as pd
import psycopg2
from tqdm import tqdm

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')
postgres_db = os.getenv('POSTGRES_DB')
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
data_dir = os.getenv('DATA_DIR')
# staging_dir = os.getenv('STAGING_DIR')

# Determine the path to the staging directory relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, '..', 'data', 'company_data')  # Update path to company_data

try:
    # Read data from Parquet files
    parquet_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.parquet')]
    dfs = [pd.read_parquet(file) for file in parquet_files]
    companies_df = pd.concat(dfs)

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=postgres_host,
        port=postgres_port,
        database=postgres_db,
        user=postgres_user,
        password=postgres_password
    )
    cursor = conn.cursor()

    # Define the table name
    table_name = 'companies'

    # Create the table if it doesn't exist
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id UUID PRIMARY KEY,
            company VARCHAR,
            name VARCHAR,
            address VARCHAR,
            transaction_amount DECIMAL,
            transaction_date DATE,
            customer_preference VARCHAR,
            communication_method VARCHAR
        );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Ingest data into the table
    for _, row in tqdm(companies_df.iterrows(), total=companies_df.shape[0], desc="Ingesting data"):
        insert_query = f"""
            INSERT INTO {table_name} (id, company, name, address, transaction_amount, transaction_date, customer_preference, communication_method)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (
            row['id'],
            row['company'],
            row['name'],
            row['address'],
            float(row['transaction_amount']),  # Convert Decimal to float
            row['transaction_date'],
            row['customer_preference'],
            row['communication_method']
        ))
        conn.commit()

    print("Data successfully ingested into PostgreSQL.")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
