-- Create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO GENERATED NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL,
)i;
