from importing_modules import *


def download_video(self,location,link):
    ydl_opts = {}
    os.chdir(location)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        msgbox=QMessageBox.information(self,"Potwierdzenie","Pobieranie zostało zakończone")
        
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