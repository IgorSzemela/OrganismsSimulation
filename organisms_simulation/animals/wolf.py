from world.animal import Animal
from grid.position import Position


class Wolf(Animal):

    def __init__(self, world, position):
        super(Wolf, self).__init__(9, 5, world, position)

    def get_new_organism_object(self):
        return Wolf(self.world, Position())

    def get_symbol(self):
        return "W"
