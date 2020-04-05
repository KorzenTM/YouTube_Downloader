# -*- coding: utf-8 -*-
"""
Simple application downloading videos from YouTube platform written in Python(PyQt5)
@author: Mateusz Korzeniowski(KorzenTM)
Version: 1.0
"""

from main_window import *
from libraries import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
