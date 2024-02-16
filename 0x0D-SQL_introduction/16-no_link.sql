-- List all records in DESC order

SELECT score, name
FROM second_table
WHERE name <> ""
ORDER BY score DESC;
