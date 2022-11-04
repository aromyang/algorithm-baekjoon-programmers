-- 코드를 입력하세요
SET @HOUR := -1;

SELECT (@HOUR := @HOUR +1) AS hour, (SELECT COUNT(*) 
                                     FROM animal_outs 
                                     WHERE HOUR(datetime) = @HOUR) AS count
FROM animal_outs
WHERE @HOUR < 23