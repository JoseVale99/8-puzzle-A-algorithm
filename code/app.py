from PyQt5.QtWidgets import (QApplication)
from controller.ControllerApp import PuzzleView
# from style.style import style
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    puzzleapp = PuzzleView()
    # login.setStyleSheet(style)
    puzzleapp.show()
    sys.exit(app.exec_())