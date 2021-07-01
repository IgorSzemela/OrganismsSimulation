from grid.position import Position
from world.plant import Plant


class Grass(Plant):

    def __init__(self, world, position):
        super(Grass, self).__init__(0, 0, world, position)

    def get_new_organism_object(self):
        return Grass(self.world, Position())

    def get_symbol(self):
        return "#"

