#export DISPLAY=:0.0 polecenie do Xming by zadziałał tryb okienkowy
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt #ma wiele atrybutów do widgetow

class MainWindow(QMainWindow):
    def __init__(self, *args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        
        self.setWindowTitle("YouTube Video Downloader by KorzenTM")
        #center window on screen(it is not working)
        #self.center()
        self.resize(800,600)
        self.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
        
        label=QLabel("YouTube Downloader",self)
        label.setAlignment(Qt.AlignLeft)
        label.move(0,500)
        
        logo=QLabel(self)
        pixmap=QPixmap("resources/img/668px-Logo_of_YouTube_(2013-2015).svg.png")
        scaled_pix=pixmap.scaled(100,100,Qt.KeepAspectRatio,Qt.FastTransformation)
        logo.setPixmap(scaled_pix)
        logo.resize(150,150)
        logo.move(650,10)
        
        button=QPushButton("Zamknij aplikację",self)
        button.clicked.connect(QApplication.instance().quit)
        button.resize(100,32)
        button.move(650,550)
        
    def on_button_clicked(self):
        alert=QMessageBox()
        alert.setText("You clicked the button!")
        alert.exec_()

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




