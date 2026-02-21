# Write your MySQL query statement below
with x as (
select id, num, 
lag(num, 1) over (order by id) as prev1,
lag(num, 2) over (order by id) as prev2

from Logs
)

select distinct num as ConsecutiveNums from x where num = prev1 and num = prev2