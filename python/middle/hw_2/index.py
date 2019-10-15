from bs4 import BeautifulSoup as BS
import requests as req
import re
import sys

separator_var = "-"*100

def separete(something,separator=separator_var):
    print()
    print(separator,something,separator)
    print()

def get_content():
    encoding = "utf-8"
    try:
        return req.get("https://geekbrains.ru").content.decode(encoding)
        # return req.get("https://geekbrcdacdaains.ru").content.decode(encoding)
    except Exception as e:
        print(f"Ошибка получения данных сайта {e}")
        print("Инфа из заготовленного файла")
        file_name="index.html"
        try:
            with open("index.html","r",encoding=encoding) as f:
                return f.read()
        except FileNotFoundError as e:
            print(f"Ошибка получения чтения файда {file_name}: {e}")
            sys.exit()

separete("task1")

s = get_content()

print(re.sub("[ ]","",re.findall("<span class=\"total-users\">[^\d]*([\d\s]+)",s)[0]))

separete("task2")

bs = BS(s,"html.parser")

print(re.sub("[^\d]","",bs.find("span", "total-users").string))



# with open("index.html","w") as f:
#     f.write(bs.prettify())
