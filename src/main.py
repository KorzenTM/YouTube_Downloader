# -*- coding: utf-8 -*-
"""
Simple application downloading videos from YouTube platform written in Python(PyQt5)
@author: Mateusz Korzeniowski(KorzenTM)
Version: 1.0
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
        self.setStyleSheet("QMainWindow {background-color: #6495ED}")
        self.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
        
        self.styleSheet="""
        QTextEdit{
            background-color:yellow;
        }
        """
        
        #backgrounds
        self.top_background=QLabel(self)
        self.top_background.resize(780,100)
        self.top_background.move(10,10)
        self.top_background.setStyleSheet("background-color: #B22222")
        self.middle_background=QLabel(self)
        self.middle_background.resize(780,260)
        self.middle_background.move(10,150)
        self.middle_background.setStyleSheet("background-color: #D3D3D3")
        self.download_background=QLabel(self)
        self.download_background.resize(780,100)
        self.download_background.move(10,420)
        self.download_background.setStyleSheet("background-color: #D3D3D3")
        self.end_background=QLabel(self)
        self.end_background.resize(230,50)
        self.end_background.move(530,540)
        self.end_background.setStyleSheet("background-color: #708090")
        
        self.label_hello=QLabel("YouTube Downloader",self)
        self.label_hello.setAlignment(Qt.AlignCenter|Qt.AlignRight)
        self.label_hello.setStyleSheet("font: 30pt Times New Roman")
        self.label_hello.resize(400,100)
        self.label_hello.move(0,10)
        
        self.logo=QLabel(self)
        self.pixmap=QPixmap("resources/img/logo_yt.png")
        self.scaled_pix=self.pixmap.scaled(200,200,Qt.KeepAspectRatio,Qt.FastTransformation)
        self.logo.setPixmap(self.scaled_pix)
        self.logo.resize(200,200)
        self.logo.move(550,-45)
        
        self.link=QLabel("Video Url:",self)
        self.link.setAlignment(Qt.AlignLeft)
        self.link.setStyleSheet("font: 20pt Times New Roman")
        self.link.resize(700,200)
        self.link.move(20,183)
        
        self.link_textbox=QLineEdit(self)
        self.link_textbox.move(130,180)
        self.link_textbox.resize(500,30)
        self.link_textbox.setPlaceholderText("Example:http://www.youtube.com/watch?v=ecsCrOEYl7c")
        self.link_textbox.textChanged.connect(lambda: button_function.check_state_link_textbox(self,self.link_textbox.text()))
        
        self.reset_button=QPushButton("Zresetuj",self)
        self.reset_button.setEnabled(False)
        self.reset_button.resize(100,30)
        self.reset_button.move(650,180)
        self.reset_button.setStyleSheet("background-color: #800000")
        self.reset_button.clicked.connect(lambda: button_function.data_reset(self))
        self.reset_button.setToolTip("Sprawdza, czy to prawidłowe wideo")
        
        self.image_label=QLabel(self)
        self.image_label.resize(180,125)
        self.image_label.move(600,220)
        
        self.information=QLabel("Informacje o filmie",self)
        self.information.setAlignment(Qt.AlignLeft)
        self.information.setStyleSheet("font: 15pt Times New Roman")
        self.information.resize(400,100)
        self.information.move(200,220)
        
        self.description=QTextEdit(self)
        self.description.setReadOnly(True)
        self.description.setStyleSheet("font: 10pt Times New Roman")
        self.description.resize(510,120)
        self.description.move(20,240)
        
        self.format=QLabel("Jakość:",self)
        self.format.setAlignment(Qt.AlignLeft)
        self.format.setStyleSheet("font: 15pt Times New Roman")
        self.format.resize(400,100)
        self.format.move(685,345)
        
        self.set_format=QComboBox(self)
        self.set_format.setGeometry(650,370,130,30)
        
        self.location=QLabel("Zapisz do:",self)
        self.location.setAlignment(Qt.AlignLeft)
        self.location.setStyleSheet("font: 20pt Times New Roman")
        self.location.resize(700,200)
        self.location.move(20,370)
        
        self.save_location=QLineEdit(self)
        self.save_location.resize(400,30)
        self.save_location.move(130,370)
        
        self.button_browse=QPushButton("Przeglądaj",self)
        self.button_browse.resize(100,30)
        self.button_browse.move(535,370)
        self.button_browse.clicked.connect(lambda: button_function.save_directory(self))
        self.button_browse.setToolTip("Przegląda dysk")
        
        self.download_status=QLabel("Status pobierania",self)
        self.download_status.setAlignment(Qt.AlignLeft)
        self.download_status.setStyleSheet("font: 15pt Times New Roman")
        self.download_status.resize(150,100)
        self.download_status.move(200,430)
        
        self.status=QProgressBar(self)
        self.status.setGeometry(50,460,450,25)
        
        self.convert_mp3_check=QCheckBox("Konwersja po pobraniu(mp3)",self)
        self.convert_mp3_check.setGeometry(50,420,250,150)
        self.convert_mp3_check.setStyleSheet("font: 10pt Times New Roman")
        
        self.button_download=QPushButton("POBIERZ",self)
        self.button_download.resize(215,50)
        self.button_download.move(535,450)
        self.button_download.setStyleSheet("background-color: #32CD32")
        self.button_download.clicked.connect(lambda: button_function.download_video(self, self.save_location.text(),self.link_textbox.text()))
        
        self.button_help=QPushButton("Wsparcie techniczne",self)
        self.button_help.resize(100,32)
        self.button_help.move(540,550)
        self.button_help.setStyleSheet("background-color: #1E90FF")
        self.button_help.setToolTip("Problem? Skontaktuj się ze mną.")
        
        self.button_quit=QPushButton("Zamknij aplikację",self)
        self.button_quit.clicked.connect(QApplication.instance().quit)
        self.button_quit.resize(100,32)
        self.button_quit.move(650,550)
        self.button_quit.setStyleSheet("background-color: #8B0000")
        self.button_quit.setToolTip("Zamyka aplikację")
    
if __name__=="__main__":
    
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()

    app.exec_()


