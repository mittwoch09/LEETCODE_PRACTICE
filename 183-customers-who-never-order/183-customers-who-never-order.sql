SELECT c.name AS "Customers"
FROM Customers c
LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.ID IS NULL