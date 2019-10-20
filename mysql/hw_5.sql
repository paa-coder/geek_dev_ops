--  1 task

select * from users u  where exists (select 1 from orders o where o.user_id=u.id limit 1);

-- 2 task

select p.*,c.name as catalog_name from products p join catalogs c on (c.id=p.catalog_id)
  where p.catalog_id = (select catalog_id from products where name = "Процессор Intel Core i3-8100 OEM");

-- 3 task

create table cities(
  label varchar(255) primary key,
  name varchar(255)
);

insert into cities(label,name) VALUES
  ("moscow","Москва"),
  ("irkutsk","Иркутск"),
  ("novgorod","Новгород"),
  ("kazan","Казань"),
  ("omsk","Омск");

create table flights(
  id serial primary key,
  `from` varchar(255),
  `to` varchar(255),
  foreign key index_of_from1(`from`) REFERENCES cities(label) on update cascade on delete cascade,
  foreign key index_of_to1(`to`) REFERENCES cities(label) on update cascade on delete cascade
);

insert into flights(`from`,`to`) VALUES
  ("moscow","omsk"),
  ("novgorod","kazan"),
  ("irkutsk","moscow"),
  ("omsk","irkutsk"),
  ("moscow","kazan");

select
  f.id, fr.name,t.name
from flights f
  join cities fr on (fr.label=f.from)
  join cities t on (t.label=f.to);
