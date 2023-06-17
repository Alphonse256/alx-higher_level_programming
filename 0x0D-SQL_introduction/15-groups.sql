-- Counting how many scored highly
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
