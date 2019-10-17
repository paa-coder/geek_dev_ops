--  в дз нет никаких дополнительных действий только запросы которые являются решением заданий
/*
  если хотите проверить создайте не обходимые условия для запуска решния того или иного задания
  Пример: 1.Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.(
    создайте таблицу поместите туда значения с незаполненными created_at и updated_at и запустите запрос указанний в блоке ниже)

    аналогично со всеми остальными заданиями
  */


-- 1 task

update users SET created_at=if(created_at is null,now(),created_at),updated_at=if(updated_at is null,now(),updated_at)
  where created_at is null or updated_at is null;

-- 2 task

update users SET
  created_at=if(created_at is null,null,STR_TO_DATE(created_at,'%d.%m.%Y %h:%i')),
  updated_at=if(updated_at is null,null,STR_TO_DATE(updated_at,'%d.%m.%Y %h:%i'))
where created_at is not null or updated_at is not null;

ALTER TABLE users CHANGE created_at created_at datetime;
ALTER TABLE users CHANGE updated_at updated_at datetime;

-- 3 task

select * from storehouses order by value=0,value desc;

-- 4 task

select * from users where DATE_FORMAT(birthday_at,'%M') in ('may', 'august')

-- 5 task

SELECT * FROM catalogs WHERE id IN (5, 1, 2) order by FIELD(id, 5, 1, 2);
