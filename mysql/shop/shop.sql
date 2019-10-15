
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

drop table if exists orders;
create table orders(
  id serial primary key,
  user_id bigint unsigned,
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp,
  key index_of_user_id(user_id)
) comment = 'заказы';

drop table if exists products;
create table products(
  id serial primary key,
  order_id bigint unsigned,
  product_id bigint unsigned,
  total int unsigned comment 'количество заказанных товарных позиций',
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp
) comment = 'состав заказа';

drop table if exists discounts;
create table discounts(
  id serial primary key,
  user_id bigint unsigned,
  product_id bigint unsigned,
  discount float unsigned comment 'величена скидки от 0.0 до 1.0',
  stated_at datetime,
  finished_at datetime,
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp
) comment = 'скидки';

drop table if exists storehouses;
create table storehouses(
  id serial primary key,
  uname varchar(255) comment 'название'
) comment = 'склады';
