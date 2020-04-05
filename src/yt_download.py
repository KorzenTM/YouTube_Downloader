from libraries import *
import alerts
import audio_converter

def download(self, link, location):
    def progress_function(chunk, file_handle, bytes_remaining):
        progres = round((1 - bytes_remaining / self.video.filesize) * 100)
        self.status.setValue(progres)

    self.youtube = pytube.YouTube(link, on_progress_callback=progress_function)
    self.video = self.youtube.streams.get_by_itag(self.set_format.itemData(self.set_format.currentIndex()))
    self.app_status.showMessage("Status: Pobieranie")
    try:
        self.video.download(location)
    except:
        alerts.download_error()
    else:
        if self.convert_mp3_check.isChecked():
            audio_converter.converter(self, location, self.video.default_filename)
        else:
            self.app_status.showMessage("Status: Pobieranie Zakończone")
            alerts.download_finished_window()
        self.app_status.showMessage("Status: Oczekiwanie")


def information(self, link):
    try:
        self.video = self.youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    except:
        alerts.information_error()
    else:
        self.pixmap_2 = QPixmap("resources/icons/check.png")
        self.scaled_pix_2 = self.pixmap_2.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.wrong_pic.setPixmap(self.scaled_pix_2)
        self.app_status.showMessage("Prawidłowy link!")
        self.description.setText("Tytuł: %s\n\nAutor: %s\n\nOpis: %s" % (self.youtube.title, self.youtube.author, self.youtube.description))
        tag = ""
        for i in self.video:
            tag = re.split(r" itag=\"|\" mime_type", str(i))
            temp = (str(i).split()[2].split("=")[1].split("/")[1] + " " + str(i).split()[3].split("=")[1]).replace('"',"").upper()
            self.set_format.addItem(temp, int(tag[1]))
        url = pytube.YouTube(link).thumbnail_url
        data = urllib.request.urlopen(url).read()
        self.thumb = QPixmap()
        self.thumb.loadFromData(data)
        self.scaled = self.thumb.scaled(240, 120, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_label.setPixmap(self.scaled)