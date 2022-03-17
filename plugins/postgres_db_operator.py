from airflow.models.baseoperator import BaseOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

class PostgresDBOperator(BaseOperator):

    def __init__(self,
                 name: str,
                 postgres_conn_id: str,
                 sql: str,
                 **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.postgres_conn_id = postgres_conn_id
        self.sql = sql

    def execute(self, context):
        hook = PostgresHook(
            postgres_conn_id = self.postgres_conn_id,
        )
        result = hook.get_records(self.sql)
        print(result)
        return result