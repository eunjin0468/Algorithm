select user_id, round(avg(if (c.action='confirmed',1,0)),2) as confirmation_rate 
from signups as s
join confirmations as c 
using (user_id)
group by ㄴ.user_id;