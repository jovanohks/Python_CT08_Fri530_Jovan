import random
# class Animal:
#     def __init__(self,name,species,sound,food):
#         self.name=name
#         self.species=species
#         self.sound=sound
#         self.food=food
#     def describe(self):
#         print(f"this is a {self.name}, the {self.species}")
#     def make_sound(self):
#         print(f"{self.name} the {self.species} goes {self.sound}")
#     def food_source(self):
#         print(f"{self.name} the {self.species} goes {self.food}")
# elephant=Animal("elle","elephant","trumpet","grass")
# lion=Animal("leo","lion","roar", "meat")
# lion.describe()
# lion.make_sound()
# lion.food_source()
# elephant.describe()
# elephant.make_sound()
# elephant.food_source()
# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def show_details(self):
#         print(f"this car is a {self.brand} {self.model} at ${self.price}")
# bmw_car=Car("BMW","Z4","500000")
# toyota_car=Car("toyota","supra",150000)
# toyota_car.show_details()
# lambo_car=Car("lamboghrini","galladro",200000)
# ferrari_car=Car("Ferrari","enzo",400000)
# bmw_car.show_details()
class Fighter:
    def __init__(self,name,attack,health,defence):
        self.name=name
        self.attack=attack
        self.health=health
        self.defence=defence
    def attack_target(self,target):
        damage=self.attack +random.randint(-2,2)
        damage_dealt=damage-target.defence
        if damage_dealt >0:
            target.health-=damage_dealt
        else:
            damage_dealt=0
        print(f"{self.name} attached {target.name} for {damage_dealt}!")
        print(f"{target.name} has {target.health} remaining")
    def heal_self(self):
        heal_amount = self.defence+random.randint(-2,2)
        self.health+=self.heal_amount
        print(f"{self.name} healed for {heal_amount} health!")
    def is_alive(self):
        if self.health> 0:
            return True
        else:
            return False
hero= Fighter("hero",100,10,5)
goblin=Fighter("goblin",50,8,4)
turn=1
while goblin.is_alive():
    print(f"Turn {turn}")
    print("1.attack")
    print("2.heal")
    player_choice= int(input("enter your choice"))
    if player_choice==1:
        hero.attack_target(goblin)
    elif player_choice ==2:
        hero.heal_self()

    goblin.attack_target(hero)
    turn +=1