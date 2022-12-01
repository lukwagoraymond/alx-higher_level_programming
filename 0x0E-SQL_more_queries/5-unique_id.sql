-- Create a table unique_id on your MySQL server
-- unique_id table description (columns):
-- id INT DEFAULT 1
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS `force_name` (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
