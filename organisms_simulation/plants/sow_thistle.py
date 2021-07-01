from grid.position import Position
from world.plant import Plant


class SowThistle (Plant):

    def __init__(self, world, position):
        super(SowThistle , self).__init__(0, 0, world, position)

    def action(self):
        super(SowThistle , self).action()#Performs 3 attempts at spreading in each turn
        super(SowThistle , self).action()
        super(SowThistle , self).action()

    def get_new_organism_object(self):
        return SowThistle (self.world, Position())

    def get_symbol(self):
        return "%"

    
