-- This script lists all records with score greater than or equal to 10 in 
-- the table 'second_table' of the database 'hbtn_0c_0'.

-- list the score and name of the person ordered by the highest score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score
DESC;
