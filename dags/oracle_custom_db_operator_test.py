import datetime
import pendulum

from airflow import DAG

from oracle_db_operator import OracleDBOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

with DAG(
    dag_id="oracle_db_operator",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    oracle_db_task = OracleDBOperator(
        task_id="oracle-db-task",
        name="pepega",
        oracle_conn_id="oracle_test",
        sql="select * from dual",
    )
oracle_db_task