SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary NOT IN (SELECT MAX(salary) FROM Employee)

# If there is no second highest salary, the query should report null