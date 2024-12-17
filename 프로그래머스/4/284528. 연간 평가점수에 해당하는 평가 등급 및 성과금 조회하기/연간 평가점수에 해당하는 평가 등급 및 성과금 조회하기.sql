-- 코드를 작성해주세요
SELECT 
    HEG.EMP_NO AS EMP_NO,
    HEG.EMP_NAME AS EMP_NAME,
    HEG.GRADE,
    CASE
        WHEN HEG.GRADE = 'S' THEN HEG.SAL * 0.2
        WHEN HEG.GRADE = 'A' THEN HEG.SAL * 0.15
        WHEN HEG.GRADE = 'B' THEN HEG.SAL * 0.1
        ELSE 0
    END AS BONUS
FROM (
    SELECT
        HE.EMP_NO,
        HE.EMP_NAME,
        HE.SAL,
        CASE
            WHEN HGA.SCORE >= 96 THEN 'S'
            WHEN HGA.SCORE >= 90 THEN 'A'
            WHEN HGA.SCORE >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE
    FROM HR_EMPLOYEES HE
    JOIN (
        SELECT HG.EMP_NO, AVG(HG.SCORE) AS SCORE
        FROM HR_GRADE HG
        GROUP BY HG.EMP_NO
    ) HGA
    ON HE.EMP_NO = HGA.EMP_NO
) HEG
ORDER BY HEG.EMP_NO ASC;
