import pickle
import json
import os

separator_task = "*"*100

def separete(something,separator):
    print()
    print(separator,something,separator)
    print()

def check_file(file_name):
    f_path = os.path.join(os.getcwd(),file_name)
    if os.path.exists(f_path) and  os.path.isfile(f_path):
        return True
    print("file {} not found".format(f_path))
    return False

def read_pickle(file_name):
    if not check_file(file_name):
        return None
    with open(file_name,"rb") as f:
        return pickle.load(f)

def read_json(file_name):
    if not check_file(file_name):
        return None
    with open(file_name,"r",encoding="utf-8") as f:
        return json.load(f)


separete("task №2",separator_task)

for key,value in {"group.pickle":read_pickle,"group.json":read_json}.items():
    print("object from {}: ".format(key))
    data = value(key)
    if data:
        print(data)
