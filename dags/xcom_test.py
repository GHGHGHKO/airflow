import datetime
import pendulum

from airflow import DAG

from airflow.operators.python import PythonOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

def puller(task_instance=None):
    print(task_instance.xcom_pull(dag_id='postgres_db_operator', task_ids='postgres-db-task'))

with DAG(
    dag_id="python_xcom",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    python_xcom = PythonOperator(
        task_id="xcom-python",
        python_callable=puller,
    )

python_xcom