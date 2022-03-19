# airflow

<b>Airflow install</b><br>
https://pepega.tistory.com/44 

<b>Use Oracle</b><br>
https://pepega.tistory.com/45 

<b>Use BranchSqlOperator</b><br>
https://pepega.tistory.com/46

<b>Use EmailOperator</b><br>
https://pepega.tistory.com/47

<b>Use custom Operator</b><br>
https://pepega.tistory.com/48

<b>How to use PostgresOperator Hooks</b><br>
https://pepega.tistory.com/49

<b>How to use OracleOperator Hooks</b><br>
https://pepega.tistory.com/50

<b>XComs puller</b><br>
https://pepega.tistory.com/51

<b>Send XComs with email</b><br>
https://pepega.tistory.com/52

<b>Export csv with query</b><br>
https://pepega.tistory.com/53

## HOW TO DEPLOY

https://hub.docker.com/r/gudrb963/oracle-airflow/tags
```
docker pull gudrb963/oracle-airflow:2.2.4
```

https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html
```
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
```
docker-compose up airflow-init
```
```
docker-compose up -d
```
```
CONTAINER ID   IMAGE                           COMMAND                  CREATED       STATUS                 PORTS                              NAMES
f34defe769cf   gudrb963/oracle-airflow:2.2.4   "/usr/bin/dumb-init …"   8 hours ago   Up 7 hours (healthy)   8080/tcp                           airflow_airflow-scheduler_1
81c74d916079   gudrb963/oracle-airflow:2.2.4   "/usr/bin/dumb-init …"   8 hours ago   Up 7 hours (healthy)   0.0.0.0:5555->5555/tcp, 8080/tcp   airflow_flower_1
fae60f28729a   gudrb963/oracle-airflow:2.2.4   "/usr/bin/dumb-init …"   8 hours ago   Up 7 hours (healthy)   8080/tcp                           airflow_airflow-worker_1
ae3b89d69034   gudrb963/oracle-airflow:2.2.4   "/usr/bin/dumb-init …"   8 hours ago   Up 7 hours (healthy)   8080/tcp                           airflow_airflow-triggerer_1
184c9f48dcef   gudrb963/oracle-airflow:2.2.4   "/usr/bin/dumb-init …"   8 hours ago   Up 7 hours (healthy)   0.0.0.0:8080->8080/tcp             airflow_airflow-webserver_1
c01f07f266b3   postgres:13                     "docker-entrypoint.s…"   2 days ago    Up 7 hours (healthy)   5432/tcp                           airflow_postgres_1
621293a9c103   redis:latest                    "docker-entrypoint.s…"   2 days ago    Up 7 hours (healthy)   6379/tcp                           airflow_redis_1
```