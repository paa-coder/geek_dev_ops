import pickle
import json

separator_task = "*"*100

def separete(something,separator):
    print()
    print(separator,something,separator)
    print()

def write_pickle(file_name,data):
    with open(file_name,"wb") as f:
        pickle.dump(data, f)

def write_json(file_name,data):
    with open(file_name,"w",encoding="utf-8") as f:
        json.dump(data,f)


separete("task №1",separator_task)

for key,value in {"group.pickle":write_pickle,"group.json":write_json}.items():
    value(key,{
        "name": "Г.М.О.",
        "tracks": [
            "Последний месяц осени",
             "Шапито"
             ],
        "Albums": [
            {"name": "Делать панк-рок","year": 2016},
            {"name": "Шапито","year": 2014}
            ]
    })
    print("write in file {} ".format(key))
