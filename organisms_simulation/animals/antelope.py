import random

from world.animal import Animal
from grid.position import Position


class Antelope(Animal):

    def __init__(self, world, position):
        super(Antelope, self).__init__(4, 4, world, position)

    def collision(self, attacker):
        if self is not attacker:
            if random.randint(0, 1) == 1:#Has 50% chance to escape from fight
                tmp = Position(self.position.x, self.position.y)
                self.position = attacker.position
                attacker.position = tmp 
            else:
                super(Antelope, self).collision(attacker)

    def action(self):
        position_to_go = self.world.draw_and_get_direction(self.position, 2)#Has wider range of movement - 2 
        possible_defender = self.world.get_organism_at_given_position(position_to_go)

        if possible_defender is not None:
            possible_defender.collision(self)
        else:
            self.position = position_to_go

    def get_new_organism_object(self):
        return Antelope(self.world, Position())

    def get_symbol(self):
        return "A"

    

    
