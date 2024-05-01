--create db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
--create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
--grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- flush to access privilege
FLUSH PRIVILEGES;
-- give privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- flush to access privilege
FLUSH PRIVILEGES;
