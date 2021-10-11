# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""Create Table if not exists songplays 
                        ( songplay_id serial PRIMARY KEY,
                        start_time timestamp NOT NULL,
                        user_id INT NOT NULL,
                        level varchar,
                        song_id VARCHAR,
                        artist_id VARCHAR,
                        session_id int,
                        location VARCHAR,
                        user_agent varchar NOT NULL);
              
                        
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users
                        (user_id INT PRIMARY KEY,
                        first_name varchar NOT NULL,
                        last_name varchar NOT NULL,
                        gender CHAR(1),
                        level varchar);
                     
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs
                        (song_id varchar PRIMARY KEY,
                        title varchar NOT NULL,
                        artist_id varchar,
                        year int,
                        duration numeric NOT NULL);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists
                        (artist_id varchar PRIMARY KEY,
                        name varchar NOT NULL,
                        location varchar,
                        latitude float,
                        longitude float);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time
                        (start_time timestamp PRIMARY KEY,
                        hour int,
                        day int,
                        week int,
                        month int,
                        year int,
                        weekday int);
                        
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent) 
                                    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
                          ON CONFLICT DO NOTHING
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                            VALUES (%s, %s, %s, %s, %s)
                           ON CONFLICT(user_id) DO UPDATE SET level =excluded.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                            VALUES (%s, %s, %s, %s, %s)
                           ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""INSERT INTO artists (artist_id,name,location,latitude, longitude)
                            VALUES (%s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")


time_table_insert = ("""INSERT Into time (start_time, hour, day, week , month, year, weekday)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                            ON CONFLICT DO NOTHING
""")

# FIND SONGS

"""This query is created to extract song_id and artist_id from song and artist tables 
and load it in song_id and artist_id column in songplays table"""

song_select = ("""SELECT s.song_id, a.artist_id 
                FROM artists a
                JOIN songs s
                ON a.artist_id=s.artist_id 
              WHERE s.title = %s AND a.name = %s AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]