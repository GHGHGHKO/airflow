import datetime
import pendulum

from airflow import DAG

from postgres_csv_export_operator import PostgresCsvExportOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

with DAG(
    dag_id="postgres_csv_export",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    export_csv = PostgresCsvExportOperator(
        task_id="postgres-csv-export",
        name="pepega",
        postgres_conn_id="postgres_test",
        sql="select * from account;",
    )

export_csv