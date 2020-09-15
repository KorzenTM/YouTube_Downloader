from libraries import *
import alerts_window
import yt_download


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
        yt_download.information(self, link)


def download_video(self, location, link):
    if self.link_textbox.text() == "":
        alerts_window.no_link(self)
    if self.save_location.text() == "":
        alerts_window.no_location(self)
    else:
        yt_download.download(self, link, location)


def clear(self):
    self.link_textbox.clear()
    self.wrong_pic.clear()
    self.description.clear()
    self.image_label.clear()
    self.set_format.clear()
    self.save_location.clear()
    self.status.setValue(0)
    self.app_status.showMessage("Status: Oczekiwanie")
