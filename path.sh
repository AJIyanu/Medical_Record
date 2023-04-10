#!/bin/bash

# MySQL database credentials
DB_USER="Medics"
DB_PASSWORD="Medics123"
DB_NAME="Medical_Record"

# Export data from MySQL database
mysqldump -u $DB_USER -p$DB_PASSWORD $DB_NAME > data.sql

# Import data to MySQL database
#mysql -u $DB_USER -p$DB_PASSWORD $DB_NAME --insert-ignore < data.sql

# Clean up the data.sql file
rm data.sql
