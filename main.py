# Imported UI Files
from MainWindow import *
import AppIcons_rc

# Needed Libraries
import os
import sys
from PySide2 import QtCore, QtGui, QtWidgets

def Display_Window():
    app = QtWidgets.QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Display_Window()
else:
    exit(1)