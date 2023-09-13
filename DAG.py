# Define default_args dictionary
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Initializing the DAG
dag = DAG(
    'data_warehouse_etl',
    default_args=default_args,
    description='ETL tasks for Data Warehouse',
    schedule_interval=timedelta(days=1),  # or use any cron-like expression
    start_date=datetime(2023, 1, 1),
    catchup=False
)

# Task 1: Extracting  CSV data and loading it into staging tables
extract_task = PythonOperator(
    task_id='extract_csv',
    python_callable=your_module.extract_csv,  # Refer to the module
    provide_context=True,
    dag=dag,
    doc_md="""## Extract Task
    This task extracts data from source CSV files and loads them into staging tables."""
)

# Task 2: Transforming data into dimension and fact tables
transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=your_module.transform_data,
    provide_context=True,
    dag=dag,
    doc_md="""## Transform Task
    This task transforms data from staging tables to dimension and fact tables."""
)

# Task 3: Cleaning up staging table(s)
cleanup_task = PythonOperator(
    task_id='cleanup_staging',
    python_callable=your_module.cleanup_staging,
    provide_context=True,
    dag=dag,
    retries=3,
    retry_delay=timedelta(minutes=10),
    doc_md="""## Cleanup Task
    This task cleans up the staging tables."""
)

# Task 4: performing data quality checks
data_quality_task = PythonOperator(
    task_id='data_quality_check',
    python_callable=your_module.data_quality_check,
    provide_context=True,
    dag=dag,
    doc_md="""## Data Quality Check Task
    This task performs data quality checks on the dimension and fact tables."""
)

# Set task dependencies
extract_task >> transform_task >> cleanup_task >> data_quality_task
