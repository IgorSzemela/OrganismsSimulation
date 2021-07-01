import math


class Position:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def equals(self, pos):
        return pos.x == self.x and pos.y == self.y

    def set(self, pos):
        self.x = pos.x
        self.y = pos.y   

    def get_distance(self, pos_to_compare):
        return math.sqrt(pow(abs(self.x-pos_to_compare.x),2) + pow(abs(self.y-pos_to_compare.y),2))

    def subtract(self, pos_to_compare):
        return Position(self.x-pos_to_compare.x, self.y-pos_to_compare.y)

    def add(self, pos_to_compare):
        return Position(self.x+pos_to_compare.x, self.y+pos_to_compare.y)