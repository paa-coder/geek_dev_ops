create database if not exists examples;

use examples;

create table if not exists users (
  id bigint not null auto_increment,
  name varchar(255),
  primary key (id)
)engine=InnoDB;

-- я не пользуюсь .my.cnf
-- \! mysqldump -u root --password="secret" examples > dump_example.sql
\! mysqldump examples > dump_example.sql

create database if not exists samples;
use samples;
source dump_example.sql;

-- я не пользуюсь .my.cnf
-- \! mysqldump -u root --password="secret" mysql help_keyword --where=" 1=1 order by help_keyword_id asc limit 100" > few_rows_dump.sql
\! mysqldump  mysql help_keyword --where=" 1=1 order by help_keyword_id asc limit 100" > few_rows_dump.sql
