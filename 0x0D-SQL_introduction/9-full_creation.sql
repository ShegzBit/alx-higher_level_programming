-- creates a full table `second_table and adds rows to it
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(25),
	score INT
);

INSERT INTO second_table VALUE(1, 'John', 10);
INSERT INTO second_table VALUE(2, 'Alex', 3);
INSERT INTO second_table VALUE(3, 'Bob', 14);
INSERT INTO second_table VALUE(4, 'George', 8)
