from world.animal import Animal
from plants.sosnowsky_hogweed import SosnowskyHogweed
from grid.position import Position

class CyberSheep(Animal):

    def __init__(self, world, position):
        super(CyberSheep, self).__init__(11, 4, world, position)

    def collision(self, attacker):
        super().collision(attacker)        

    def action(self):
        closest_sos_hogweed = None
        min_distance = 100

        for organism in self.world.get_organisms():#It always moves towards the closest hogweed
            if isinstance(organism, SosnowskyHogweed):
                dist = organism.position.get_distance(self.position)

                if dist < min_distance:
                    closest_sos_hogweed = organism
                    min_distance = dist

        if closest_sos_hogweed is not None:
            direction = closest_sos_hogweed.position.subtract(self.position)

            if direction.y > 0:
                direction.y = 1
            elif direction.y < 0:
                direction.y = -1

            if direction.x > 0:
                direction.x = 1
            elif direction.x < 0:
                direction.x = -1            

            position_to_go = self.position.add(direction)
            possible_defender = self.world.get_organism_at_given_position(position_to_go)

            if possible_defender is not None and possible_defender is not self:
                possible_defender.collision(self)
            else:
                self.position = position_to_go
        else:
            super().action()


    def get_new_organism_object(self):
        return CyberSheep(self.world, Position())

    def get_symbol(self):
        return "C"
   
