-- 1 task
start transaction;
insert into sample.users  (select * from shop.users sb where sb.id=1)  on DUPLICATE key update
  sample.users.name=sb.name,
  sample.users.birthday_at=sb.birthday_at,
  sample.users.created_at=sb.created_at;

delete from shop.users sb where sb.id=1;

commit;

-- 2 task

create or replace view product_catalog (product_name,catalogs_name)
  as p.name,c.name
  from products p left join catalogs c on (p.catalog_id=c.id)

-- 3 task

create table dates(
  `date` date
);

insert into dates VALUES
  ('2018-08-01'), ('2016-08-04'), ('2018-08-16'),('2018-08-17');


with recursive dates_list as (
    select date("2018-08-01") as date_value
    union all
    select date(adddate(date_value, interval 1 day)) as date_value
    from dates_list d
    where d.date_value < last_day("2018-08-01")
)
select d.date_value, 1-isnull(ds.date) present
from dates_list d left join dates ds on ds.date = d.date_value
order by d.date_value;

-- tas4

delete from table t where t.id not in (
  select t2.id from table t2 order by t2.created_at desc,t2.id desc limit 5
)
