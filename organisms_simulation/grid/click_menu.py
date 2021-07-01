from PyQt5.QtWidgets import QMenu, QAction, QWidget, QGridLayout, QMenuBar
from PyQt5 import QtCore

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

from world.world import World
from grid.position import Position

class ClickMenu(QMenu):

    def __init__(self, world: World, orgButton, *__args):
        super().__init__(*__args)
        self.orgButton = orgButton
        self.world = world       
        self.add_menu_option()

    def add_menu_option(self):
        layout = QGridLayout(self)
        menu_bar = QMenuBar()

        filemenu = menu_bar.addMenu('Add Organism')
        filemenu.triggered.connect(self.actionClicked)
        filemenu.addAction(QAction('Wolf', self))
        filemenu.addAction(QAction('Sheep', self))
        filemenu.addAction(QAction('Fox', self))
        filemenu.addAction(QAction('Turtle', self))
        filemenu.addAction(QAction('Antelope', self))
        filemenu.addAction(QAction('CyberSheep', self))
        filemenu.addAction(QAction('Grass', self))
        filemenu.addAction(QAction('SowThistle', self))
        filemenu.addAction(QAction('Guarana', self))
        filemenu.addAction(QAction('Belladonna', self))
        filemenu.addAction(QAction('SosnowskyHogweed', self))

        layout.addWidget(menu_bar)   

    @QtCore.pyqtSlot(QAction)
    def actionClicked(self, action):     
        self.world._commentator.add_new_comment(action.text() + " added by clicking on cell")
        
        if action.text() == 'Wolf':            
               self.world.add_organism(Wolf(self.world, Position(self.orgButton._x,self.orgButton._y)))  
        elif action.text() == 'Sheep':
               self.world.add_organism(Sheep(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'Fox':
               self.world.add_organism(Fox(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'Turtle':
               self.world.add_organism(Turtle(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'Antelope':
               self.world.add_organism(Antelope(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'CyberSheep':
               self.world.add_organism(CyberSheep(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'Grass':
               self.world.add_organism(Grass(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'SowThistle':
               self.world.add_organism(SowThistle(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'Guarana':
               self.world.add_organism(Guarana(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'Belladonna':
               self.world.add_organism(Belladonna(self.world, Position(self.orgButton._x,self.orgButton._y)))
        elif action.text() == 'SosnowskyHogweed':
               self.world.add_organism(SosnowskyHogweed(self.world, Position(self.orgButton._x,self.orgButton._y)))

        self.setVisible(False)
        self.world._grid.mouseReleaseEvent(QWidget)#refreshing grid after adding new organism by clicking