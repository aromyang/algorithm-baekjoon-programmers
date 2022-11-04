-- 코드를 입력하세요
SELECT A.flavor
FROM first_half A JOIN icecream_info B ON A.flavor = B.flavor
WHERE A.total_order > 3000 AND B.ingredient_type = 'fruit_based'
ORDER BY A.total_order DESC 