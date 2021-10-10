# Sparkify Database - Schema and ETL

<<<<<<< HEAD
## Overview
||||||| c4e25fc
Overview
=======
#Overview
>>>>>>> fc1a3c3d607e45ad2dff1ccfa6b215b91d0c79a9
This project provides the schema and ETL to create and populate a database for the data analysis by a music streaming app Sparkify.

The schema is created using a PostgreSQL relational database in a star schema, which allows the Sparkify team to readily run queries to analyze user activity on their app, such as on what songs users are listening to. The scripts have been created in Python using pyscopg2 as python and connector.

<<<<<<< HEAD
## Structure
||||||| c4e25fc
Structure
=======
#Structure
>>>>>>> fc1a3c3d607e45ad2dff1ccfa6b215b91d0c79a9
The project contains the following elements:

<<<<<<< HEAD
* data/ contains song and log files of user activity in JSON format
* sql_queries.py creates the tables and how to insert data in each table using SQL queries.
* create_tables.py creates the Sparkify database and connects the database to a opensource postgresSQL platform i.e pgAdmin4.
* etl.py defines the ETL pipeline, which pulls and transforms the song and log JSON files in the local directory and inserts them into the Postgres database
* etl.ipynb and test.ipynb test some of the elements contained in the Python scripts

#### Schema
||||||| c4e25fc
data/ contains song and log files of user activity in JSON format
sql_queries.py creates the tables and how to insert data in each table using SQL queries.
create_tables.py creates the Sparkify database and connects the database to a opensource postgresSQL platform i.e pgAdmin4.
etl.py defines the ETL pipeline, which pulls and transforms the song and log JSON files in the local directory and inserts them into the Postgres database
etl.ipynb and test.ipynb test some of the elements contained in the Python scripts
Schema
=======
data/ contains song and log files of user activity in JSON format.

sql_queries.py creates the tables and how to insert data in each table using SQL queries.

create_tables.py creates the Sparkify database and connects the database to a opensource postgresSQL platform i.e pgAdmin4.

etl.py defines the ETL pipeline, which pulls and transforms the song and log JSON files in the local directory and inserts them into the Postgres database

etl.ipynb and test.ipynb test some of the elements contained in the Python scripts
Schema
>>>>>>> fc1a3c3d607e45ad2dff1ccfa6b215b91d0c79a9
The database contains the following fact table:

* songplays - fact table
songplays has foreign keys to the following dimension tables:

* users
* songs
* artists
* time

#### Softwares needed:
Python 3, NumPy, and Pandas installed using Anaconda.
A text editor like Jupyter Notebook.
A terminal application like Git Bash.
Opensource PosgreSQL admin platform such as pgadmin4 

#### Installation links for softwares:
Git for windows - for terminal application using Git Bash: https://git-scm.com/download/win
Anaconda for windows: https://docs.anaconda.com/anaconda/install/windows/
pgadmin for windows: https://www.pgadmin.org/download/pgadmin-4-windows/

#### Instructions
To run the project: Connect to any local PostgreSQL administration platform and connect to the database through a user. To execute the python files, Gitbash is being used using Anaconda.Below files are executed in the bash shell 

* run create_tables.py
* run etl.py
Make sure your working directory is at the top-level of the project.



Query Example
Once you've created the database and run the ETL pipeline, you can test out some queries:

## Connect to database
%load_ext sql
%sql postgresql://postgres@127.0.0.1/sparkifydb

## session_id in sogplays table where song_id is not NULL
SELECT session_id
FROM songplays
WHERE artist_id IS NOT NULL;

##  Distinct artists among song plays
SELECT DISTINCT a.artist_name \
FROM songplays s \
LEFT JOIN artists a ON s.artist_id = a.artist_id;
