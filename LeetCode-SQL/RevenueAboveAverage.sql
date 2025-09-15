/*
Find products with revenue above average
Suppose you have two tables:

Products(product_id, product_name, unit_price)

Sales(sale_id, product_id, quantity_sold, total_price, sale_date)

Question: Find names of products whose total revenue (sum of total_price) is greater than the average total revenue over all products.
*/

SELECT p.product_id, p.product_name, SUM(s.total_price) AS total_revenue
FROM Products p
LEFT JOIN Sales s
ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING SUM(s.total_price) > (
    SELECT AVG(product_revenue)
    FROM (
        SELECT SUM(total_price) AS product_revenue
        FROM Sales
        GROUP BY product_id
    ) sub
);
