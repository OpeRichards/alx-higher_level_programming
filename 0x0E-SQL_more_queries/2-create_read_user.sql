-- CREATE DATABASES
CREATE DATABASES 'hbtn_0d_2';

-- CREATE USER WITH PASSWORD
CREATE USER 'user_0d_2'@'localhost' 
IDENTIFIED BY 'user_0d_2_pwd';

-- CREATE SELECT permissionn to user
GRANT SELECT 
ON hbtn_0d_2.* 
TO 'user_0d_2'@'localhost';
