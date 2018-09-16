/*
URL of problem:
https://leetcode.com/problems/swap-salary/description/
*/

UPDATE salary
SET sex =
    CASE WHEN (sex = 'm') THEN 'f'
        ELSE 'm'
        END
