
INSERT INTO catalogs VALUES
  (DEFAULT, 'Процессоры'),
  (DEFAULT, ''),
  (DEFAULT, null),
  (DEFAULT, null),
  (DEFAULT, 'Мат.платы'),
  (DEFAULT, 'Видеокарты');

-- оставить условие можно но придется удалить unique index
DROP INDEX unique_name ON catalogs;

UPDATE catalogs SET name = 'emty'
WHERE name = '' or name is null;
