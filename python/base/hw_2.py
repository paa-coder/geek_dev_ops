from calendar import monthrange

separator_task = "*******************"
separator_var = "-------------------"

def separete(something,separator):
    print()
    print(separator,something,separator)
    print()

map_months = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11:"ноября",
    12:  "декабря"
}

map_days = {
    28: "двадцать восьмое",
    29: "двадцать девятое",
    30: "тридцатое",
    31: "дридцать первое"
}

def get_date():
    string_date = ""
    try:
        arr_date = input("введите дату в формате d.m.Y: " ).split(".")
        if(len(arr_date)!=3):
            raise Exception("указаная дата не соответсвует формату")
        day=int(arr_date[0])
        month=int(arr_date[1])
        year=int(arr_date[2])
        if (not month in map_months.keys()):
            raise Exception("не корректно указан месяц")
        if(day<1 or day>31):
            raise Exception("не корректно указан день")
        if(not day in map_days.keys()):
            raise Exception("лень писать словарь укажите день в промежутке {}".format(list(map_days.keys())))
        count_days_in_month = monthrange(year,month)[1]
        if(not day in range(1,count_days_in_month+1)):
            raise Exception("в указанном месяце {} дней".format(count_days_in_month))

        print(map_days[day],map_months[month],year)
        string_date =  "{} {} {} года".format(map_days[day],map_months[month],year)
    except Exception as e:
        print("не корректно указана дата:{}".format(e))
        get_date()

    return string_date


separete("task №1",separator_task)


#можно сделать через set но будет не коректно если my_list_1 будет содержать дубли элементов отсутствующие в  my_list_2
separete("вариант 1 корректен для указанных спсиков,будет не коректно если my_list_1 будет содержать дубли элементов отсутствующие в  my_list_2",separator_var)
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
print("my_list_1:",my_list_1)
print("my_list_2:",my_list_2)
print("answer:",list(set(my_list_1)-set(my_list_2)))
#через цикл будет корректен не зависимо от состава списков

separete("вариант 2 корректен",separator_var)
my_list_1 = [2, 5, 8, 2, 12, 12, 4,13,13]
my_list_2 = [2, 7, 12, 3]
print("my_list_1:",my_list_1)
print("my_list_2:",my_list_2)
for value in my_list_2:
    while value in my_list_1:
        my_list_1.remove(value)

print("answer:",my_list_1)

separete("task №2",separator_task)
print(get_date())

separete("task №3",separator_task)

my_list_1 = [2, 2, 5, 12, 8, 2, 12]
print("my_list_1:",my_list_1)
my_list_2 = []
for item in my_list_1:
    if my_list_1.count(item)>1:
        continue
    my_list_2.append(item)
print("my_list_2:",my_list_2)
