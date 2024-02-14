-- This script creates the database 'hbtn_0d_2' and the user 'user_0d_2'

-- create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create the user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant user read only permissions on the 'htbn_0d_2' database
GRANT USAGE, SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- effect the change
FLUSH PRIVILEGES;
