drop table if exists users;
create table users(
  id serial primary key,
  name varchar(255) comment 'имя',
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp
) comment = 'пользователь';

drop table if exists files;
create table files(
  id serial primary key,
  path varchar(255) comment 'путь к файлу в файловой системе',
  name varchar(255) comment 'название',
  description text comment 'описание',
  teg_list json comment 'ключевые слова',
  user_id bigint unsigned,
  created_at datetime default current_timestamp,
  updated_at datetime default current_timestamp on update current_timestamp,
  key index_of_user_id(user_id),
  key index_of_name(name(10))
) comment = 'пользователь';
