from airflow.models.baseoperator import BaseOperator
from airflow.providers.oracle.hooks.oracle import OracleHook

class OracleDBOperator(BaseOperator):

    def __init__(self,
                 name: str,
                 oracle_conn_id: str,
                 sql: str,
                 **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.oracle_conn_id = oracle_conn_id
        self.sql = sql

    def execute(self, context):
        hook = OracleHook(
            oracle_conn_id = self.oracle_conn_id,
        )
        result = hook.get_first(self.sql)
        print(result)
        return result