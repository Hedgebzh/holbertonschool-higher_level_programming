-- Task description : Write a script that updates the score of Bob to 10 in the table second_table.

-- command for show and list all database on the server
UPDATE second_table
SET
	score = '10'
WHERE name = Bob;
