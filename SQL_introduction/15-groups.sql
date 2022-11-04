-- Task description : Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

-- command for show and list all database on the server
SELECT score, COUNT(*) AS number FROM second_table ORDER BY score DESC GROUP BY score ;
