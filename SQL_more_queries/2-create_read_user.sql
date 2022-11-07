-- Task description : Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- test
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- test
CREATE USER IF NOT EXISTS 'user_0d_2'@locasthost IDENTIFIED BY 'user_0d_2_pwd';
-- test
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@locasthost;
