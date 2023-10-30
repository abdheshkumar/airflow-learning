Testing airflow
```shell
docker compose up airflow-init
```
```shell
docker-compose up
```
http://localhost:8080/login/
```shell
airflow tasks test <dag_id> <task_id> <past_date>
```

Example:
```shell
airflow tasks test example_python_operator compute_dates 2022-05-03

airflow tasks test my_dag my_task
```