from __future__ import print_function

import time
from builtins import range
from pprint import pprint

from airflow.utils.dates import days_ago
from datetime import timedelta, datetime
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
import logging

args = {
    'owner': 'Airflow',
    'start_date': datetime(2022, 5, 4)
}

dag = DAG(
    dag_id='example_python_operator',
    default_args=args,
    schedule_interval=None,
    tags=['example']
)


def compute_dates(ti, ts_nodash):
    #ti = kwargs['ti']
    launch_dt = datetime.strptime(ts_nodash, '%Y%m%dT%H%M%S')
    datettime_with_offset = launch_dt - timedelta(hours = 10)
    event_date = datettime_with_offset.date().isoformat()
    event_hour = datettime_with_offset.hour
    trip_start_date = (datettime_with_offset + timedelta(days=1)).date().isoformat()
    trip_end_date= (datettime_with_offset + timedelta(days=30)).date().isoformat()
    
    ti.xcom_push(key='event_date', value=event_date)
    ti.xcom_push(key='event_hour', value=event_hour)
    ti.xcom_push(key='trip_start_date', value=trip_start_date)
    ti.xcom_push(key='trip_end_date', value=trip_end_date)


run_this = PythonOperator(
    task_id='compute_dates',
    #provide_context=True,
    python_callable=compute_dates,
    dag=dag,
)

def simulate_dataoperator(**kwargs):
    pprint(kwargs)

event_date = '{{ ti.xcom_pull(key="event_date", task_ids="compute_dates") }}'
event_hour = '{{ ti.xcom_pull(key="event_hour", task_ids="compute_dates") }}'    
trip_start_date = '{{ ti.xcom_pull(key="trip_start_date", task_ids="compute_dates") }}'    
trip_end_date = '{{ ti.xcom_pull(key="trip_end_date", task_ids="compute_dates") }}'    

run_that = PythonOperator(
    task_id='simulate_dataoperator',
    provide_context=True,
    python_callable=simulate_dataoperator,
    op_kwargs={'query':  'query {0},{1},{2},{3}'.format(event_date, event_hour, trip_start_date, trip_end_date)},
    dag=dag,
)

run_this >> run_that

# [END howto_operator_python_kwargs]