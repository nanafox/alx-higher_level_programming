-- This script removes all records with scores less than or equal to 5 in
-- the table 'second_table' of the database 'hbtn_0c_0'.

-- delete all records with a score <= 5
DELETE FROM second_table
WHERE score <= 5;
