from world.plant import Plant
from grid.position import Position


class Belladonna(Plant):

    def __init__(self, world, position):
        super(Belladonna, self).__init__(99, 0, world, position)

    def collision(self, attacker):#Kills any animal which eats it.
        self.world._commentator.add_new_comment("B ate " + attacker.get_symbol())
        self.world.delete_organism(attacker)
        self.world.delete_organism(self)

    def get_new_organism_object(self):
        return Belladonna(self.world, Position())

    def get_symbol(self):
        return "B"

    
