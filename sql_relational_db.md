# Database relationships

## ERDs (Entity- relationship diagram)
- Databases can be drawn in diagrams, called ERDs (Entity-relationship diagram).  
- There are different types of relationships, including 1:1, 1:many, many:many.  The diagrams can be connected with lines that have symbols on each end to express whether they are zero, one, or many of each item.  
- Two separate tables can be related by a JOIN table (a third table they both reference)
- **Foreign key**: (aka referencing key) Can feed into another diagram/table 
- Note: lucidchart is a free software that can be used to make ERDs


## Foreign key
```
CREATE TABLE books (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  title VARCHAR(32),
  description TEXT,
  isbn VARCHAR(32),
  author_id INT,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);
```
## Create a join table:
```
CREATE TABLE books_genres (
  book_id INT,
  FOREIGN KEY (book_id) REFERENCES books(id),
  genre_id INT,
  FOREIGN KEY (genre_id) REFERENCES genres(id),
  PRIMARY KEY (book_id, genre_id)
);
```
## Using Select with Join

```
SELECT field1, field2, field3, ...
FROM table_name_a
INNER JOIN table_name_b
  ON condition
/* Optional WHERE clause */
```
Example query for book title + author, from two tables (books and authors), using author_id as the search term
```
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors
  ON books.author_id = authors.id;
  ```
To be more specific, you can add a `WHERE` conditional at end of command.
  ```
  SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors
  ON books.author_id = authors.id
WHERE authors.first_name = 'Kaja' and
  authors.last_name = 'Howell';
  ```

## Using Join with many to many relationships
```
SELECT books.title, genres.name
FROM books
INNER JOIN books_genres
  ON books_genres.book_id = books.id
INNER JOIN genres
  ON books_genres.genre_id = genres.id;
```

```
SELECT vendors.name
FROM vendors
INNER JOIN products
ON vendors.id = products.vendor_id;
```