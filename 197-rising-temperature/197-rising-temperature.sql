SELECT w2.id
FROM Weather w1 JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = -1
WHERE w2.Temperature > w1.Temperature

# ON DATE_SUB(w1.RecordDate, INTERVAL 1 DAY) = w2.RecordDate
