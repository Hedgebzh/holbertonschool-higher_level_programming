-- Task description : Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT * FROM states, cities WHERE name = 'California' AND states.name = 'California' ORDER BY cities.id;
