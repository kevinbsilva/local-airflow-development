# local-airflow-development
A base repository for local airflow development and tests. It uses the base docker-compose shared by Airflow. This image contains an Airflow image, with a Postgres DB and a Celery executor with Redis.

It is ready to be used locally for development and testing. 


# Getting started

Make sure you have Docker instaled and you are in the same path as the `docker-compose.yml` file. Then, execute the following command:

```shell
docker-compose up
```

This will start all services and after a while you can log into the Airflow webserver locally, which is located by default at `localhost:8080`.


# Login in Web UI

To login, we have:

- username: airflow
- password: airflow


If you want to customize your credentials, feel free to change in docker-compose.yml:

```yml
_AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow}
_AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow}
```

The volumes are already configured so you can start developing your DAGs at `./dags`. It should appear on the webserver almost instantly. 