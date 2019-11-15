# task1
echo "file1">file1
cp file1 file2
ln -s file1 file3
ln file1 file4
ls -li
rm file1
ls -li
#file 3 error
# task2
mv file2 tmp
rm ./file*
ln -s tmp tmp2
ln tmp tmp3
mkdir task2
mv -i tmp2 tmp3 ./task2
# error on ./task2/tmp2
# task3
touch tmp tmp2
chmod ug=rw,o=r tmp
chmod 664 tmp
chmod u=rw,go=r tmp2
chmod 644 tmp2
# task4
useradd -m -G sudo -s /bin/bash test
passwd test
killall -u test
userdel -r test
# task5
groupadd developer
useradd -m -G developer -s /bin/bash dev1
useradd -m -G developer -s /bin/bash dev2
passwd dev1
passwd dev2
umask 002
mkdir /home/dev
chgrp developer /home/dev
chmod ug+s,o-rwx /home/dev
# task6
mkdir /home/dev/exchange
chmod o-rwx exchange/
chmod +t exchange/
# task7
mkdir -m0773 /home/dev_blind
