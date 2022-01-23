from datetime import timedelta
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

from datetime import datetime, timedelta
import pandas as pd

default_args = {
    "owner":"airflow",
    "retries":3,
    "retry_delay":timedelta(minutes=5)
}

def _download_trips():
    for chunk in pd.read_csv('/opt/airflow/dags/files/trips.csv',chunksize=10):
        chunk['origin_coord'] = chunk['origin_coord'].map(lambda x: x.strip('POINT ()')).str.split(' ')
        chunk['origin1'] = chunk['origin_coord'].str[0]
        chunk['origin2'] = chunk['origin_coord'].str[1]
        chunk['destination_coord'] = chunk['destination_coord'].map(lambda x: x.strip('POINT ()')).str.split(' ')
        chunk['destination1'] = chunk['destination_coord'].str[0]
        chunk['destination2'] = chunk['destination_coord'].str[1]
        columns = ['region','origin1','origin2','destination1','destination2','datetime','datasource']
        header = False
        chunk.to_csv('trips_processed.csv',columns=columns,header=header, mode='a',index = False)
        

with DAG("data_pipeline", start_date=datetime(2022,1,1),schedule_interval="@daily",default_args=default_args,catchup=False) as dag:

    is_trips_file_available = FileSensor(
        task_id="is_trips_file_available",
        fs_conn_id="file_path",
        filepath="trips.csv",
        poke_interval=5,
        timeout=20
    )

    processing_trips = PythonOperator(
        task_id='processing_trips',
        python_callable=_download_trips
    )

    creating_table = SqliteOperator(
        task_id='creating_table',
        sqlite_conn_id='sqlite_default',
        sql='''
            CREATE TABLE if not exists trips (
                trip_id INTEGER PRIMARY KEY AUTOINCREMENT,
                region TEXT NOT NULL,
                origin1 NUMERIC NOT NULL,
                origin2 NUMERIC NOT NULL,
                destination1 NUMERIC NOT NULL,
                destination2 NUMERIC NOT NULL,
                datetime TEXT NOT NULL,
                datasource TEXT NOT NULL
            );
            '''
    )

