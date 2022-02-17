from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta
from airflow.utils.email import send_email

def on_failure(context):

    task = context.get('task_instance').task_id
    dag = context.get('task_instance').dag_id
    message = """
    <h3>:red_circle: Task Failed.</h3>
    <h3>Task: {}</h3>
    <h3>Dag: {}</h3>
    """.format(task,dag)

    send_email('sondonghyun7@hyundai.com', "TestEmailAlert",message)

args = {'owner': 'donghyun', 
        'depends_on_past':True,
        'on_failure_callback': on_failure

        }


dag = DAG(dag_id='FfailMailTestEachTask_dag',
        default_args=args,
        start_date = days_ago(1),
        schedule_interval='@daily')

t1 = BashOperator(task_id='task1',
        bash_command='whoami',
        dag=dag)

t2 = BashOperator(task_id='task2',
        bash_command='whoami',
        dag=dag)

t3 = BashOperator(task_id='task3',
        bash_command='whoami',
        dag=dag)

t4 = BashOperator(task_id='task4',
        bash_command='whoami',
        dag=dag)

t5 = BashOperator(task_id='task5',
        bash_command='exit(1)',
        dag=dag)


t6 = BashOperator(task_id='task6',
        bash_command='whoami',
        dag=dag)


t1 >> t2 >> [t3,t4] >> t5 >> t6


