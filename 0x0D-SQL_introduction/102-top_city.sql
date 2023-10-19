-- 102-top_city.sql

SELECT city, AVG(value) AS 'avg_temp'
FROM temperatures AS t
WHERE t.month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
