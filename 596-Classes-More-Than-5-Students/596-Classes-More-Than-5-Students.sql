SELECT
    c.class
FROM
    Courses AS c
GROUP BY
    c.class
HAVING
    COUNT(c.class) >= 5