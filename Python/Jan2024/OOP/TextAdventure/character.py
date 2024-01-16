from weapon import fists
from health_bar import 

# create a character
class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists
    
    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)

        print("==================================================")
        print(f"Damage dealt of {self.name}: {self.weapon.damage}")
        print(f"Health of {target.name}: {target.health}")
        print("==================================================")
# create a sub class for the Hero

class Hero(Character):
    def __init__(self, name: str, health: int):
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon

    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}!")

    def drop(self):
        self.weapon = self.default_weapon
        print(f"{self.name} dropped {self.weapon.name}")


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon):
        super().__init__(name=name, health=health)
        self.weapon = weapon
    