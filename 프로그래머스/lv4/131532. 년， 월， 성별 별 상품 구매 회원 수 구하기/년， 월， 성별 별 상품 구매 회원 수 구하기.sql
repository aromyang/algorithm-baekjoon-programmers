-- 코드를 입력하세요
SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month, gender, COUNT(DISTINCT A.user_id) AS users
FROM user_info A JOIN online_sale B
ON A.user_id = B.user_id
GROUP BY year, month, gender
HAVING gender IS NOT NULL
ORDER BY year, month, gender