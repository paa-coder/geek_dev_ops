from helper import separete
from itertools import groupby
import sys
import re

def popular(count,list_c):
    list_c.sort()
    counting = [ tuple([key,len(list(group))]) for key, group in groupby(list_c)]
    counting.sort(key=lambda t: t[1],reverse = True)
    return counting[:count]

s = None
separete("task1")
try:
    with open("test.txt","r") as f:
        s = f.read()
except FileNotFoundError as e:
    print("файл с пирмером не найден: {}".format(e))


if not s:
    sys.exit()
print(s)

separete("task2")

t1 = re.findall("\S[^\.!\?]+[\.!\?]+(?:\S(?:[^А-Я]+)|)",s)
for i in range(len(t1)):
    print("{}-{}".format(i,t1[i]))

separete("task3")

print(popular(10,[i.lower() for i in re.findall("[А-Яа-яA-Za-z]{4,}",s)]))

separete("task4")

pattern = re.compile('\w+[\w/.\-_]*\.\w{2,}[/\w]*(?:\?(?:[\w&=%]*)[\w]+)?')

list_link = pattern.findall(s)
print(list_link)

separete("task5")

print(popular(1,[re.split("/",i)[0] for i in pattern.findall(s)]))

separete("task6")

print(re.sub(pattern,"Ссылка отобразится после регистрации",s))
