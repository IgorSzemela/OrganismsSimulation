from world.organism import Organism
import random


class Plant(Organism):

    def __init__(self, strength, initiative, world, position):
        super(Plant, self).__init__(strength, initiative, world, position)

    def collision(self, attacker):
        super(Plant, self).collision(attacker)

    def action(self):
        if random.randint(0, 19) == 1:# probability to sow 5%
            self.breed()         

    
