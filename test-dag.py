import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


executor_config = {
    "KubernetesExecutor": {
        "image": "apache/airflow:1.10.10.1-alpha2-python3.6",
    }
}

common_task_args = {
    'retries': '1',
    'start_date': datetime(2019, 8, 26),
    'executor_config': executor_config
}

dag = DAG('test-dag', default_args=common_task_args, is_paused_upon_creation=True,schedule_interval=None)



test = BashOperator(
    task_id='hello_task',
    bash_command='echo hello;sleep 60;echo done',
    dag=dag
)
