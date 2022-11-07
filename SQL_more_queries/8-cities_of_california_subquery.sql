-- Task description : Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT * FROM (SELECT name FROM states UNION SELECT name FROM cities) WHERE name = 'California' ORDER BY cities.id;
