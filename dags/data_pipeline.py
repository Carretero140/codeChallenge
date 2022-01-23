from datetime import timedelta
from airflow import DAG
from airflow.sensors.filesystem import FileSensor

from datetime import datetime, timedelta

default_args = {
    "owner":"airflow",
    "retries":3,
    "retry_delay":timedelta(minutes=5)
}

with DAG("data_pipeline", start_date=datetime(2022,1,1),schedule_interval="@daily",default_args=default_args,catchup=False) as dag:

    is_trips_file_available = FileSensor(
        task_id="is_trips_file_available",
        fs_conn_id="file_path",
        filepath="trips.csv",
        poke_interval=5,
        timeout=20
    )

