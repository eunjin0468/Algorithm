with t as (select player_id, min(event_date) as first_log
from activity
group by player_id)

select round(count(distinct t.player_id) / count(distinct a.player_id), 2) as fraction
from activity as a
left join t on a.player_id = t.player_id
            and a.event_date = date_add(t.first_log, interval 1 day)