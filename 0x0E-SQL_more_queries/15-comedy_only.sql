--  a script that lists all Comedy shows in the database hbtn_0d_tvshows

SELECT s.title
FROM tv_shows AS s INNER JOIN tv_show_genres AS g
ON s.id = g.show_id
WHERE g.genre_id =
	(SELECT id
		FROM tv_genres AS t 
		WHERE t.name = 'Comedy')
ORDER BY title;
