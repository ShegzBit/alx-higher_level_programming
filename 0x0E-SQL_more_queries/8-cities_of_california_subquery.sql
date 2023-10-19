--  a script that lists all the cities of California that
-- can be found in the database hbtn_0d_usa

-- selects all states of california
SELECT c.id, name
FROM cities AS c
WHERE c.state_id = 
	(SELECT id FROM states AS s
		WHERE s.name = 'California'
	)
