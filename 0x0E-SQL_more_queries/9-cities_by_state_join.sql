-- This script lists all the cities contained in the database 'hbtn_0d_usa' and
-- their corresponding state names

-- select the city id, city name and state name
SELECT c.id, c.name, s.name
-- grab them from the cities tables and inner join on the states table
FROM cities c JOIN states s
	-- join on the premise of the `state_id` being the same
	ON c.state_id = s.id
-- order the result by the city id in ascending order
ORDER BY c.id;
