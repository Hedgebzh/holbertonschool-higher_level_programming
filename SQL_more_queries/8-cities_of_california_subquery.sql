-- Task description : Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT * FROM hbtn_0d_usa.cities WHERE hbtn_0d_usa.states = California ORDER BY cities.id;
