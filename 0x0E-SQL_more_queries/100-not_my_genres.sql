-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT DISTINCT t.name
FROM (tv_genres AS t INNER JOIN tv_show_genres AS g
ON t.id = g.genre_id) INNER JOIN tv_shows AS s
ON s.id = g.show_id
WHERE t.name NOT IN (
	SELECT name
	FROM tv_shows AS s INNER JOIN tv_show_genres AS g
	ON s.id = g.show_id
	INNER JOIN tv_genres AS t
	ON t.id = g.genre_Id
	WHERE title = 'Dexter'
)
ORDER BY t.name;
