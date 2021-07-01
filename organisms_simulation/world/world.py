import random

from grid.position import Position
from grid.grid_is_full_exception import GridIsFullException
import world.organism as organism

class World:

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.user_command = ''
        self._organisms = []

    def __getstate__(self):#excluding _commentator and _grid from pickling
        attributes = self.__dict__.copy()
        del attributes['_commentator']
        del attributes['_grid']
        return attributes

    def make_turn(self):
        self._organisms.sort(key = lambda x: (x.initiative,x.age), reverse=True)#sorting organisms by initiative and age

        for i in range(len(self._organisms)):
            if i >= len(self._organisms):
                break

            from animals.human import Human
            self._organisms[i].age+=1#increasing age of each  organism
            if self._organisms[i] is not None and isinstance(self._organisms[i], Human):
                human_instance = self.get_human()
                if human_instance.ability_round_counter > 0:
                    human_instance.special_ability()
            elif self._organisms[i] is not None:
                self._organisms[i].action()

    def next_human_turn(self, direction_choice):
        human_instance = self.get_human()
        if human_instance is not None:
            human_instance.action(direction_choice)
        
    def get_human(self) -> organism:
        from animals.human import Human
        for i in range(0, len(self._organisms)):
            if isinstance(self._organisms[i], Human):          
                return self._organisms[i]
        return None

    def add_organism(self, organism: organism):
        self._organisms.append(organism)

    def delete_organism(self, organism: organism):
        self._organisms.remove(organism)

    def draw_postition_add_organism(self, organism: organism):
        self.draw_not_occupied_position_on_whole_grid(organism)
        self._organisms.append(organism)  

    def get_organism_at_given_position(self, p) -> organism:
        for i in range(0, len(self._organisms)):
            if self._organisms[i].position.equals(p):
                return self._organisms[i]
        return None

    def get_organisms(self):
        return self._organisms

    def get_not_occupied_position_with_range(self, position, range):
        i = 0
        while True:
            new_position = self.draw_and_get_direction(position, range)
            if self.get_organism_at_given_position(new_position) is None:
                return new_position
            i += 1
            if i >= 200:
                raise GridIsFullException()    

    def draw_and_get_direction(self, position, range):
        while True:
            position_to_go = Position()
            position_to_go.set(position)
            direction = random.randint(0, 7)
            if direction == 0:
                position_to_go.y = position_to_go.y - range
                position_to_go.x = position_to_go.x - range
            elif direction == 1:
                position_to_go.x = position_to_go.x - range               
            elif direction == 2:
                position_to_go.y = position_to_go.y + range
                position_to_go.x = position_to_go.x - range
            elif direction == 3:
                position_to_go.y = position_to_go.y + range
                position_to_go.x = position_to_go.x - range
            elif direction == 4:
                position_to_go.y = position_to_go.y + range
            elif direction == 5:
                position_to_go.x = position_to_go.x + range               
            elif direction == 6:
                 position_to_go.y = position_to_go.y - range
                 position_to_go.x = position_to_go.x + range
            elif direction == 7:
                 position_to_go.y = position_to_go.y - range                

            if self.if_in_grid(position_to_go):
                return position_to_go
   
    def draw_not_occupied_position_on_whole_grid(self, organism):
        check = True
        while check is True:
            temp = Position()
            x = random.randint(0, self._height-1)
            y = random.randint(0, self._width-1)            
            temp.set(Position(x, y))
            for i in range(0, len(self._organisms)):
                if self._organisms[i].position.equals(temp):
                    check = False

            if check is False:
                check = True
            else:
                check = False
                organism.position.set_x(y)
                organism.position.set_y(x)

    def if_in_grid(self, p):
        return p.y >= 0 and p.y < self._height and p.x >= 0 and p.x < self._width        


    