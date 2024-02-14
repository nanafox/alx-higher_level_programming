-- This script converts the 'hbtn_0c_0' database to UTF8

-- alter the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- select the 'hbtn_0c_0' database
USE hbtn_0c_0;

-- alter the table 'first_table'
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
