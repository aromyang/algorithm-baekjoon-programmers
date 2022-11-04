-- 코드를 입력하세요
SELECT animal_type, COUNT(animal_type)
FROM animal_ins
GROUP BY animal_type
HAVING animal_type IN ('Cat', 'Dog')
ORDER BY animal_type