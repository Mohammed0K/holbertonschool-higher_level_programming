-- script that lists all records of the table
SELECT score, name FROM second_table
WHERE name IS NOT NULL
  AND score IS NOT NULL
GROUP BY score, name
ORDER BY score DESC;
