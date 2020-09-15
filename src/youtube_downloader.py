from libraries import *
import alerts_window
import audio_converter_window
import button_function

filenames = []

def information(self, link):
    try:
        self.video = self.youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
    except:
        alerts_window.information_error()
    else:
        self.pixmap_2 = QPixmap("resources/icons/check.png")
        self.scaled_pix_2 = self.pixmap_2.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.if_link_correct.setPixmap(self.scaled_pix_2)
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


def download(self, location = None, links = None, quality = None):
    if quality is None:
        quality = []
    if links is None:
        links = []
    if location is None:
        location = []

    itag = self.set_format.itemData(self.set_format.currentIndex())
    for i in range(len(links)):
        print("{}\n {}\n {}\n".format(location[i], links[i], quality[i]))



def video_download(self, link, location, filename):
    def progress_function(percent):
        if percent != self.status.value():
            self.app_status.showMessage("Status: Pobieranie pliku {}".format(filename))
            self.status.setValue(percent)

    itag = self.set_format.itemData(self.set_format.currentIndex())
    self.downloader = Downloader()
    self.downloader.processSignal.connect(progress_function)
    self.downloader.download_video(link, location, itag)


class Downloader(QThread):
    processSignal = pyqtSignal(float)

    def __init__(self, parent=None):
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

#audio_converter_window.converter(self, location, default_filename)