from PyQt5.QtWidgets import QTextEdit

from grid.grid_is_full_exception import GridIsFullException
from grid.commentator import Commentator
from world.world import World
from grid.position import Position


class Organism:

    def __init__(self, strength, initiative, world: World, position: Position):
        self._strength = strength
        self.age = 1
        self.initiative = initiative
        self.position = position
        self.world = world 

    def collision(self, attacker):
        if attacker.get_strength() >= self._strength:#attacker has higher strength. If strengths are equal the encounter is won by the attacker.
            self.world._commentator.add_new_comment(attacker.get_symbol() + " ate " + self.get_symbol())
            attacker.position = self.position
            self.world.delete_organism(self)            
        else:#attacker has lower strength 
            self.world._commentator.add_new_comment(self.get_symbol() + " ate " + attacker.get_symbol())
            self.world.delete_organism(attacker)  

    def breed(self):
        try:
            from animals.human import Human
            if not isinstance(self, Human):   #only one instance of Human
                self.world._commentator.add_new_comment("New instance of " + self.get_symbol() + " has been created")
                new_organism = self.get_new_organism_object()
                new_position = self.world.get_not_occupied_position_with_range(self.position, 1)
                new_organism.position.set(new_position)
                self.world.add_organism(new_organism)        
        except GridIsFullException:
            pass

    def get_strength(self):
        return self._strength

    def set_strength(self, strength):
        self.strength = strength