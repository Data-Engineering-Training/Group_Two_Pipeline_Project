import os
import pyarrow as pa
import pyarrow.parquet as pq
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Define the companies
companies = [
    "KGL Technology Limited",
    "Melcom Limited",
    "Zeepay Ghana Limited",
    "Ghana Oil Palm Development Ltd",
    "Sage Distribution Limited",
    "Total Energies Marketing Ghana Plc",
    "Enterprise Trustees",
    "IT Consortium Ltd",
    "Sunon Asogli Power Ghana Limited Company",
    "Ecobank"
]

# Define the fields to generate
fields = [
    "company",
    "name",
    "address",
    "transaction_amount",
    "transaction_date",
    "customer_preference",
    "communication_method"
]

# Create the directory for company data if it doesn't exist
data_dir = 'data/company_data'
os.makedirs(data_dir, exist_ok=True)

# Generate and write data for each company
for company in companies:
    records = []
    for _ in range(100000):
        record = {
            "company": company,
            "name": fake.name(),
            "address": fake.address(),
            "transaction_amount": fake.pydecimal(left_digits=4, right_digits=2, positive=True),
            "transaction_date": fake.date_between(start_date="-1y", end_date="today"),
            "customer_preference": fake.random_element(elements=("app", "website")),
            "communication_method": fake.random_element(elements=("email", "phone"))
        }
        records.append(record)

    # Create a dictionary with field names as keys and lists of values
    data_dict = {field: [record[field] for record in records] for field in fields}

    # Create a PyArrow table from the dictionary
    table = pa.Table.from_pydict(data_dict)

    # Write the table to a Parquet file
    filename = f"{company.replace(' ', '_')}.parquet"
    filepath = os.path.join(data_dir, filename)
    pq.write_table(table, filepath)
