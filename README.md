Testing airflow
docker compose up airflow-init
docker-compose up
http://localhost:8080/login/
airflow tasks test <dag_id> <task_id> <past_date>

Example:
airflow tasks test example_python_operator compute_dates 2022-05-03

airflow tasks test my_dag my_task