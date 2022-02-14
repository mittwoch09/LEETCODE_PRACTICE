SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1

/*
# Using SELF JOIN
SELECT DISTINCT p1.Email
FROM Person p1 JOIN Person p2 ON p1.Email = p2.Email AND p1.Id != p2.Id
*/

/*
# Using subquery
SELECT Email FROM
(SELECT Email, COUNT(Email) AS c
FROM Person
GROUP BY Email) AS temp
WHERE c > 1
*/