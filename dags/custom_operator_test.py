import datetime
import pendulum

from airflow import DAG

from hello_operator import HelloOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

with DAG(
    dag_id="custom_operator",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    hello_task = HelloOperator(task_id="sample-task", name="foo_bar")