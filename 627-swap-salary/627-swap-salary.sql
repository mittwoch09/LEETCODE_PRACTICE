# UPDATE Salary SET sex = CASE WHEN sex = "m" THEN "f" ELSE "m" END

UPDATE Salary
SET sex = CASE WHEN Salary.sex = 'm' THEN 'f'
               ELSE 'm' END
