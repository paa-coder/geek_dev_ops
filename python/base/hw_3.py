import time

def create_question(question):
    answer = input(f'{question} [yes/no]: ')
    result = False
    if(answer.strip()=="yes"):
        result = True
    elif(answer.strip()!="no"):
        print("ответь точнее!",end="")
        return create_question(question)
    return result

def nextTry(number):
    return create_question(f'ты загадал число {number}?')

def wait(question):
    time.sleep(2)
    if(create_question(question)):
        return True
    return wait(question)

def get_middle(number_range):
    return number_range[0]-1+round((number_range[-1]-number_range[0])/2+0.5);

def start_game():
    print("Привет",end=",")
    if(create_question("хочешь фокус?")):
        number_range = range(1,101)
        print(f'Загадай число от {number_range[0]} до {number_range[-1]}')
        if wait("загадал?"):
            count_tries = 1
            while not nextTry(get_middle(number_range)):
                count_tries+=1

                if(create_question("загаданное число больше?")):
                    number_range = range(get_middle(number_range)+1,number_range[-1]+1)
                else:
                    number_range = range(number_range[0],get_middle(number_range),1)

                if len(number_range)==1:
                    print(f'значит ты загадл {number_range[0]} и всего то с {count_tries} попытки )))')
                    break
            else:
                print(f'угадал с {count_tries} попытки )))')
