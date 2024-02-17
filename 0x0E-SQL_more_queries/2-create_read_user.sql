-- CREATE DATABASES
CREATE DATABASES IF NOT EXISTS 'hbtn_0d_2';

-- CREATE USER WITH PASSWORD
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' 
IDENTIFIED BY 'user_0d_2_pwd';

-- CREATE SELECT permissionn to user
GRANT SELECT 
ON hbtn_0d_2.* 
TO 'user_0d_2'@'localhost';
