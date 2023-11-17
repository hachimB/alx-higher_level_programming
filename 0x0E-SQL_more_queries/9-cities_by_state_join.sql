-- A script that lists all cities contained in the database hbtn_0d_usa.
-- ONE SELECT AND JOIN
SELECT cities.id, cities.name, states.name FROM cities
RIGHT JOIN states ON cities.id = states.id
WHERE cities.id IS NULL;
