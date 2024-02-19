-- Make a list from 2 tables
SELECT cities.id, cities.name, states.name
FROM states
LEFT JOIN cities
ON states.id = cities.state_id 
