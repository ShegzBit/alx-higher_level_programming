-- shows all shows linked to a genre

-- try to get all show linked using a right out join

SELECT s.title, g.genre_id
FROM tv_shows AS s INNER JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id;

