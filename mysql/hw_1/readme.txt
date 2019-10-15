_____________
!!! необходимо находиться в директории папки
mysql> \! ls -la

drwxr-xr-x  6 paa  staff  192 15 окт 18:48 .
drwxr-xr-x  3 paa  staff   96 15 окт 18:46 ..
-rw-r--r--  1 paa  staff   35 15 окт 17:42 .my.cnf
-rw-r--r--  1 paa  staff  697 15 окт 18:48 example.sql
-rw-r--r--  1 paa  staff  114 15 окт 18:33 example_drop.sql
-rw-r--r--  1 paa  staff  172 15 окт 18:44 readme.txt

_____________
запустить домашнее задание:
mysql> source example.sql;

удалить базы данных и дампы:
mysql> source example_drop.sql;
