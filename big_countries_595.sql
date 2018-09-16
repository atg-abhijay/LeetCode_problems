/*
URL of problem:
https://leetcode.com/problems/big-countries/description/
*/

Select name, population, area
From World
Where
    area > 3000000
    or population > 25000000
