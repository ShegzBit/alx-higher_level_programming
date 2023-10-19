-- 103-max_state.sql

SELECT `state`, MAX(value) AS `max_temp`
FROM `temperatures` AS t
GROUP BY `state`
ORDER BY `state`;
