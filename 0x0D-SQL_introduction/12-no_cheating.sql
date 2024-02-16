-- Update score of Bob to 10

SELECT second_table
SET score = 10
WHERE name = Bob;
SELECT score, name
FROM second_table;
