# codeChallenge
This is a very simple pipeline done in airflow and containerized with docker to demonstrate data engineering skills and how an end to end process should look like. 

## Requirements
The only requirements to run this project is to have docker desktop installed.

## Steps
To run this container, clone the repository and inside the folder in a terminal type the following command:

docker-compose -f docker-compose.yml up -d

this will then start all the containers needed to run airflow and the configuration is already set.

from there you can go to localhost:8080

log in with the username: airflow and password airflow

## Setting up Connections

Go to admin > Connections as shown in the image below:

![alt text](/airflowConnections.png)

Click on the + button to add a new connection and enter the following details:
![alt text](/file_path.png)

Click save then create another connection:
![alt text](/sqlite.png)

## Running the DAG
Go to your Dags and then trigger it via the action arrow on the far right as shown on the image:
![alt text](/dagRun.png)

If you want to see details of execution of the dag you can click on it.