from importing_modules import *


        
def download_video(self,location,link):
    if self.link_textbox.text()=="":
        msg=QMessageBox()
        msg.setWindowTitle("Ostrzeżenie")
        msg.setText("Nie podałeś linku")
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()
    if self.save_location.text()=="":
        msg=QMessageBox()
        msg.setWindowTitle("Ostrzeżenie")
        msg.setText("Nie podałeś lokalizacji")
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()
    else:
        def percent(tem,total):
            perc=(float(tem)/float(total))*float(100)
            return perc 

        def progress_function(chunk,file_handle,bytes_remaining):
            progres=round((1-bytes_remaining/self.video.filesize)*100, 3)
            self.status.setValue(progres)
        
        self.video_url =link # paste here your Youube videos' url
        self.youtube = pytube.YouTube(self.video_url,on_progress_callback=progress_function)
        self.video = self.youtube.streams.first()
        self.video.download(location)
        
        
        
        msg=QMessageBox()
        msg.setWindowTitle("Informacja")
        msg.setText("Pobieranie zostało zakończone")
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()
         
def open_directory(self,location):
    
    #print(self.save_location.text())
    webbrowser.open(location)

def save_directory(self):
    dialog = QFileDialog()
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    dialog.setWindowTitle("Wybierz folder")
    dialog.setAcceptMode(QFileDialog.AcceptOpen)
    #dialog.setNameFilter(nameFilter)
    dialog.setFileMode(QFileDialog.DirectoryOnly)
    if dialog.exec_() == QFileDialog.Accepted:
        self.save_location.setText(dialog.selectedFiles()[0])

def open_link(self,link):
    # print(self.link_textbox.text())
    webbrowser.open(link)

def center(self):
        #geometry of the main window
        qr=self.frameGeometry()
        #center point of screen
        cp=QDesktopWidget().availableGeometry().center()
        #move rectangle's center point to screen's center poit
        qr.moveCenter(cp)
        #top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())