from grid.position import Position
from world.plant import Plant
from world.animal import Animal


class SosnowskyHogweed(Plant):
    def __init__(self, world, position):
        super(SosnowskyHogweed, self).__init__(10, 0, world, position)

    def collision(self, attacker):
        from animals.cyber_sheep import CyberSheep
        self.world.delete_organism(self)
        if not isinstance(attacker, CyberSheep):#Kills every animal in its immediate neighborhood except cyber-sheep.
            self.world._commentator.add_new_comment("$ ate " + attacker.get_symbol())
            self.world.delete_organism(attacker)        

    def action(self):
        for i in range(0, 200):
            new_direction = self.world.draw_and_get_direction(self.position, 1)
            possible_defender = self.world.get_organism_at_given_position(new_direction)

            from animals.cyber_sheep import CyberSheep
            if possible_defender is not None and isinstance(possible_defender, Animal) and not isinstance(possible_defender, CyberSheep):
                possible_defender.world.delete_organism(possible_defender)       
        super(SosnowskyHogweed, self).action()

    def get_new_organism_object(self):
        return SosnowskyHogweed(self.world, Position())

    def get_symbol(self):
        return "$"

    
    

