WITH report AS (
    SELECT
        managerId,
        COUNT(*) AS report_cnt
    FROM
        Employee
    GROUP BY
        managerId
    HAVING
        report_cnt >= 5
)
SELECT
    Employee.name
FROM
    report
JOIN
    Employee
ON
    report.managerId=Employee.id