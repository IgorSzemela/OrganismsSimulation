from world.animal import Animal
from grid.position import Position


class Fox(Animal):

    def __init__(self, world, position):
        super(Fox, self).__init__(3, 7, world, position)

    def action(self):
        possible_defender = None
        position_to_go = None

        for i in range(0, 200):
            position_to_go = self.world.draw_and_get_direction(self.position, 1)
            possible_defender = self.world.get_organism_at_given_position(position_to_go)

            if possible_defender is None or possible_defender.get_strength() <= self._strength:#will never move to a cell occupied by a stronger organism.
                break

        if possible_defender is not None:
            possible_defender.collision(self)
        else:
            self.position = position_to_go

    def get_new_organism_object(self):
        return Fox(self.world, Position())

    def get_symbol(self):
        return "F"

    
