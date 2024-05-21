-- Write your PostgreSQL query statement below

with wf as (
SELECT
    reports_to as employee_id,
    COUNT(*) over (PARTITION BY reports_to) as reports_count,
    AVG(age) over (PARTITION BY reports_to) as average_age
FROM
    Employees
),

rowsu as (
SELECT
    wf.employee_id,
    e.name as name,
    wf.reports_count,
    ROUND(wf.average_age) as average_age,
    ROW_NUMBER() over (PARTITION BY wf.employee_id ORDER BY wf.employee_id) as rn
FROM
    Employees e
JOIN
    wf
ON
    e.employee_id = wf.employee_id
)

SELECT
    employee_id,
    name,
    reports_count,
    average_age
FROM
    rowsu
WHERE
    rn = 1
