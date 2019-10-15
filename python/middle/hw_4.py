import requests as rq
from itertools import groupby
from bs4 import BeautifulSoup as BS
import re

def cretae_question(question,type):
    try:
        string = input(question.strip()+" или введите exit чтобы прервать выполнение скрипта: ")
        if string=="exit":
            sys.exit()
        else:
            return type(string)
    except TypeError as e:
        print("Ошибка: не корректно введено значение")
        return cretae_question(question,type)

def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link

def get_content(link):
    return rq.get(link).text

def visualize_common_words(content,start=100,end=90):
    try:
        start = int(start)
        end = int(end)
    except TypeError as e:
        rint("Ошибка: не корректно указан диапазон")
    words_list = re.findall("[а-яА-Я\-\']{4,}", content)
    words_list.sort()
    words = [ tuple([key,len(list(group))]) for key, group in groupby(words_list)]
    words.sort(key=lambda t: t[1],reverse = True)
    for w in words[start if start<end else end : end if end>start else start]:
        print(w[0])


def get_wiki_sub_links(s):
    bs = BS(s,"html.parser")
    div = bs.find(id="mw-content-text")

    # ссылки ищутся только в основной части иначе каша получается
    #зачем все возмем только 5
    return [i["href"] for i in div.findChildren(href=re.compile("/wiki/%.*")) if not i.get("class",[])][:5]

def get_topic(link,pattern):
    return pattern.findall(link)[0]



list = [];

pattern = re.compile("/wiki/(%.*)")
for l in get_wiki_sub_links(get_content(get_link(cretae_question("введите искомую информацию",str)))):
    list.append(l)
    [list.append(i) for i in get_wiki_sub_links(get_content(get_link(get_topic(l,pattern))))]

print("")
print("_"*100)
print("не понял задания из чего в конце концов должен состоять результирующий список поэтому состоит из 5 ссылок искомой страницы и пяти ссылок из каждой из страниц на которую они ведут   ")
print("")
print("\n".join(list))
