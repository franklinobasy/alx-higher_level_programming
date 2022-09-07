-- Script that lists all the cities of California registered in the database
-- Query to list all the cities from California
SELECT id, name 
  FROM cities
 WHERE state_id = ( -- Query to get the id of California
      SELECT id
        FROM states
       WHERE name = "California");