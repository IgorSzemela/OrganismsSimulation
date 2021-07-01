from world.animal import Animal
from grid.position import Position

import random

class Human(Animal):

    def __init__(self, world, position):
        super(Human, self).__init__(5, 4, world, position)
        self.range = 1
        self.ability_round_counter = 0
    
    def action(self, direction_choice):
        if self.ability_round_counter > 0:
            self.special_ability()
       
        position_to_go = self.get_human_new_position(direction_choice, self.range)
        if position_to_go is not None:
            self.world._organisms.sort(key = lambda x: (x.initiative,x.age), reverse=True)#sorting organisms by initiative and age

            for i in range(len(self.world._organisms)):
                self.world._organisms[i].age+=1

            possible_defender = self.world.get_organism_at_given_position(position_to_go)

            if possible_defender is not None:
                possible_defender.collision(self)
            else:
                self.position = position_to_go

    def get_human_new_position(self, direction_choice, range):  
            position_to_go = Position()
            position_to_go.set(self.position)
            if direction_choice == 1:#up
                position_to_go.y = position_to_go.y - range
            elif direction_choice == 2:#right
                position_to_go.x = position_to_go.x + range
            elif direction_choice == 3:#down
                position_to_go.y = position_to_go.y + range
            elif direction_choice == 4:#left
                position_to_go.x = position_to_go.x - range      
                
            if self.world.if_in_grid(position_to_go):
                return position_to_go

    def special_ability(self):#Antelope's speed is choosen special ability
        self.ability_round_counter += 1

        if self.ability_round_counter >= 1 and self.ability_round_counter <= 4:#Human's movement range is 2 for 3 rounds
            self.range = 2
            self.world._commentator.add_new_comment("ability active, human range: " + str(self.range))           
        elif self.ability_round_counter >=5 and self.ability_round_counter <= 6:# In next 2 rounds probability that he moves by 2 cells is 50%
            if random.randint(0, 2) == 1:
                self.range = 2
            else:
                self.range = 1
            self.world._commentator.add_new_comment("ability active, human range: " + str(self.range))
        elif self.ability_round_counter >=7 and self.ability_round_counter <= 11: #the special ability is turned off and cannot be activated for the next 5 rounds.
             self.range = 1
             self.world._commentator.add_new_comment("ability cannot be activated")
        elif self.ability_round_counter > 11:
            self.ability_round_counter = 0

    def get_symbol(self):
        return "H"





            
    