SELECT
    author_id AS id
FROM
    Views
GROUP BY
    author_id
HAVING
    MAX(author_id = viewer_id) = 1
ORDER BY
    author_id ASC;