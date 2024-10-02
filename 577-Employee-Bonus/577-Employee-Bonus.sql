SELECT
    Employee.name,
    Bonus.bonus
FROM
    Employee
LEFT JOIN
    Bonus
ON
    Employee.empID = Bonus.empId
WHERE
    Bonus.bonus < 1000 or Bonus.bonus IS NULL