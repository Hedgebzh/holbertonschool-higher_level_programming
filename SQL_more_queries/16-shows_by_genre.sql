-- Task description : Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
CREATE USER [IF NOT EXISTS] 'user_0d_1' IDENTIFIED BY PASSWORD 'user_0d_1_pwd';
GRANT ALL ON `database`.* TO 'user_0d_1'@'localhost';
