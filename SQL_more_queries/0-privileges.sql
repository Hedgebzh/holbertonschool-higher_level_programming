--Task description : Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

CREATE USER [IF NOT EXISTS] 'user_0d_1', 'user_0d_2';
SHOW GRANTS [FOR user_0d_1, user_0d_2];
