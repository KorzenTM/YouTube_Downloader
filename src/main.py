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
        
        self.label_hello=QLabel("YouTube Downloader",self)
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
        
        self.link=QLabel("Podaj link do filmu:",self)
        self.link.setAlignment(Qt.AlignLeft)
        self.link.setStyleSheet("font: 20pt Comic Sans MS")
        self.link.resize(700,200)
        self.link.move(10,180)
        
        self.link_textbox=QLineEdit(self)
        self.link_textbox.move(220,180)
        self.link_textbox.resize(415,30)
        self.link_textbox.textChanged.connect(lambda: button_function.check_state_link_textbox(self,self.link_textbox.text()))
        
        self.check_button=QPushButton("Sprawdź",self)
        self.check_button.setEnabled(False)
        self.check_button.resize(100,30)
        self.check_button.move(650,180)
        self.check_button.clicked.connect(lambda: button_function.open_link(self,self.link_textbox.text()))
        self.check_button.setToolTip("Sprawdza, czy to prawidłowe wideo")
        
        self.information=QLabel("Informacje o filmie",self)
        self.information.setAlignment(Qt.AlignLeft)
        self.information.setStyleSheet("font: 15pt Comic Sans MS")
        self.information.resize(400,100)
        self.information.move(250,230)
        
        self.description=QTextEdit(self)
        self.description.setReadOnly(True)
        self.description.setStyleSheet("font: 10pt Comic Sans MS")
        self.description.resize(400,80)
        self.description.move(200,255)
        
        self.format=QLabel("Wybierz format:",self)
        self.format.setAlignment(Qt.AlignLeft)
        self.format.setStyleSheet("font: 15pt Comic Sans MS")
        self.format.resize(400,100)
        self.format.move(620,250)
        
        self.set_format=QComboBox(self)
        self.set_format.setGeometry(620,270,130,25)
        
        self.location=QLabel("Gdzie zapisać plik:",self)
        self.location.setAlignment(Qt.AlignLeft)
        self.location.setStyleSheet("font: 20pt Comic Sans MS")
        self.location.resize(700,100)
        self.location.move(10,350)
        
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
        
        self.download_status=QLabel("Status pobierania",self)
        self.download_status.setAlignment(Qt.AlignLeft)
        self.download_status.setStyleSheet("font: 15pt Comic Sans MS")
        self.download_status.resize(150,100)
        self.download_status.move(200,430)
        
        self.status=QProgressBar(self)
        self.status.setGeometry(50,460,450,25)
        
        self.convert_mp3_check=QCheckBox("Konwersja po pobraniu(mp3)",self)
        self.convert_mp3_check.setGeometry(50,420,250,150)
        self.convert_mp3_check.setStyleSheet("font: 10pt Comic Sans MS")
        
        self.button_download=QPushButton("POBIERZ",self)
        self.button_download.resize(215,50)
        self.button_download.move(535,450)
        self.button_download.setStyleSheet("background-color: #A52A2A")
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
    
if __name__=="__main__":
    
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()

    app.exec_()


