-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table with constraints 
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT NOT NULL PK,
	state_id INT NOT NULLL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
