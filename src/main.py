# -*- coding: utf-8 -*-
"""
Simple application downloading videos from YouTube platform written in Python(PyQt5)
@author: Mateusz Korzeniowski(KorzenTM)
"""
from importing_modules import *
import button_function

class MainWindow(QMainWindow):
    def __init__(self, *args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        
        self.setWindowTitle("YouTube Video Downloader by KorzenTM")
        #center window on screen(it is not working)
        #self.center()
        self.resize(800,600)
        self.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
        
        self.label_hello=QLabel("Witaj w aplikacji YouTube Downloader",self)
        self.label_hello.setAlignment(Qt.AlignCenter)
        self.label_hello.setStyleSheet("font: 30pt Comic Sans MS")
        self.label_hello.resize(800,100)
        self.label_hello.move(0,10)
        
        self.logo=QLabel(self)
        self.pixmap=QPixmap("resources/img/logo_yt.png")
        self.scaled_pix=self.pixmap.scaled(200,200,Qt.KeepAspectRatio,Qt.FastTransformation)
        self.logo.setPixmap(self.scaled_pix)
        self.logo.resize(200,200)
        self.logo.move(10,450)
        
        self.label_1=QLabel("Podaj link do filmu:",self)
        self.label_1.setAlignment(Qt.AlignLeft)
        self.label_1.setStyleSheet("font: 20pt Comic Sans MS")
        self.label_1.resize(700,250)
        self.label_1.move(10,250)
        self.link_textbox=QLineEdit(self)
        self.link_textbox.move(220,250)
        self.link_textbox.resize(415,30)
        self.check_button=QPushButton("Sprawdź",self)
        self.check_button.resize(100,30)
        self.check_button.move(650,250)
        self.check_button.clicked.connect(lambda: button_function.open_link(self,self.link_textbox.text()))
        self.check_button.setToolTip("Sprawdza, czy to prawidłowe wideo")
        
        self.label_2=QLabel("Gdzie zapisać plik:",self)
        self.label_2.setAlignment(Qt.AlignLeft)
        self.label_2.setStyleSheet("font: 20pt Comic Sans MS")
        self.label_2.resize(700,100)
        self.label_2.move(10,350)
        self.save_location=QLineEdit(self)
        self.save_location.resize(300,30)
        self.save_location.move(220,350)
        self.button_browse=QPushButton("Przeglądaj",self)
        self.button_browse.resize(100,30)
        self.button_browse.move(535,350)
        self.button_browse.clicked.connect(lambda: button_function.save_directory(self))
        self.button_browse.setToolTip("Przegląda dysk")
        self.button_open_dir=QPushButton("Otwórz",self)
        self.button_open_dir.resize(100,30)
        self.button_open_dir.move(650,350)
        self.button_open_dir.clicked.connect(lambda: button_function.open_directory(self,self.save_location.text()))
        self.button_open_dir.setToolTip("Otwiera wybrany folder")
        
        self.button_download=QPushButton("POBIERZ",self)
        self.button_download.resize(200,50)
        self.button_download.move(300,450)
        self.button_download.clicked.connect(lambda: button_function.download_video(self, self.save_location.text(),self.link_textbox.text()))
        
        self.button_help=QPushButton("Wsparcie techniczne",self)
        self.button_help.resize(100,32)
        self.button_help.move(540,550)
        self.button_help.setToolTip("Problem? Skontaktuj się ze mną.")
        
        self.button_quit=QPushButton("Zamknij aplikację",self)
        self.button_quit.clicked.connect(QApplication.instance().quit)
        self.button_quit.resize(100,32)
        self.button_quit.move(650,550)
        self.button_quit.setToolTip("Zamyka aplikację")
                
    def center(self):
        #geometry of the main window
        qr=self.frameGeometry()
        #center point of screen
        cp=QDesktopWidget().availableGeometry().center()
        #move rectangle's center point to screen's center poit
        qr.moveCenter(cp)
        #top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())
   
if __name__=="__main__":
    
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()

    app.exec_()


