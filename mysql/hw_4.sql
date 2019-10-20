-- 1 task

select avg(timestampdiff(year,birthday_at,now())) as avg_years from users;

-- 2 task

select
  DAYOFWEEK(MAKEDATE(YEAR(now()),DAYOFYEAR(birthday_at))) as day_number,
  DAYNAME(MAKEDATE(YEAR(now()),DAYOFYEAR(birthday_at))) as day_name,
  count(*) as count_birthday
from users
  group by day_number,day_name order by day_number;

-- 3 task

select round(exp(sum(log(id)))) from users;
