import datetime
import pendulum

from airflow import DAG

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.sql import BranchSQLOperator

KST = pendulum.timezone("Asia/Seoul")

default_args = {
    'owner': 'pepega',
}

with DAG(
    dag_id="postgres_branch_test",
    start_date=datetime.datetime(2022, 3, 1, tzinfo=KST),
    schedule_interval="@once",
    catchup=True,
    tags=['pepega'],
) as dag:
    true_branch_operator = BranchSQLOperator(
        task_id="true_sql_branch_id",
        conn_id="postgres_test",
        sql="sql/account_count.sql",
        follow_task_ids_if_true="true_operator_1st",
        follow_task_ids_if_false="false_operator_1st",
    )

    false_branch_operator = BranchSQLOperator(
        task_id="false_sql_branch_id",
        conn_id="postgres_test",
        sql="sql/zero_count.sql",
        follow_task_ids_if_true="true_operator_2nd",
        follow_task_ids_if_false="false_operator_2nd",
    )

    true_dummy_operator = DummyOperator(
        task_id='true_operator_1st',
    )

    false_dummy_operator = DummyOperator(
        task_id='false_operator_1st',
    )

    true_dummy_operator_2nd = DummyOperator(
        task_id='true_operator_2nd',
    )

    false_dummy_operator_2nd = DummyOperator(
        task_id='false_operator_2nd',
    )

true_branch_operator >> [true_dummy_operator, false_dummy_operator]
false_branch_operator >> [true_dummy_operator_2nd, false_dummy_operator_2nd]