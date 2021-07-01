from  world.organism import Organism


class Animal(Organism):

    def __init__(self, strength, initiative, world, position):
        super(Animal, self).__init__(strength, initiative, world, position)

    def collision(self, attacker):
        from animals.human import Human

        if type(self) == type(attacker) and not isinstance(self, Human):#only one Humnan on the grid
            super(Animal, self).breed()
        else:
            super(Animal, self).collision(attacker)

    def action(self):
        position_to_go = self.world.draw_and_get_direction(self.position, 1)
        possible_defender = self.world.get_organism_at_given_position(position_to_go)

        if possible_defender is not self and possible_defender is not None:
            possible_defender.collision(self)
        else:   
            self.position = position_to_go

    

