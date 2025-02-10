from datetime import datetime
import os
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline

default_args = {
    'owner': 'Mateus Naza',
    'start_date': datetime(2025, 2, 6)  # Corrigido aqui
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit']
)

extract = PythonOperator(
    task_id='reddit_extract',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag  # Adicionado aqui
)

extract  # Adicionado para garantir que a tarefa esteja na DAG
