-- Lists all records where score >= 10 
-- order by score in Descending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
