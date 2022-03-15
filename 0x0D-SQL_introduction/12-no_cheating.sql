-- Updates the score of Bob to 10 in the table second_table.
-- You are not allowed to use Bob’s id value, only the name field

UPDATE LOW_PRIORITY IGNORE second_table
SET
    score = 10
WHERE
    name = 'Bob';
