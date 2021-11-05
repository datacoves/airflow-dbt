from airflow import DAG
from airflow_dbt.operators.dbt_operator import DbtSeedOperator

from airflow.utils.dates import days_ago

default_args = {"dir": "/root/dbt_project", "start_date": days_ago(0)}
with DAG(dag_id="dbt", default_args=default_args, schedule_interval="@daily") as dag:

    dbt_seed = DbtSeedOperator(
        task_id="dbt_seed",
    )
