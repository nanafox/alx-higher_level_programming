-- This script lists all records of the 'second_table of the database
-- 'hbtn_0c_0' whose 'name' field is not NULL

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score
DESC;
