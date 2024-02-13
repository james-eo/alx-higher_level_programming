-- Temprature #2
-- Displays the max temprature of each state

SELECT state, MAX(value) AS "max_temp" 
FROM temperatures
GROUP BY state
ORDER BY state ASC;
