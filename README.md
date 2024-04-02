## Customer Data Generation and Analysis Pipeline
## Project Overview

This project outlines a data pipeline for generating and analyzing customer data for 10 fictitious companies. The pipeline leverages the Faker library to create realistic customer data and explores various functionalities through SQL queries.

## Pipeline Stages

Data Generation (Python):

Utilize Faker library to generate 100,000 customer records for each of the 10 companies.
Include demographics (name, address), transaction activity, customer preferences (app, website), and communication methods (email).
Data Ingestion (Python):

Establish connection to a relational database (e.g., PostgreSQL, MySQL).
Define database schema to accommodate the generated customer data.
Ingest the generated data into the database tables.
Data Analysis (SQL):

Develop a set of 10 SQL queries to answer various business-related questions about the customer data.
Examples might include:
Identify customers with the highest spending history.
Find the most popular communication channels.
Analyze customer preferences between app and website usage.
Query Storage (Text File):

Store the developed SQL queries in a separate text file for reference and future use.
Data Pipeline Diagram (Image):

Create a visual representation of the data pipeline workflow, illustrating the flow of data from generation to analysis.
Technologies Used

Python (programming language)
Faker (data generation library)
Relational Database (PostgreSQL or MySQL)
SQL (Structured Query Language)
Benefits

Simulates real-world customer data for analysis and exploration.
Provides a practical example of data pipeline construction.
Demonstrates the power of SQL in extracting insights from customer data.
Getting Started

Install required libraries: pip install faker
Choose a relational database and set up a connection.
Refer to the provided code and documentation for further details on each stage.
Future Enhancements

Integrate data visualization tools to present analytical results.
Expand the range of queries to answer more complex business questions.
Implement data quality checks for data validation purposes.

# More Info

This repository contains scripts for generating synthetic company data, writing it to Parquet files, and ingesting it into a PostgreSQL database. Below is a guide on how to use these scripts effectively.

## Installation

Before running the scripts, make sure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Generating Company Data
```bash
generate_data.py
```
Is used to generate synthetic data.

## Ingestion of Data
```bash
data_ingestion_pipeline.py
```
Is used to create a database in the postgres docker container and ingest the synthetically generated data into it

## Dependencies

    pyarrow==5.0.0
    pandas==1.3.3
    psycopg2==2.9.1
    tqdm==4.62.3
    Faker==9.10.2

## Note

    The generated data is purely synthetic. NO COMPANY'S DATA was used in this project.
    Ensure proper configuration of environment variables and database connection details before running the ingestion program.