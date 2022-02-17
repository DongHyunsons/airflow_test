from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.utils.email import send_email

def on_failure(context):

    print("=====================================")
    print("test")
    print("=====================================")

    send_email('sondonghyun7@hyundai.com', "TestEmailAlert","Hi")

args = {'owner': 'donghyun', 
        'depends_on_past':True,
        }


dag = DAG(dag_id='my_second_dag',
        default_args=args,
        start_date = days_ago(1),
        schedule_interval='@daily')

t1 = BashOperator(task_id='test',
        on_failure_callback= on_failure,
        bash_command='exit(1)',
        dag=dag)


t1
