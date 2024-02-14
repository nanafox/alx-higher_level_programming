-- This script lists all cities of California that can be found in the database
-- 'hbtn_0d_usa'

-- select the id and name fields from the `cities` table
SELECT c.id, c.name FROM cities c
-- select cities who's `state_id` match those in the "California" state
WHERE c.state_id IN (
	SELECT s.id
	FROM states s
	WHERE s.name = "California"
)
-- order the results by the `cities.id` in natural order (ascending)
ORDER BY c.id;
