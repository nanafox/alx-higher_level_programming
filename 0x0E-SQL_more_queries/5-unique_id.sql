-- This script creates the table 'unique_id'

-- create a table with a unique id field
CREATE TABLE IF NOT EXISTS unique_id (
	-- id defaults to 1 if not provided, and must be unique
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
