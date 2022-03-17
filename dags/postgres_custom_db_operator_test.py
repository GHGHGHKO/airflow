import datetime
import pendulum

from airflow import DAG

from postgres_db_operator import PostgresDBOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

with DAG(
    dag_id="postgres_db_operator",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    hello_db_task = PostgresDBOperator(
        task_id="postgres-db-task",
        name="pepega",
        postgres_conn_id="postgres_test",
        sql="select * from account;",
    )
hello_db_task