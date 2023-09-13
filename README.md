## Data-engineering-test

# Overview

Each task of extracting, transforming, cleanup, and data quality has a corresponding Python function that performs the required actions. From a Python perspective, I use OOP in the office but not sure as we don’t have the logical requirements. The Airflow DAG orchestrates these tasks, ensuring that they run in the specified order. We can further customize and expand the ETL process and add error handling as needed. The SQL statements and Python functions can also be customized to match specific requirements, use cases, and database systems.

To parse the given CSV data, design dimensions, and fact tables, and use Apache Airflow for workflow management, we'll break down the process into multiple steps. Here's a high-level overview of the steps and the structure of the Python code, SQL scripts, and Airflow DAG :

# Step 1: Creating Database Schema

Create a database schema in MySQL or SQL Server where you will store the data warehouse tables.

# Step 2: Defining Dimension Tables

Define dimension tables for the following entities:

- Customer
- Campaign
- Ad Group
- Ad
- Device
- Language
- Network
- Currency
- Date

# Step 3: Defineing Fact Table

Define a fact table to store the metrics (Impressions, Clicks, Spend, etc.) with foreign keys to the dimension tables.

# Step 4: Creating Airflow DAG

Create an Airflow DAG to automate the ETL process. The DAG should consist of the following tasks:

- Task 1: Extract CSV data and load it into staging table(s).
- Task 2: Transform data from staging table(s) into dimension and fact tables.
- Task 3: Clean up staging table(s).
- Task 4: Optionally, perform data quality checks.
- Task 5: Optionally, schedule the DAG to run periodically.

