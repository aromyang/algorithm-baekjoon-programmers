-- 코드를 입력하세요
SELECT member_id, member_name, gender, DATE_FORMAT(m.date_of_birth, '%Y-%m-%d') as date_of_birth
FROM member_profile m
WHERE MONTH(m.date_of_birth) = '3' AND tlno IS NOT NULL AND gender = 'W'
ORDER BY member_id