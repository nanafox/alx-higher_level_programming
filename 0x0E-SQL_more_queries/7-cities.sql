-- This script creates the database 'hbtn_0d_usa' and the table 'city'

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

use hbtn_0d_usa;

-- create the cities table
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT fk_cities_state_id FOREIGN KEY (state_id)
	REFERENCES states (id)
);
