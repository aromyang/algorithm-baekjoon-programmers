-- 코드를 입력하세요
SELECT A.rest_id, rest_name, food_type, favorites, address, ROUND(AVG(B.review_score), 2) as score
FROM rest_info A
JOIN rest_review B
ON A.rest_id = B.rest_id
GROUP BY A.rest_id
HAVING A.address LIKE '서울%'
ORDER BY score DESC, favorites DESC