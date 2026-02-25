# Write your MySQL query statement below
with ranked as 
(select player_id, event_date, 
row_number() over (partition by player_id order by event_date ) as rnk
from Activity )

select player_id, event_date as first_login from ranked where rnk = 1