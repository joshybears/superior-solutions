-- Write your PostgreSQL query statement below

SELECT COALESCE((
    SELECT
        salary as "SecondHighestSalary"
    FROM (
        SELECT 
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) as rk
        FROM
            Employee
    )
    WHERE
        rk = 2
    LIMIT 1
        ), NULL) as "SecondHighestSalary"
