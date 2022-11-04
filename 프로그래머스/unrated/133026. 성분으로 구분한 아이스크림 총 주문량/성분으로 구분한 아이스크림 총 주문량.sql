-- 코드를 입력하세요
SELECT ingredient_type, SUM(total_order) AS total_order
FROM first_half A JOIN icecream_info B
ON A.flavor = B.flavor
GROUP BY ingredient_type
ORDER BY total_order