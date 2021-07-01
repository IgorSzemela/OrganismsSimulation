from world.animal import Animal
from grid.position import Position


class Sheep(Animal):

    def __init__(self, world, position):
        super(Sheep, self).__init__(4, 4, world, position)

    def get_new_organism_object(self):
        return Sheep(self.world, Position())

    def get_symbol(self):
        return "S"
