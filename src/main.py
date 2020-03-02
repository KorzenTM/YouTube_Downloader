# -*- coding: utf-8 -*-
"""
Simple application downloading videos from YouTube platform written in Python(PyQt5)
@author: Mateusz Korzeniowski(KorzenTM)
"""
import sys
from PyQt5.QtWidgets import QApplication, QToolButton,QWidget, QMainWindow, QLabel, QPushButton,QFileDialog ,QMessageBox, QDesktopWidget, QLineEdit, QFileSystemModel, QTreeView, QVBoxLayout
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt #ma wiele atrybutów do widgetow
import urllib

class MainWindow(QMainWindow):
    def __init__(self, *args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        
        self.setWindowTitle("YouTube Video Downloader by KorzenTM")
        #center window on screen(it is not working)
        #self.center()
        self.resize(800,600)
        self.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
        
        label_hello=QLabel("Witaj w aplikacji YouTube Downloader",self)
        label_hello.setAlignment(Qt.AlignCenter)
        label_hello.setStyleSheet("font: 30pt Comic Sans MS")
        label_hello.resize(800,100)
        label_hello.move(0,10)
        
        logo=QLabel(self)
        pixmap=QPixmap("resources/img/logo_yt.png")
        scaled_pix=pixmap.scaled(200,200,Qt.KeepAspectRatio,Qt.FastTransformation)
        logo.setPixmap(scaled_pix)
        logo.resize(200,200)
        logo.move(10,450)
        
        label_1=QLabel("Podaj link do filmu:",self)
        label_1.setAlignment(Qt.AlignLeft)
        label_1.setStyleSheet("font: 20pt Comic Sans MS")
        label_1.resize(700,250)
        label_1.move(10,250)
        link_textbox=QLineEdit(self)
        link_textbox.move(220,250)
        link_textbox.resize(415,30)
        check_button=QPushButton("Sprawdź",self)
        check_button.resize(100,30)
        check_button.move(650,250)
        check_button.setToolTip("Sprawdza, czy to prawidłowe wideo")
        
        label_2=QLabel("Gdzie zapisać plik:",self)
        label_2.setAlignment(Qt.AlignLeft)
        label_2.setStyleSheet("font: 20pt Comic Sans MS")
        label_2.resize(700,100)
        label_2.move(10,350)
        save_location=QLineEdit(self)
        save_location.resize(300,30)
        save_location.move(220,350)
        button_browse=QPushButton("Przeglądaj",self)
        button_browse.resize(100,30)
        button_browse.move(535,350)
        button_browse.setToolTip("Przegląda dysk")
        button_open_dir=QPushButton("Otwórz",self)
        button_open_dir.resize(100,30)
        button_open_dir.move(650,350)
        button_open_dir.setToolTip("Otwiera wybrany folder")
        
        button_help=QPushButton("Wsparcie techniczne",self)
        button_help.resize(100,32)
        button_help.move(540,550)
        button_help.setToolTip("Problem? Skontaktuj się ze mną.")
        button_quit=QPushButton("Zamknij aplikację",self)
        button_quit.clicked.connect(QApplication.instance().quit)
        button_quit.resize(100,32)
        button_quit.move(650,550)
        button_quit.setToolTip("Zamyka aplikację")
        
        
    
        
        
    
        
    def center(self):
        #geometry of the main window
        qr=self.frameGeometry()
        #center point of screen
        cp=QDesktopWidget().availableGeometry().center()
        #move rectangle's center point to screen's center poit
        qr.moveCenter(cp)
        #top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())
app=QApplication(sys.argv)

window=MainWindow()
window.show()

app.exec_()


