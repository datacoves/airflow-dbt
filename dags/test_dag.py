from airflow import DAG
from airflow_dbt.operators.dbt_operator import DbtBuildOperator
from airflow.utils.dates import days_ago


default_args = {"dir": "/root/dbt_project", "start_date": days_ago(0)}
with DAG(
    dag_id="DbtBuildOperator_Test",
    default_args=default_args,
    schedule_interval="@daily",
) as dag:

    dbt_build = DbtBuildOperator(
        task_id="dbt_buid",
    )
