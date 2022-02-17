from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from datetime import timedelta



args = {'owner': 'donghyun', 
        'depends_on_past':True,
        'email': 'sondonghyun7@hyundai.com',
        'email_on_failure': True
        }


dag = DAG(dag_id='my_third_dag',
        default_args=args,
        start_date = days_ago(1),
        schedule_interval='@daily')

t1 = BashOperator(task_id='test',
        bash_command='exit(1)',
        dag=dag)


t1
