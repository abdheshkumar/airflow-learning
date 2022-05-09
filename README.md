Testing airflow

airflow tasks test <dag_id> <task_id> <past_date>

Example:
airflow tasks test example_python_operator compute_dates 2022-05-03