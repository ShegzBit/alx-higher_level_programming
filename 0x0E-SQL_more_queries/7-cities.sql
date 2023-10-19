-- create a database and a city table with foreign key referencing state table
CREATE SCHEMA IF NOT EXISTS hbtn_0d_usa;

-- Use database
USE hbtn_0d_usa;

-- create city if not exists
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
);
