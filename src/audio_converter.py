from libraries import *
import alerts


class Downloader(QThread):
    processSignal = pyqtSignal(float)

    def __init__(self, parent=None):
        super(Downloader, self).__init__(parent=parent)
        self.path = None
        self.url = None
        self.video = None
        self.stream = None

    def download_video(self, url, path):
        self.path = path
        self.url = url

        self.start()

    def run(self):
        self.video = YouTube(self.url)
        self.video.register_on_progress_callback(self.return_progress)
        self.stream = self.video.streams.first()
        self.stream.download(self.path)

    def return_progress(self, stream, chunk, file_handle, bytes_remaining):
        percentage = 1 - bytes_remaining / self.stream.filesize
        self.processSignal.emit(percentage)

class convert_window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(convert_window, self).__init__(*args, **kwargs)
        self.setWindowTitle("Audio Converter")
        self.setWindowIcon(QIcon("resources/icons/converter.png"))
        self.resize(480, 320)

        qss_file = open("qss/style.qss").read()
        self.setStyleSheet(qss_file)

        self.top_background = QLabel(self)
        self.top_background.resize(100, 100)
        self.top_background.move(10, 10)
        self.setObjectName("top")
        self.top_background.setStyleSheet("background-color: #D3D3D3")

        self.top_background = QLabel(self)
        self.top_background.resize(320, 300)
        self.top_background.move(10, 10)
        self.top_background.setStyleSheet("background-color: #D3D3D3")

        self.set_audio_format = QComboBox(self)
        self.set_audio_format.setGeometry(230, 250, 50, 50)
        self.set_audio_format.addItem("MP3")
        self.set_audio_format.addItem("WAV")

        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setObjectName("convert")
        self.convert_button.setGeometry(100, 100, 50, 30)
        #self.convert_button.clicked.connect(self.convert())

    def get_data(self, location, filename):
        print(location)
        print(filename)


""""
    def convert(self):
        # convert_window.show()
        audio_formats = [".mp3", ".wav"]
        file_name = str(filename.split('.')[0])
        #self.app_status.setText("Status: Konwersja")
        for file in [n for n in os.listdir(location) if n == self.video.default_filename]:
            full_path = os.path.join(location, file)
            output_path = os.path.join(location, os.path.splitext(file)[0] + audio_formats[index])
            clip = mp.AudioFileClip(full_path)
            clip.write_audiofile(output_path)
        alerts.convert_finished_window()
        #self.app_status.setText("Status: Konwersja zakończona")
"""


def converter(self, location, filename):
    self.app_status.showMessage("Status: Konwersja")
    window_2 = convert_window(self)
    window_2.get_data( location, filename)
    window_2.show()




