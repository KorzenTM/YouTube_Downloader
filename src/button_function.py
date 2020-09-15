from libraries import *
import alerts_window
import youtube_downloader

links = []
quality = []
locations = []


def add_to_list(self, link, save_location, itag):
    if self.link_textbox.text() == "":
        alerts_window.no_link(self)
    elif self.save_location.text() == "":
        alerts_window.no_location(self)
    else:
        links.append(link)
        locations.append(save_location)
        quality.append(itag)
        self.app_status.showMessage("Status: Dodano element do listy pobierania")
        clear(self)


def save_directory(self):
    dialog = QFileDialog()
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    dialog.setWindowTitle("Wybierz folder")
    dialog.setAcceptMode(QFileDialog.AcceptOpen)
    dialog.setFileMode(QFileDialog.DirectoryOnly)
    if dialog.exec_() == QFileDialog.Accepted:
        self.save_location.setText(dialog.selectedFiles()[0])


def check_state_link_textbox(self, link):
    self.app_status.showMessage("Status: Sprawdzanie linku")
    try:
        self.youtube = pytube.YouTube(link)
    except:
        alerts_window.bad_link_warning(self)
    else:
        youtube_downloader.information(self, link)


def download_video(self):
    try:
        youtube_downloader.download(self, locations, links, quality)
    except:
        alerts_window.download_error(self)
    else:
        self.app_status.showMessage("Status: Rozpoczęto pobieranie")


def clear(self):
    self.link_textbox.clear()
    self.if_link_correct.clear()
    self.description.clear()
    self.image_label.clear()
    self.set_format.clear()
    self.save_location.clear()
    self.status.setValue(0)
    self.app_status.showMessage("Status: Oczekiwanie")
