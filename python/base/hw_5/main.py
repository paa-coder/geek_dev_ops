from first import create
import second

separator_task = "*"*100

def separete(something,separator):
    print()
    print(separator,something,separator)
    print()


list = [1,2,3,4,5]

if __name__=="__main__":

    separete("task №1",separator_task)
    create([1,2,3,4,5])

    separete("task №2",separator_task)
    print("list of {} return: {}".format(list,second.random_from_list(list)))
    print("emty list return {}".format (second.random_from_list([])))
