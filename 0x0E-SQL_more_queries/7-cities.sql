-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table with constraints
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT NOT NULL PK,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
