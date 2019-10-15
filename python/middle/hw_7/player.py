import random
from hamsters import Item

class Player(Item):
    health = 10
    max_health = 10

    def __init__(self,map):
        self.position = self.get_clear_position(map)




    def was_hit(self, hid):
        # self.health -= hid
        self.health -= 1 + random.choice(range(hid+1))

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
        print("player's health:", self.health)
