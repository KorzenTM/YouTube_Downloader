from libraries import *
import alerts_window
import audio_converter_window
import button_function


def information(self, link):
    try:
        self.video = self.youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    except:
        alerts_window.information_error()
    else:
        self.pixmap_2 = QPixmap("resources/icons/check.png")
        self.scaled_pix_2 = self.pixmap_2.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.wrong_pic.setPixmap(self.scaled_pix_2)
        self.app_status.showMessage("Prawidłowy link!")
        self.description.setText(
            "Tytuł: %s\n\nAutor: %s\n\nOpis: %s" % (self.youtube.title, self.youtube.author, self.youtube.description))
        tag = ""
        for i in self.video:
            tag = re.split(r" itag=\"|\" mime_type", str(i))
            temp = (str(i).split()[2].split("=")[1].split("/")[1] + " " + str(i).split()[3].split("=")[1]).replace('"',
                                                                                                                   "").upper()
            self.set_format.addItem(temp, int(tag[1]))
        url = pytube.YouTube(link).thumbnail_url
        data = urllib.request.urlopen(url).read()
        self.thumb = QPixmap()
        self.thumb.loadFromData(data)
        self.scaled = self.thumb.scaled(240, 120, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_label.setPixmap(self.scaled)


def download(self, link, location):
    itag = self.set_format.itemData(self.set_format.currentIndex())
    video = pytube.YouTube(link)
    stream = video.streams.get_by_itag(itag)
    default_filename = stream.default_filename
    file_location = str(location) + str("/") + str(default_filename.split('.')[0]) + str(".mp4")
    if Path(file_location).is_file():
        self.app_status.showMessage("Status: Plik istnieje")
        alerts_window.file_exist(self, location, default_filename)
    else:
        self.app_status.showMessage("Status: Pobieranie")
        video_download(self, link, location, default_filename)


def video_download(self, link, location, default_filename):
    def progress_function(percent):
        if percent != self.status.value():
            print(percent)
            self.status.setValue(percent)
            if percent == 100.0:
                end_download(self, location, default_filename)

    itag = self.set_format.itemData(self.set_format.currentIndex())
    self.downloader = Downloader()
    self.downloader.processSignal.connect(progress_function)
    self.downloader.download_video(link, location, itag)


class Downloader(QThread):
    processSignal = pyqtSignal(float)

    def __init__(self, parent = None):
        super(Downloader, self).__init__()
        self.path = None
        self.url = None
        self.video = None
        self.stream = None
        self.itag = None

    def download_video(self, url, path, itag):
        self.path = path
        self.url = url
        self.itag = itag

        self.start()

    def run(self):
        try:
            self.video = pytube.YouTube(self.url)
        except:
            alerts_window.download_error(self)
        else:
            self.video.register_on_progress_callback(self.return_progress)
            self.stream = self.video.streams.get_by_itag(self.itag)
            self.stream.download(self.path)

    def return_progress(self, stream, chunk, bytes_remaining):
        percentage = round((1 - bytes_remaining / self.stream.filesize) * 100, 4)
        self.processSignal.emit(percentage)


def end_download(self, location, default_filename):
    if self.convert_mp3_check.isChecked():
        self.app_status.showMessage("Status: Konwersja")
        audio_converter_window.converter(self, location, default_filename)
        button_function.clear(self)
    else:
        self.app_status.showMessage("Status: Pobieranie Zakończone")
        alerts_window.download_finished_window(self)
        button_function.clear(self)
    self.app_status.showMessage("Status: Oczekiwanie")










