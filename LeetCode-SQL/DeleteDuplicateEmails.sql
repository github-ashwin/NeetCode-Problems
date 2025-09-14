# Write your MySQL query statement below
DELETE FROM Person
WHERE id NOT IN (
    SELECT temp.min_id
    FROM (
        SELECT MIN(id) AS min_id
        FROM Person
        GROUP BY email
    ) temp
);
