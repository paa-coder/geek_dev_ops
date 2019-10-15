#! /usr/bin/env python
# -*- coding: utf-8 -*-
# separator = "*******************"
#
# def separete(task_number):
#     print(separator,"task №",task_number,separator)
#
# def cretae_question(question,type,order=0):
#     if order>0:
#         print("Ошибка: не корректно введено значение")
#     try:
#         return type(input(question.strip()+" "))
#     except TypeError as e:
#         order+=1
#         cretae_question(question,type,order)
#
#
#
# separete(1)
#
# number_t1 = cretae_question("Дай число?",int)
# print("ответ = "+str(number_t1+2))
#
# separete(2)
#
# while True:
#     number_t2 = cretae_question("Дай число?",int)
#     if number_t2>0 and number_t2<10:
#         print("ответ = "+str(number_t2**2))
#         break
#     print("Число должно быть >0 и <10")
#
# separete(3)
#
# surname_t3 = cretae_question("Фамилия?        ",str)
# name_t3 = cretae_question("Имя?",str)
# age_t3 = cretae_question("Какой возраст?",int)
# weight_t3 = cretae_question("Какой вес?",int)
#
# diagnosis= None
#
# if age_t3<30 and weight_t3<120 and weight_t3>50:
#     diagnosis = "хорошее состояние"
# elif (weight_t3>120 or weight_t3<50) and age_t3>30:
#     if age_t3>40:
#         diagnosis = "следует обратится к врачу!"
#     else:
#         diagnosis = "следует заняться собой"
# else:
#     diagnosis = "все норм"
#
# print(name_t3,surname_t3, end=', ')
# print(age_t3,"год", end= ', ')
# print("вес",weight_t3, end=' - ')
# print(diagnosis)


class A:
    a=0

b = A()

print(b.c+b.d)
