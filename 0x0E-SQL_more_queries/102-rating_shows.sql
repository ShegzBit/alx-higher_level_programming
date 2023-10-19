-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT s.title, COUNT(r.rate) AS `rating sum`
FROM tv_shows AS s INNER JOIN tv_show_ratings AS r
ON s.id = r.show_id
GROUP BY s.title
ORDER BY `rating sum` DESC;
