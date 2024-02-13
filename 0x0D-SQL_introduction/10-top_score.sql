-- This script lists all records of the table 'second_table' of the database
-- 'hbtn_0c_0'. The results are returned based on the highest score.

-- list the score and name of the person ordered by the highest score.
SELECT score, name 
FROM second_table
ORDER BY score
DESC;
