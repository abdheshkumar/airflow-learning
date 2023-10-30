from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2023, 10, 26)
}
dag = DAG('my_dag',
          default_args=default_args,
          schedule_interval=None)

# Get the latest date for which we should have data
job_run_date = '{{ ds }}'


def my_python_function():
    # Your Python code here
    print("Working.....")
    print(job_run_date)
    print("Done.....")


my_task = PythonOperator(
    task_id='my_task',
    python_callable=my_python_function,
    provide_context=True,
    dag=dag
)

print(job_run_date)

my_task
