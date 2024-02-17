-- Create database
CREATE DATABASES 'hbtn_0d_2';

-- Create user with password
CREATE USER 'user_0d_2'@'localhost' 
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant permissions to user
GRANT SELECT 
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';
