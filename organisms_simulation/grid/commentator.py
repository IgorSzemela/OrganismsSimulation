from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit

class Commentator(QTextEdit):
    def __init__(self, widget : QWidget):
        super(Commentator, self).__init__(widget)
        self.move(730, 90)
        self.resize(400, 600)
        self.setReadOnly(True)

    def add_new_comment(self, new_comment):
       self.append(new_comment)

     