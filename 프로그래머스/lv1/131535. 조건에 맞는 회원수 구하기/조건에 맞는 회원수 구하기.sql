-- 코드를 입력하세요
SELECT COUNT(*) AS users
FROM user_info
WHERE joined LIKE '2021%' AND (age >= 20 AND age <=29)
