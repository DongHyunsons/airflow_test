from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator


args = {'owner': 'jovyan', 'start_date': days_ago(n=1)}

dag = DAG(dag_id='my_first_dag',
        default_args=args,
        schedule_interval='@daily')

t1 = BashOperator(task_id='print_date',
        bash_command='date',
        dag=dag)

email = EmailOperator(
        task_id='send_email',
        to='sondonghyun7@hyundai.com',
        subject='Airflow Alert',
        html_content=""" <h3>Email Test</h3> """,
        dag=dag
        )

t1 >> email
