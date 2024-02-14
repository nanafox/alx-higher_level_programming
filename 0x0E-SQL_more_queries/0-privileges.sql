-- This script lists all privileges of users 'user_0d_1' and 'user_0d_2'

-- show the privileges for the users
SHOW GRANTS FOR 'user_0d_1'@'localhost'; 
SHOW GRANTS FOR 'user_0d_2'@'localhost'; 

-- flush privileges to effect change
FLUSH PRIVILEGES;
