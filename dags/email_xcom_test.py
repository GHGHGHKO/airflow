import datetime
import pendulum

from airflow import DAG

from airflow.operators.email_operator import EmailOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

with DAG(
    default_args = default_args,
    dag_id="send_email",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    email_operator = EmailOperator(
        task_id='send_email',
        to='receiver@example.com',
        subject='[TEST] 테스트 메일입니다.',
        html_content="""
                        테스트 메일입니다.<br/><br/> 
                        ninja template<br/>
                        {{ data_interval_start }}<br/>
                        {{ ds }}<br/>
                        {{ task_instance.xcom_pull(dag_id='postgres_db_operator', task_ids='postgres-db-task') }}<br/>
                    """,
    )

email_operator