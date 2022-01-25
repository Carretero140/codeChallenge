# codeChallenge
Coding challenge for data engineering

The only requirements to run this project is to have docker desktop installed.

To run this container, clone the repository and inside the folder in a terminal type the following command:

docker-compose -f docker-compose.yml up -d

this will then start all the containers needed to run airflow and the configuration is already set.

from there you can go to localhost:8080

log in with the username: airflow and password airflow

Then you can find this pipeline under DAGs