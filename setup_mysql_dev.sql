-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS Medical_Record;
CREATE USER IF NOT EXISTS 'Medics'@'localhost' IDENTIFIED BY 'Medics123';
GRANT ALL PRIVILEGES ON `Medics`.* TO 'Medical_Record'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
