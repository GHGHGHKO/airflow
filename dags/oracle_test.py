import datetime
import pendulum

from airflow import DAG
from airflow.providers.oracle.operators.oracle import OracleOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

with DAG(
    dag_id="oracle_test",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    oracle_task = OracleOperator(
        task_id='oracle',
        oracle_conn_id='oracle_test',
        sql='SELECT * FROM DUAL',
        dag=dag,
    )

oracle_task