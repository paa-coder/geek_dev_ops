-- task 1_______________________________________________

/*
если пользователь должен заходить не с локальной машины

create user 'shop'@'%' identified with sha256_password by 'shop';
grant all on shop.* to 'shop'@'%';
grant grant option on shop.* to 'shop'@'%';
show grants for 'shop'@'%';

*/
create user 'shop'@'localhost' identified with sha256_password by 'shop';
grant all on shop.* to 'shop'@'localhost';
grant grant option on shop.* to 'shop'@'localhost';
show grants for 'shop'@'localhost';

/*
*** из задания не понял должен ли иметь  shop_read доступы к другим бд если должен то использовать нужно нижний скрипт
grant USAGE, SELECT on *.* to 'shop_read'@'localhost'; \ grant USAGE, SELECT on *.* to 'shop_read'@'%';

*** если пользователь должен заходить не с локальной машины
create user 'shop_read'@'%' identified with sha256_password by 'shop_read';
grant usage, select on shop.* to 'shop_read'@'%';
show grants for 'shop_read'@'%';
*/
create user 'shop_read'@'localhost' identified with sha256_password by 'shop_read';
grant usage, select on shop.* to 'shop_read'@'localhost';
show grants for 'shop_read'@'localhost';



drop user 'shop'@'localhost';
-- drop user 'shop'@'%';
drop user 'shop_read'@'localhost';
-- drop user 'shop_read'@'%';


-- task 2_______________________________________________
drop table if exists accounts;
create table accounts(
  id serial primary key,
  name varchar(255),
  password varchar(255)
);
insert into accounts(name,password) values
  ('name1','pass1'),
  ('name2','pass2'),
  ('name3','pass3');

create or replace view username(id,name) as select id, name from accounts;

create user 'user_read'@'localhost' identified with sha256_password by 'user_read';
grant usage, select on shop.username to 'user_read'@'localhost';
show grants for 'user_read'@'localhost';
