
--Step 1: Creating Database Schema


--Create the database schema if it doesn't exist

CREATE DATABASE IF NOT EXISTS radancy_dw;

--  Step 2: Define Dimension Tables

-- SQL CREATE statements for dimension tables
--  for Customer dimension table:
CREATE TABLE customer (
     customer_id INT PRIMARY KEY,
     customer_name VARCHAR(255),
     account_number VARCHAR(255),
     account_name VARCHAR(255),
     account_status VARCHAR(50)
     -- Add other columns as needed
 );

-- We can define similar tables for Campaign, Ad Group, Ad, Device, Language, Network, Currency, and Date dimensions.

-- Step 3: Define Fact Table

-- SQL CREATE statement for the fact table
CREATE TABLE fact (
     fact_id INT PRIMARY KEY,
     date_id INT,
     customer_id INT,
     campaign_id INT,
     ad_group_id INT,
     ad_id INT,
     device_id INT,
     language_id INT,
     network_id INT,
     currency_id INT,
     impressions INT,
     clicks INT,
     spend DECIMAL(10, 2),
     avg_position DECIMAL(4, 2),
     conversions INT,
     assists INT
     -- We can add other columns as needed
);

-- We can  further define foreign keys to link the fact table to dimension tables.




