# SQL practice
## Make a new table
```
CREATE TBALE restaurants (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
    name VARCHAR(30),
    minutes_to_walk INT,
    rating INT CHECK (rating > 0 and rating < 6)
);
```
## Add a new record to table:
**Best practice is to include column names**
```
INSERT INTO restaurants (name, distance, rating)
VALUES ('Ada Cafe', 3, 5);
```
Other variations:  
```
INSERT INTO restaurants (id, name, minutes_to_walk, rating)
VALUES (DEFAULT, 'Ada Cafe', 3, 5);
```   

```
INSERT INTO restaurants 
VALUES (DEFAULT, 'Ada Cafe', 3, 5);
```
## Read from the table
```
# Get all restaurants less than 5 mins away

SELECT name FROM restaurants 
WHERE minutes_to_walk < 5;
```

## Update a table
```
# Change a Ada Cafe's rating to 1

UPDATE restaurants
SET rating = 1
WHERE name = 'Ada Cafe';
```
## Delete a record from a table
```
# Delete Ada Cafe record 

DELETE FROM restaurants
WHERE name = 'Ada Cafe';
```

## Solar Sytem Database, Planets Table
```
CREATE TABLE Planets(id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, Name VARCHAR(30), Surface_Area_in_Miles INT, Moons INT, Distance_from_Sun_in_Miles INT, Namesake TEXT);
```
```
INSERT INTO planets VALUES (DEFAULT, 'Jupiter', 23710000000,79,483300000, 'King of the Roman gods, aka Zeus.' );
```
Above psql command gives error: `ERROR:  integer out of range`  
- Must alter table constraints from INT to BIG INT for surface_area:
    ```
    ALTER TABLE planets ALTER COLUMN distance_from_sun_in_miles TYPE BIGINT;
    ```
    ```
    ALTER TABLE planets ALTER COLUMN surface_area_in_miles TYPE BIGINT;
    ```
---
## Find the number of records: COUNT
`SELECT COUNT(*) as num_planets from planets; ` 
`SELECT COUNT(*) from planets;`

## How to Read in from a CSV file with a loop:????
for line in file:
planet_items = line.split(',')

    name = str(planet_items[0])
    Surface_Area_in_Miles = planet_items[1]
    Moons = planet_items[2]
    Distance_from_Sun_in_Miles = planet_items[3]
    Namesake = planet_items[4].strip(")

    INSERT INTO Planets
    VALUES (DEFAULT, name, Surface_area_in_miless, moon, distance_from_sun_in_miles, Namesake);