## Description
---
This repo provides the ETL pipeline, to populate the postgres database.  
* The purpose of this database is to enable postgres to answer business questions it may have of its users, the types of songs they listen to and the artists of those songs using the data that it has in logs and files. The database provides a consistent and reliable source to store this data.

* This source of data will be useful in helping postgres reach some of its analytical goals, for example, finding out songs that have highest popularity or times of the day which is high in traffic.

## Database Design and ETL Pipeline
---
* For the schema design, the STAR schema is used as it simplifies queries and provides fast aggregations of data.

<img width="724" alt="image" src="https://github.com/Tuantn97/Postgres_ETL/assets/130779401/ef2cc6b0-1cf6-4405-94c5-a36df7fa72fc">

* For the ETL pipeline, Python is used as it contains libraries such as pandas, that simplifies data manipulation. It also allows connection to Postgres Database.

* There are 2 types of data involved, song and log data. For song data, it contains information about songs and artists, which we extract from and load into users and artists dimension tables

* Log data gives the information of each user session. From log data, we extract and load into time, users dimension tables and songplays fact table.

## Running the ETL Pipeline
---
* First, run create_tables.py to create the data tables using the schema design specified. If tables were created previously, they will be dropped and recreated.

* Next, run etl.py to populate the data tables created.
