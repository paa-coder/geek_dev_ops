import random
import math

separator_task = "*"*100

def separete(something,separator):
    print()
    print(separator,something,separator)
    print()


separete("task №1",separator_task)

fruits = [
    "яблоко","банан","апельсин",
    "ананас","персик","лимон",
    "мандарин","груша","киви"
    ]

def get_random_fruits(lenght=5):
    fruits = [
        "яблоко","банан","апельсин",
        "ананас","персик","лимон",
        "мандарин","груша","киви"
        ]
    return set([random.choice(fruits) for i in range(lenght)])

fruits_first = get_random_fruits()
fruits_second = get_random_fruits(4)

print("first fruits list:{}\nsecond fruits list:{}".format(fruits_first,fruits_second))
print("lists contains same fruits: {}".format([i for i in fruits_first if i in fruits_second]))

separete("task №2",separator_task)

random_int = set([random.randint(-100,100) for i in range(30)])

print("random numbers list:\n{}".format(random_int))
print("selected list condition( Элемент кратен 3,Элемент положительный,Элемент не кратен 4.): {}"
    .format([i for i in random_int if i%3==0 and i>=0 and i%4!=0]))

separete("task №3",separator_task)

def get_pow(list):
    return [i if i<0 else math.sqrt(i) for i in list.copy() if i!=-1]

init = [random.randint(-10,10) for i in range(5)]

print(" init state list {}".format(init))
print(" result list {}".format(get_pow(init)))
print(" state of init list {}".format(init))

separete("task №4",separator_task)

def cretae_question(question,type):
    try:
        return type(input(question.strip()+" "))
    except Exception as e:
        print("Error: value not correct: {}".format(e))
        return cretae_question(question,type)

def get_pow_2(integer):
    if integer==13:
        raise ValueError("not available value {}".format(integer))
    return integer**2


try:
    x = get_pow_2(cretae_question(" insert integer:", int))
except ValueError as e:
    print("Error: {}".format(e))
else:
    print("answer: {}".format(x))
