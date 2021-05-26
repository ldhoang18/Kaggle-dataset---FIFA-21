# Kaggle-dataset---FIFA-21
There is one sql file, fifa21.sql, that contains 2 tables to be created: player and team. There is one python file that is used to display data visualization. There is one csv file to be imported into the table

#connect to psql:
psql -d username_db where username is your name in remote server
\i fifa21.sql to initiate the table on terminal

###importing csv files:
COPY tablename(attribute1, attribute2, attribute3, attribute4...)
FROM './path/to/file.csv'
DELIMITER ','
CSV HEADER;

where tablename is a table initiated at the terminal. Type \t or \dt for more information. 

###displaying visualization:
type python file_on_repo.py, replace file_on_repo.py with the name of the py file seen in this repository
