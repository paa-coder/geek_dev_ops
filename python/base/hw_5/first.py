from time import sleep
import sys
import shutil
import os

def delete(list):
    for s in list:
        new_path = os.path.join(os.getcwd(),"test_{}".format(s))
        shutil.rmtree(new_path)


def create(list):
    for s in list:
        new_path = os.path.join(os.getcwd(),"test_{}".format(s))
        os.mkdir(new_path)

    print("Директории созданы")
    for i in range(10, 0, -1):
        str_t = "директории удалятся через: {}".format(i);
        print(str_t, end='\r')
        sleep(1)
        print(" "*len(str_t), end='\r')
    delete(list)
    print("директории удалены")

if __name__=="__main__":
    create([1,2,3,4,5])
