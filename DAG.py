from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime


# Initializing the DAG
dag = DAG(
    'data_warehouse_etl',
    schedule_interval=None,  # we can set the schedule as needed
    start_date=datetime(2023, 1, 1),  # defining the start date
    catchup=False  # this disables catching up missed runs
)

# Task 1: Extracting  CSV data and loading into staging tables
extract_task = PythonOperator(
    task_id='extract_csv',
    python_callable=extract_csv,
    provide_context=True,  # we are allowing passing context (like execution date)
    dag=dag
)

# Task 2: Transforming data into dimension and fact tables
transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    provide_context=True,
    dag=dag
)

# Task 3: Cleaning up staging table(s)
cleanup_task = PythonOperator(
    task_id='cleanup_staging',
    python_callable=cleanup_staging,
    provide_context=True,
    dag=dag
)

# Task 4: performing data quality checks
data_quality_task = PythonOperator(
    task_id='data_quality_check',
    python_callable=data_quality_check,
    provide_context=True,
    dag=dag
)

# Set task dependencies
extract_task >> transform_task >> cleanup_task >> data_quality_task

# Optionally, Task 5: Schedule the DAG to run periodically
