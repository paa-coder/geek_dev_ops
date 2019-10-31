-- 1  task
drop table if exists catalogs;
create table catalogs(
  id serial primary key,
  name varchar(255) comment 'название раздела',
  unique unique_name(name(10))
) comment = 'разделы интернет магазина';

drop table if exists users;
create table users(
  id serial primary key,
  name varchar(255) comment 'имя покупателя',
  birthday_at date comment 'дата рождения',
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp
) comment = 'покупатели';

drop table if exists products;
create table products(
  id serial primary key,
  name varchar(255) comment 'название',
  description text comment 'описани',
  price decimal(11,2) comment 'цена',
  catalog_id bigint unsigned,
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp,
  key index_of_catalog_id(catalog_id)
) comment = 'товарные позиции';

drop table if exists logs;
create table logs(
  id serial,
  table_name char(8) not null,
  item_id bigint unsigned not null,
  created_at datetime not null,
  name varchar(255) comment 'название'
) engine = Archive;

delimiter //
-- проседура для сохранения логов будет едина для всех
drop procedure if exists save_log//
create procedure save_log(table_name char(8),item_id bigint,created_at datetime,name varchar(255))
  begin
    insert into logs values (null,table_name,item_id,coalesce(created_at,now()),name);
  end //

-- создаем тригеры срабатывающие после добавления записи в таблице
drop trigger if exists products_inser//
create trigger products_inser after insert on products
  for each row
  begin
    call save_log('products',new.id,new.created_at,new.name);
  end//

drop trigger if exists users_inser//
create trigger users_inser after insert on users
  for each row
  begin
    call save_log('users',new.id,new.created_at,new.name);
  end//


drop trigger if exists catalogs_inser//
create trigger catalogs_inser after insert on catalogs
  for each row
  begin
    call save_log('catalogs',new.id,now(),new.name);
  end//

delimiter ;

-- 2 task

-- если есть доступ к данным в рамках текущих баз данных к примеру записи из sample.users перенести в shop.users
--  наиболее оптимальным будет insert into select

insert into users(name,birthday_at,created_at) select s.name,s.birthday_at,s.created_at from sample.users s;

-- если данные надо загрузить откуда то
--  наиболее оптимальным будет load data infile для выполнения не обходимо настроить secure_file_priv и local_infile
LOAD DATA INFILE 'pwd/users.csv' INTO TABLE users
  COLUMNS TERMINATED BY ';'
  LINES TERMINATED BY '\n' (name,birthday_at,created_at);
