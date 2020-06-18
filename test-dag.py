import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


common_task_args = {
    'retries': '1',
    'start_date': datetime(2019, 8, 26),
}

dag = DAG('test-dag', default_args=common_task_args, is_paused_upon_creation=True,schedule_interval=None)



test = BashOperator(
    task_id='hello_task',
    bash_command='echo hello',
    dag=dag
)
