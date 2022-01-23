from datetime import timedelta
from airflow import DAG

from datetime import datetime, timedelta

default_args = {
    "owner":"airflow",
    "retries":3,
    "retry_delay":timedelta(minutes=5)
}

with DAG("data_pipeline", start_date=datetime(2022,1,1),schedule_interval="@daily",default_args=default_args,catchup=False) as dag:
    
