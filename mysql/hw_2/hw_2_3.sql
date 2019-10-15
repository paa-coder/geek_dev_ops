drop table if exists cat;

create table cat(
  id serial primary key,
  name varchar(255) comment 'название раздела'
) comment = 'разделы интернет магазина';


TRUNCATE catalogs;
INSERT INTO catalogs VALUES
  (DEFAULT, 'Процессоры'),
  (DEFAULT, 'Мат.платы'),
  (DEFAULT, 'Видеокарты');

INSERT INTO cat VALUES (DEFAULT, 'Видеокарты');

INSERT INTO cat (SELECT * FROM catalogs) ON DUPLICATE KEY UPDATE cat.name=catalogs.name;

SELECT * FROM cat;
