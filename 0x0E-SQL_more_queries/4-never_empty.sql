-- This script creates the table 'id_not_null'

-- create the table if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
	-- the id field can not be left empty, it defaults to '1' if not provided
	id INT NOT NULL DEFAULT 1,
	name VARCHAR(256)
);
