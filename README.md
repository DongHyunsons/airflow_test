# airflow_test
## test email alert in airflow

docker pull jupyter/base-notebook:python-3.7.3
docker run --name py3 -it -p 8881-8889:8881-8889 -v C:\notebooks\:/notebooks/ jupyter/base-notebook:python-3.7.3 bash

conda update -y conda
conda install -y airflow=1.10.3
conda install -y vim

airflow initdb      ##    여기서 버전 문제가 있을 수 있으므로 그것에 맞게 다운그레이드

echo 'export AIRFLOW_HOME=\~/airflow' >> /home/jovyan/.profile
echo 'export AIRFLOW_HOME=\~/airflow' >> /home/jovyan/.bashrc
source ~/.profile

mkdir $AIRFLOW_HOME/dags


airflow
├── airflow.cfg          <- airflow 환경설정 파일
├── airflow.db           <- 데이터베이스(SQLite)파일
├── dags                 <- DAG들을 저장하는 디렉토리
│   └── my_first_dag.py  <- DAG 정의 파이썬 파일
├── logs                 <- 로그파일을 저장하는 디렉토리

airflow version

DAG python 파일 작성 후 

airflow scheduler & airflow webserver -p 8882 

http://localhost:8882/admin 접속하여 확인
