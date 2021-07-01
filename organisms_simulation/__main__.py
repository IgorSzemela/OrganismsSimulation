from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit
from PyQt5 import QtCore
from PyQt5.Qt import Qt

import sys
import pickle
import random

from animals.human import Human
from animals.wolf import Wolf
from animals.sheep import Sheep
from animals.fox import Fox
from animals.turtle import Turtle
from animals.antelope import Antelope
from animals.cyber_sheep import CyberSheep
from plants.grass  import Grass 
from plants.sow_thistle  import SowThistle 
from plants.guarana import Guarana
from plants.belladonna import Belladonna
from plants.sosnowsky_hogweed import SosnowskyHogweed

from grid.grid_cell import GridCell
from grid.position import Position
from world.world import World
from grid.commentator import Commentator


class Grid(QWidget):

    def __init__(self, world: World):
        super(Grid, self).__init__()
        self._world = world
        self.menu_info = QTextEdit(self)
        self.legend = QTextEdit(self)
        self._commentator = Commentator(self)
        world._commentator = self._commentator
        world._grid = self
        self.initUI()
        self.setChildrenFocusPolicy(QtCore.Qt.NoFocus)
       
    def setChildrenFocusPolicy (self, policy):#reads arrowys from keyboard
        def recursiveSetChildFocusPolicy (parentQWidget):
            for childQWidget in parentQWidget.findChildren(QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)
        recursiveSetChildFocusPolicy(self)

    def initUI(self):
        self.setWindowTitle('Igor Szemela 184659')
        self.setGeometry(400, 150, 1200, 900)
        self.setStyleSheet("border:1px solid #4e4e4e; background-color:#D28271")
        self.menu_info.move(60, 20)
        self.menu_info.resize(600, 60)
        self.menu_info.setReadOnly(True)
        self.menu_info.append("arrows - Human move || a - Human's ability activation || space - next round \n"
        "esc - quit the game || s - save game instance || l - load game instance")
        
        self.legend.move(60, 700)
        self.legend.resize(600, 80)
        self.legend.setReadOnly(True)
        self.legend.append("Antelope - A || Belladonna - B || CyberSheep - C || Fox - F || Grass - # ||\n Guarana - G || "
        "Human - H || Sheep - S || SosnowskyHogweed - $ || \n SowThistle - % || Turtle - T || Wolf - W ")

        for i in range(0, dimension_x):#placing cells (buttons) on the grid
            for j in range(0, dimension_y):
                button = GridCell(self, self._world, i, j)   
                button.move(i * 30 + 60, j * 30 + 90)
                button.resize(30, 30)                

        self.show()
                  
    def keyPressEvent(self, q_key_event):
        self._world.user_command = q_key_event.key()
        super().keyPressEvent(q_key_event)
        key_command = self._world.user_command
                  
        if key_command == QtCore.Qt.Key_Up:
            self._world.next_human_turn(1)
        elif key_command == QtCore.Qt.Key_Right:
            self._world.next_human_turn(2)
        elif key_command == QtCore.Qt.Key_Down:
            self._world.next_human_turn(3)
        elif key_command == QtCore.Qt.Key_Left:
            self._world.next_human_turn(4) 
        elif key_command == QtCore.Qt.Key_S:
             self._commentator.add_new_comment("Game is saved!")
             instance_saved = self._world
             with open('prev_instances/saved_instance.txt', 'wb') as i:
                pickle.dump(instance_saved, i)
        elif key_command == QtCore.Qt.Key_L:
            with open('prev_instances/saved_instance.txt', 'rb') as i:
                instance_loaded = pickle.load(i)
            self.close()
            self.Open = Grid(instance_loaded)
            self.Open.show()  
        elif key_command == QtCore.Qt.Key_A:
            human_instance = self._world.get_human()
            human_instance.special_ability()
        elif key_command == QtCore.Qt.Key_Space:
             self._world.make_turn()
        elif key_command == QtCore.Qt.Key_Escape:
             app.quit()
        
        self.repaint()

    def mouseReleaseEvent(self, q_key_event):
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dimension_x=20
    dimension_y=20
    organisms_amount=10
    print("Type 'd' If you would like to load default instance of the game\n"
		 "Type 'n' If you would like to start new game and personalize the gird")
    value = input()

    if value == 'n':
        dimension_x = input("Grid's X dimension: ")
        dimension_y = input("Grid's Y dimension: ")
        organisms_amount = input("Amount of organisms on the grid different than Human (must be less than: {}): ".format(int(dimension_x)*int(dimension_y)-1))
        dimension_x=int(dimension_x)
        dimension_y=int(dimension_y)
        organisms_amount=int(organisms_amount)

    s = World(dimension_x, dimension_y)
    ex = Grid(s)

    s.draw_postition_add_organism(Human(s, Position()))

    for i in range(0, organisms_amount):
        organism_kind =  random.randint(0, 10)
        if organism_kind == 0:            
               s.draw_postition_add_organism(Wolf(s, Position())) 
        elif organism_kind == 1:
               s.draw_postition_add_organism(Sheep(s, Position()))
        elif organism_kind == 2:
               s.draw_postition_add_organism(Fox(s, Position()))
        elif organism_kind == 3:
               s.draw_postition_add_organism(Turtle(s, Position()))
        elif organism_kind == 4:
               s.draw_postition_add_organism(Antelope(s, Position()))
        elif organism_kind == 5:
               s.draw_postition_add_organism(CyberSheep(s, Position()))
        elif organism_kind == 6:
               s.draw_postition_add_organism(Grass(s, Position()))
        elif organism_kind == 7:
               s.draw_postition_add_organism(SowThistle (s, Position()))
        elif organism_kind == 8:
               s.draw_postition_add_organism(Guarana(s, Position()))
        elif organism_kind == 9:
               s.draw_postition_add_organism(Belladonna(s, Position()))
        elif organism_kind == 10:
               s.draw_postition_add_organism(SosnowskyHogweed(s, Position()))   

    ex.repaint()
    sys.exit(app.exec_())
