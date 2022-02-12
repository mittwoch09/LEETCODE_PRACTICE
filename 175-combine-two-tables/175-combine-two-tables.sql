# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person LEFT JOIN Address ON Person.PersonId = Address.PersonId

#FROM Person LEFT OUTER JOIN Address ON Person.PersonId = Address.PersonId
#FROM Address RIGHT JOIN Person ON Person.PersonId = Address.PersonId
