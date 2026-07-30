-- Lists all privileges of user_0d_1 and user_0d_2
SELECT * FROM information_schema.user_privileges WHERE grantee LIKE "'user_0d_1'%";
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
