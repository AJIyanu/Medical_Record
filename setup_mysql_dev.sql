-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS Medical_Record;
CREATE USER IF NOT EXISTS 'Medics'@'localhost' IDENTIFIED BY 'Medics123';
GRANT ALL PRIVILEGES ON `Medical_Record`.* TO 'Medics'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'Medics'@'localhost';
FLUSH PRIVILEGES;
