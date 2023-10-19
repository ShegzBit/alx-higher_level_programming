-- create a Table if not exsists
CREATE TABLE IF NOT EXISTS `unique_id` (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
