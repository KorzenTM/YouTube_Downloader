from libraries import *
import alerts
import yt_download


def bad_link_warning(self):
    self.pixmap_2 = QPixmap("resources/icons/wrong.png")
    self.scaled_pix_2 = self.pixmap_2.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
    self.wrong_pic.setPixmap(self.scaled_pix_2)
    self.app_status.showMessage("Nieprawidłowy link")
    self.loading = QMovie("resources/gif/yt_loading.gif")
    self.loading.setScaledSize(QSize(240, 120))
    self.image_label.setMovie(self.loading)
    self.loading.start()
    self.link_textbox.textChanged


def clear(self):
    if self.link_textbox.text() == "":
        self.warning.clear()
        self.wrong_pic.clear()
        self.description.clear()
        self.image_label.clear()
        self.set_format.clear()
        self.save_location.clear()


def download_video(self, location, link):
    if self.link_textbox.text() == "":
        alerts.no_link(self)
    if self.save_location.text() == "":
        alerts.no_location(self)
    else:
        yt_download.download(self, link, location)


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
        bad_link_warning(self)
    else:
        yt_download.information(self, link)
