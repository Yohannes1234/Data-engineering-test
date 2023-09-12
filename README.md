## data-engineering-test

# Overview

In this code structure, each task (e.g., extract, transform, cleanup, data quality) has a corresponding Python function that performs the required actions. The Airflow DAG orchestrates these tasks, ensuring that they run in the specified order. We can further customize and expand the ETL process and add error handling as needed.The SQL statements and Python functions can also be customized to match specific requirements, use cases and database system.

To parse the given CSV data, design dimensions and fact tables, and use Apache Airflow for workflow management, we'll break down the process into multiple steps. Here's a high-level overview of the steps and the structure of the Python code, SQL scripts, and Airflow DAG :

# Step 1: Create Database Schema

1. Create a database schema in MySQL or SQL Server where you will store the data warehouse tables.

# Step 2: Define Dimension Tables
2. Define dimension tables for the following entities:

- Customer
- Campaign
- Ad Group
- Ad
- Device
- Language
- Network
- Currency
- Date

# Step 3: Define Fact Table

3. Define a fact table to store the metrics (Impressions, Clicks, Spend, etc.) with foreign keys to the dimension tables.

# Step 4: Create Airflow DAG

4. Create an Airflow DAG to automate the ETL process. The DAG should consist of the following tasks:

Task 1: Extract CSV data and load it into staging table(s).
Task 2: Transform data from staging table(s) into dimension and fact tables.
Task 3: Clean up staging table(s).
Task 4: Optionally, perform data quality checks.
Task 5: Optionally, schedule the DAG to run periodically.
Now, let's look at a more detailed Python code example for each of these steps.

