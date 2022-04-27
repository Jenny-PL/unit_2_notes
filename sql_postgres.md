# Postgres
To open postgres in terminal:
```
psql -U postgres
```
You will see:
```
psql (14.2)
Type "help" for help.

postgres=# 
```

To exit the psql terminal, we use \q:
```
postgres=# \q
```
Restart Postgres with:
```
 $ brew services restart postgres
 ```
**Other commands in postgres**:  

`help` will summarize high-level psql commands  
`\?` will list all psql commands  
`\h` will list all SQL commands  
`\l` will list all available Postgres databases on this machine  
`\du` lists users


`\c <name>` to connect to a database by name  
`\dt`  view a list of all tables that are within the connected database 

`CREATE DATABASE db_name;`  This will create a new data_base with the name: db_name.  You must use a `;` at end of the command.    

`CREATE TABLE example_table_name (
    column_name data_type constraint_name,
    column_name data_type constraint_name
);`  

`DROP DATABASE db_name;` Drop the database; **not reversible!**
` DROP TABLE example_table_name;`  This will delete the table  

`\c db_name` To connect to a database by name

Example:   
```
postgres=# \c new_db 
You are now connected to database "new_db" as user "postgres".
new_db=# 
```

---
## Creating at Table (**C**RUD)
When creating a table, include:
- table name
- Columns and their data type
- Any column constraints
- Which column is the primary key

### Examples of creating a table:
```
CREATE TABLE example_table_name (
    column_name data_type constraint_name,
    column_name data_type constraint_name
);
```

```
CREATE TABLE example_table_name (
    column_name data_type PRIMARY KEY,
    column_name data_type constraint_name
);
```
```
CREATE TABLE authors (
  author_name VARCHAR(100),
  author_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY
);
```
```
CREATE TABLE drivers (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  vin VARCHAR(50),
  is_available BOOLEAN
);
```
```
CREATE TABLE media (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  category VARCHAR(50) NOT NULL,
  title VARCHAR(200) NOT NULL, 
  # not null is a constraint
  creator TEXT,
  publication_year VARCHAR(10),
  description_text TEXT
);
```
---
## Add a new record:
Example: 
```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

**Adding to a table when a value is unkown(ie - id number)**:  
One option: Include the id column and use `DEFAULT` for the value; table will auto-fill:  
```
INSERT INTO authors (author_name, author_id)
VALUES ('Octavia E. Butler', DEFAULT);
```
Another option: leave column out; table will auto-fill the id number.  
```
INSERT INTO authors (author_name)
VALUES ('Octavia E. Butler');
```
**Notes on adding columns and values**:
It is not essential to add in (column1, column2 ,etc) if the values are in order of our table's column, however it is likely best practice to list out the column names.  
- If we do not know a piece of info in a record (such as an ID), you can add DEFAULT as the value to match the column name (ie- data_id), or the column name and value can be left off.  SQL will automatically auto-fill the ID. 
- If an ID is always generated. Example:  
`guest_id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY`,   
then you cannot give a value in the column explicitly.
---
## Retrieving values within a table, aka Reading (C**R**UD)
- ` SELECT * from table_name`   
- `SELECT column_name from table_name`   

**Can also combine SELECT, FROM, and WHERE**:  
- This will narrow down the search
- `SELECT column1, column2 FROM table_name WHERE condition;`  
- For example: 
```
 SELECT title FROM media WHERE id <3;
 ```
- **SELECT** is a powerful command.  It can be used with defining multiple conditions in the WHERE clause, sorting the retrieved data, finding unique records, and finding records related to other records.

 ### Comparing with NULL:
 - Must use `IS NULL` or `IS NOT NULL`; cannot use = (it will return false)

## Updating data (CR**U**D)

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
**Where** is important... without it, evertyhing is updated!  

Another example:
```
UPDATE media
SET publication_year = '1990', description_text = NULL
WHERE media_id = 1;
```
---
## Deleting data (CRU**D**)

Syntax to delete from a table:
```
DELETE FROM table_name
WHERE condition;
```
Example:
```
DELETE FROM drivers
WHERE license_expires = '2020'
```
<mark>Without **where**, everything from table would be deleted!</mark>