-- This script displays the max temperature of each state (ordered by State
	-- name)

-- select the state, and compute it's maximum temperature
SELECT state, MAX(value) AS max_temp
FROM temperatures
-- group the results by the state
GROUP BY state
-- sort by the name of the state in ascending order
ORDER BY state;
