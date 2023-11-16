-- script that creates the database hbtn_0d_usa and the table cities
-- cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
FOREIGN KEY (state_id) REFERENCES states(id)
);
