-- This script displays the top 3 of cities temperatures ordered by the
-- temperature (descending)

-- select the fields
SELECT city, AVG(value) AS avg_temp
FROM temperatures
-- the month should be July or August
WHERE month IN (7, 8)
-- group by the city
GROUP BY city
-- sort in descending order of the average temperature
ORDER BY avg_temp
DESC
-- display the top 3
LIMIT 3;
