"""Simple DAG to print the configuration used in the UI trigger"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from typing import Any, Dict

with DAG(
    dag_id="test_dag_conf",
    schedule_interval=None,
    start_date=days_ago(1),
    description=(
        "Example DAG to print a given configuration "
        "in the UI after trigger"
    )
) as dag:
    
    
    def get_conf(dg_conf: Dict[str, Any], **context) -> None:
        print(dg_conf)
    
    t = PythonOperator(
        task_id="get_conf",
        python_callable=get_conf,
        op_kwargs={"dg_conf": "{{ dag_run.conf }}"}
    )