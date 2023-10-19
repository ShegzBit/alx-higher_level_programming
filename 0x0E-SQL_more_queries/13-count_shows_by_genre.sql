-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

SELECT tg.name AS 'genre', 
COUNT(g.show_id) AS number_of_shows
FROM tv_genres AS tg INNER JOIN tv_show_genres AS g
ON g.genre_id = tg.id
GROUP BY genre
HAVING number_of_shows >= 1
ORDER BY number_of_shows DESC;
