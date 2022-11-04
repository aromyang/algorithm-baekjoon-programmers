-- 코드를 입력하세요
SELECT HOUR(datetime) AS hour, COUNT(*)
FROM animal_outs
WHERE HOUR(datetime) >= 9 AND HOUR(datetime) <= 19
GROUP BY HOUR(datetime)
ORDER BY hour