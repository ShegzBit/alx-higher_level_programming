-- a script that lists all shows contained in the database hbtn_0d_tvshows

-- tries to use the let out join to get a list of all show

SELECT s.title, g.genre_id
FROM tv_shows AS s LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id
