from grid.position import Position
from world.plant import Plant


class Guarana(Plant):

    def __init__(self, world, position):
        super(Guarana, self).__init__(0, 0, world, position)

    def collision(self, attacker):#Strength of the animal which ate guarana is permanently increased by 3.
        attacker._strength += 3
        self.world._commentator.add_new_comment(attacker.get_symbol() + " strenght increased by 3")
        super(Guarana, self).collision(attacker)

    def get_new_organism_object(self):
        return Guarana(self.world, Position())

    def get_symbol(self):
        return "G"

    