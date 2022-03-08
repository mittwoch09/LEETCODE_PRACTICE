/*
SELECT IF(id < (SELECT MAX(id) FROM Seat), IF(id % 2 = 0, id-1, id+1), IF(id % 2 = 0, id-1, id)) AS id, student
FROM Seat
ORDER BY id
*/

SELECT
    CASE
        WHEN id % 2 = 0 THEN id - 1
        WHEN id % 2 = 1 AND id < (SELECT COUNT(*) FROM Seat) THEN id + 1
        ELSE id -- max odd num
    END AS id, 
    student 
FROM Seat
ORDER BY id