-- This script updates the score of "Bob" to 10 in the second_table of the
-- 'hbtn_0c_0' database

-- update Bob's score to 10
UPDATE second_table 
SET score = 10
WHERE name = "Bob";
