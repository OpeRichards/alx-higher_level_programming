-- Make a list from 2 tables
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.states_id 
