-- 코드를 입력하세요
SELECT A.flavor AS flavor
FROM first_half A JOIN july B
ON A.flavor = B.flavor
GROUP BY A.flavor
ORDER BY SUM(A.TOTAL_ORDER) DESC
LIMIT 3