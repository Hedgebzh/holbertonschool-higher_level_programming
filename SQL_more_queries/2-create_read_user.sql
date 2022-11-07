-- Task description : Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER 'user_0d_2'@'locasthost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.hbtn_0d_2 TO 'user_0d_2'@'locasthost';
