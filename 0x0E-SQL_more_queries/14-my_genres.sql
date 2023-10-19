-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter


SELECT tg.name
FROM tv_genres AS tg INNER JOIN tv_show_genres as g
ON tg.id = g.genre_id
WHERE g.show_id =
	(SELECT id
		FROM tv_shows as s
		WHERE s.title = 'Dexter')
ORDER BY tg.name;
