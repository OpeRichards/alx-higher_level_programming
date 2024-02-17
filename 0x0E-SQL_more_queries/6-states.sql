-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PK,
	name VARCHAR(256) NOT NULL,
);
