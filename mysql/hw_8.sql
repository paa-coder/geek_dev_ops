-- 1 task

delimiter //
drop function if exists hello//
create function hello()
  returns text deterministic
  begin
    declare hour int default cast(date_format(curtime(), "%h") as signed);
    if(hour between 0 and 5)then
      return 'доброй ночи';
    elseif(hour between 6 and 11)then
      return 'доброе утро';
    elseif(hour between 12 and 17)then
      return 'добрый день';
    else
      return 'добрый вечер';
    end if;
  end //
delimiter ;

-- 2 task

drop table if exists products;
create table products(
  id serial primary key,
  name varchar(255),
  description text
) comment = 'состав заказа';

delimiter //
drop function if exists valid_products//
create function valid_products(name varchar(255),description text)
  returns int deterministic
  begin
    if (name is null and description is null)then
      return 0;
    else
      return 1;
    end if;
  end //
drop trigger if exists products_desc_inser//
create trigger products_desc_inser after insert on products
  for each row
  begin
    if(not valid_products(new.name,new.description))then
      signal sqlstate '45000' set message_text = 'name or description must not empty';
    end if;
  end//
drop trigger if exists products_desc_update//
create trigger products_desc_update after update on products
  for each row
  begin
    if(not valid_products(new.name,new.description))then
      signal sqlstate '45000' set message_text = 'name or description must not empty';
    end if;
  end//
  delimiter ;

-- 3 task

delimiter //
drop function if exists fibonacci//
create function fibonacci(num int)
  returns bigint deterministic
  begin
    if(num < 0)then
      signal sqlstate '45000' set message_text = 'params must be unsigned';
    elseif(num > 92)then
      signal sqlstate '45000' set message_text = 'max value 92';
    elseif(num between 0 and 1)then
      return num;
    else
      begin
        declare sub_prew bigint default 0;
        declare prew bigint default 1;
        declare tmp bigint;
        set num = num -1;
        while num > 0 do
          set tmp = prew;
          set prew = tmp+sub_prew;
          set sub_prew=tmp;
          set num = num-1;
        end while;
        return prew;
      end;
    end if;

  end //
 delimiter ;
