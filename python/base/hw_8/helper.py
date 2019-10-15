import datetime
import os
import shutil
from time import sleep

def log(message):
    with open("message.log","a",encoding="utf-8") as f:
        if(message):
            s ="{} {}".format(datetime.datetime.now(),message)
            f.write("{}\n".format(s))
            print(s)

def create_file(name,text= None):
    with open(name,"w",encoding="utf-8") as f:
        log("пересоздание файда {} c содержимым '{}'".format(name,text))
        if(text):
            f.write(text)

def change_dir(name):
    try:
        os.chdir(name)
        log("текущая дериктория изменена: {} ".format(os.getcwd()))
    except Exception as e:
        print("директория не найдена:",e,name)


def create_dir(name):
    try:
        os.mkdir(name)
        log("создание дериктории {} ".format(name))
    except FileExistsError as e:
        print("директория {} уже существует".format(name))

def get_list(only_dir=False):
    return [i for i in os.listdir() if (os.path.isdir(i) and only_dir) or not only_dir]

def delete(name):
    if not os.path.exists(name):
        print("{} не существует".format(name))
        return
    text=None
    if os.path.isdir(name):
        text = "директория удалена"
        os.rmdir(name)
    else:
        text = "файл удален"
        os.remove(name)

    log("{} {}".format(name,text))


def copy(name,new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name,new_name)
            log("копирование данных папки {} в {}".format(name,new_name))
        except FileExistsError as e:
            print("директория {} уже существует".format(new_name))
    else:
        shutil.copy(name,new_name)
        log("копирование данных файла {} в файл {}".format(name,new_name))
