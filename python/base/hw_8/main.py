import helper
import sys
from hw_3 import start_game

separator_var = "-"*100

def separete(something,separator):
    print()
    print(separator,something,separator)
    print()

def cretae_question(question,type):
    try:
        return type(input(question.strip()+" или введите exit чтобы прервать выполнение скрипта: "))
    except TypeError as e:
        print("Ошибка: не корректно введено значение")
        return cretae_question(question,type)

def help_custom():
    separete("HELP",separator_var)
    for key,value in functions.items():

        print(f"{key} - {value['name']} {'параметры:' if len(value['props']) else ''} ",end="")

        for key_p,value_p in value["props"].items():
            print("{}({})".format(value_p["name"],"обязателен" if value_p["required"] else "не обязателен"),end="; ")
        print("")
    separete("HELP",separator_var)

functions = {
    ":mk_file":{
        "name":"создание файла",
        "func": helper.create_file,
        "props":{
            2:{
                "type":str,
                "name":"имя нового файла",
                "required":True
            },
            3:{
                "type":str,
                "name":"содеожимое",
                "required":False
            }
        }
    },
    ":mk_dir":{
        "name":"создание папки",
        "func": helper.create_dir,
        "props":{
            2:{
                "type":str,
                "name":"имя новой папки",
                "required":True
            }
        }
    },
    ":cd":{
        "name":"изменение дериктории",
        "func": helper.change_dir,
        "props":{
            2:{
                "type":str,
                "name":"путь",
                "required":True
            }
        }
    },
    ":rm":{
        "name":"удалени файла или папки",
        "func": helper.delete,
        "props":{
            2:{
                "type":str,
                "name":"имя удаляемого файла или папки",
                "required":True
            }
        }
    },
    ":list":{
        "name":"удалени файла или папки",
        "func": helper.get_list,
        "props":{
            2:{
                "type":bool,
                "name":" показывать только папки",
                "required":False
            }
        }
    },
    ":copy":{
        "name":"сопирование файла или папки",
        "func": helper.copy,
        "props":{
            2:{
                "type":str,
                "name":"что копировать",
                "required":True
            },
            3:{
                "type":str,
                "name":"куда копировать",
                "required":True
            }
        }
    },
    ":game":{
        "name":"игра",
        "func": start_game,
        "props":{}
    },
    ":h":{
        "name":"возможности",
        "func": help_custom,
        "props":{}
    }
}

def get_props(props):
    list = []
    for key,value in props.items():
        try:
            list.append(sys.argv[int(key)])
        except IndexError as e:
            if(value["required"]):
                list.append(cretae_question("не найден параметр, укажите {}".format(value["name"]),value["type"]))
    return list


def start(command_name):
    if command_name=="exit":
        sys.exit()
    if not command_name in functions:
        return start(cretae_question("комманда не найдена, укажите команду",str))
    comand = functions[command_name]
    if(len(comand["props"])):
        return comand["func"](*get_props(comand["props"]))
    return comand["func"]()


try:
    command = sys.argv[1]
except IndexError as e:
    help_custom()
    command = cretae_question("комманда не указана, укажите команду",str)
finally:
    print(start(command.strip()))
