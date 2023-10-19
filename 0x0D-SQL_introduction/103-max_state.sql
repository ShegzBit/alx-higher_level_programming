-- 103-max_state.sql

SELECT state, MAX(value) AS max_temp
FROM temperatures AS t
WHERE t.month IN (7, 8)
GROUP BY state
ORDER BY state
LIMIT 3;
