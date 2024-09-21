SELECT
    Orders.customer_number
FROM
    Orders
GROUP BY
    Orders.customer_number
ORDER BY
    COUNT(customer_number) DESC
LIMIT
    1;