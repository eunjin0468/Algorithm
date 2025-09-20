select r.contest_id,  round(count(u.user_id)/(select count(*) from users)*100,2) as percentage
from users u
join register r on u.user_id=r.user_id
group by r.contest_id 
order by percentage desc, r.contest_id;