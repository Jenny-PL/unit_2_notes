# SQL

- Strings Use Single Quotes (') Only  
- SQL commands will end in `;`
- It is convention to capitalize commands (ie- CREATE TABLE)  
- White space is irrelevant
- You can identify a **primary key** for a table (this acts a constraint)
- use_snake_case when naming things in SQL
- Use = for equivalance (not ==)
- You can use `>` or `<` to compare strings (ie- `year < '1990'`)  
- Does not equal: `!=` or `<>`
- Operator precendence: 
- [Explanation of operator precendence](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/operator-precedence-transact-sql?view=sql-server-ver15)  
- example: `NOT` has greater precedence than  `AND` which has greater precendence than `OR`   

**Precedence example:** The following command will find al books (regardless of genre) by Madie McClure + all Intrigue books by Tim McDermott.  This is because `AND` has greater precedence and thus is evaluated first.
```
SELECT * from books
WHERE author = 'Madie McClure'
OR author = 'Tim McDermott'
AND genre = 'Intrigue';
```
 To instead select Intrigue books by either author, use `()` to group the `OR` clause.  
```
SELECT * from books
WHERE (author = 'Madie McClure' OR author = 'Tim McDermott')
AND genre = 'Intrigue';
```
--- 
### Order_by
```
SELECT
    columns_desired
FROM
    table_name
(additional optional clauses)
ORDER BY
    sort_expression1 sort_direction,
    sort_expression2 sort_direction,
    ... ;
```
 - **sort_direction**: `ASC` or `DEC`. If no value is give, default is `ASC`.
 - **sort_expression**: Most commonly, this will be a column name  

Simple example:
```
SELECT title
FROM books
ORDER BY title
```
```
SELECT title, price
FROM books
ORDER BY price DESC;
```
---
### Limit
To limit the results given at once:  
```
SELECT columns_desired
FROM table_name
(additional optional clauses)
LIMIT row_count;
```
Where row_count = the number of results you desire at once.

---
### Offset
To skip the first n results:
```
SELECT title
FROM books
WHERE genre = 'sci-fi'
OFFSET 10;
```
Will give results 11 on...    
Alternately, can be used together with limit: ` LIMIT 10 OFFSET 10` would give results 11 to 20.  

--- 
Other resources:
- [A game to pratice SQL](https://mystery.knightlab.com/)  
- [CS50 SQL Practice problems](https://cs50.harvard.edu/x/2022/psets/7/fiftyville/)  
- A tool for seeing SQL: [Pgadmin](
https://www.pgadmin.org/)   
