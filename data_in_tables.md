# Data in Tables

**record**: single set of related data (aka row, data item, item)
**attribute**: a property of a record (aka column, data field, field)
**reading**: getting/querying/selecting: get value of something

What will you do with data?
**CRUD**: Create, Read, Update, Delete

Note: It is easy to add/delete rows; columns are hard to change.  To change a column, you must go thru each record and change it within the record.

---
## Relational Databases:
- Use tables
- Some examples: MySQL, PostgreSQL, SQLite, Apache Hive, MariaDB, Oracle, Microsoft Azure SQL, Microsoft SQL Server
- PostgreSQL: free, open-source, easy to download, compatable with Heroku (we'll use this in Ada)

**Concepts**:
- **Schema**: Layout for data. Name of each table, attributes(columns) in the tables, data type for each column, rules/constrains for each column and table (ie- no null values, integers > 0, etc)
- **Data types**: boolean, varchar, integer, text, numeric, timestamp, json
  - varchar: text, can define max length
  - text: no max length
