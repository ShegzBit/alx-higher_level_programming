-- my sql task 16 prints all rows with a name

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
