import random

separator_task = "*"*100
separator_var = "-"*100

def separete(something,separator):
    print()
    print(separator,something,separator)
    print()


separete("task №1",separator_task)

def address(name="Василий",age=21,city="Москва"):
    return f'{name}, {age} год(а), проживает в городе {city}'

print(address())
print(address(name="Tom",city="London"))

separete("task №2",separator_task)

def custom_max(*args):
    return max(args)

print(custom_max(2,17,8))

separete("task №3",separator_task)

player_name = input("how to call a player? ")
enemy_name = input("how to call a enemy? ")

player = {
    "name":player_name
}

enemy = {
    "name":enemy_name
}

def build(item):
    item["health"]=1000+random.randint(100,300)
    item["damage"]=random.randint(100,300)
    item["armor"]=1+round(random.random(),2)

def attack(player1,player2):
    print(f'{player1["name"]} attack {player2["name"]} урон {player1["damage"]}')
    player2["health"] -= player1["damage"]
    return player2


for x in [player,enemy]: build(x)

enemy = attack(player,enemy)
player = attack(enemy,player)
enemy = attack(player,enemy)

separete("task №4",separator_task)

def damage_rate(damage,armor):
    return round(damage / armor);

def attack_armor(player1,player2):
    damage_less = damage_rate(player1["damage"],player2["armor"])
    print(f'{player1["name"]} attack {player2["name"]} урон уменьшен на {player1["damage"]-damage_less}')
    player2["health"] -= damage_less
    return player2

player = attack_armor(enemy,player)
enemy = attack_armor(player,enemy)
player = attack_armor(enemy,player)
