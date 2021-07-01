from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui

from grid.click_menu import ClickMenu
from grid.position import Position
from world.world import World


class GridCell(QPushButton):#one cell on the grid  

    def __init__(self, parent, world: World, x: int, y: int):
        super(GridCell, self).__init__(' ', parent)        
        self.menu = ClickMenu(world, self, self)
        self.clicked.connect(self.action)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self._x = x
        self._y = y
        self.world = world             

    def action(self):
        if self.world.get_organism_at_given_position(Position(self._x,self._y)) is None:
            self.menu.popup(QPoint())
   
    def paintEvent(self, q_paint_event):#Prints symbol of each organism on each cell
        recieved_organism = self.world.get_organism_at_given_position(Position(self._x, self._y))
        if recieved_organism is not None:
            self.setText(recieved_organism.get_symbol())
        else:
            self.setText("")

        super().paintEvent(q_paint_event)

    
