from grid.position import Position
from world.animal import Animal
import random


class Turtle(Animal):

    def __init__(self, world, position):
        super(Turtle, self).__init__(2, 1, world, position)

    def collision(self, attacker):
        if attacker.get_strength()>4:#Reflects attacks of animal with strength less than 5. 
            super(Turtle, self).collision(attacker)

    def action(self):
        if random.randint(0, 3) ==1:#Has 75% chance to stay in the same place.
            super(Turtle, self).action()

    def get_new_organism_object(self):
        return Turtle(self.world, Position())

    def get_symbol(self):
        return "T"

    

    
            