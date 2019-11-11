# task1
ls -la /etc /proc /home
cat /etc/crontab
cat /etc/netconfig
# task2
cat > tmp
cat > tmp2
cat tmp tmp2 > tmp3
# task3
touch tmp tmp2
mkdir temp_dir
mv -i tmp2 ./temp_dir
rm -rf ./*
# task4
ls -A1 ~/ | grep "^\." | wc -l
# task5
touch ~/error
cat /etc/* /etc/.* 2>~/error
cat ~/error | wc -l
# task6
#first tab
tail -fn30 log
#second tab
ps aux | grep tail
kill pid
#first tab
Terminated
# task7
lsof -u0 -a /dev | less
# task8
for i in $(seq 2019 2023);
  do for m in $(seq 1 12);
    do mkdir -p ~/lessons1/filles/$i/$m;
  done;
done;
#task9
for y in $(ls ~/lessons1/filles/);
  do for m in $(ls ~/lessons1/filles/$y);
    do for ds in $(date -d "$y/$m/1 + 1 month - 1 day" "+%d");
      do for d in $(seq 1 $ds);
        do
          date=`date +%Y%m%d%H -d "$y/$m/$d"`
          echo "$date.txt">~/lessons1/filles/$y/$m/$date.txt
        done;
      done;
    done;
  done;
#task10
ls -lA /etc/|grep -v ^t |cut -d' ' -f1| sort | uniq | wc -l
