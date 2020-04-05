from libraries import *
import alerts


class convert_window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(convert_window, self).__init__(*args, **kwargs)
        self.setWindowTitle("Audio Converter")
        self.resize(480, 320)
        self.hello = QLabel("Witaj!", self)

        self.top_background = QLabel(self)
        self.top_background.resize(460, 300)
        self.top_background.move(10, 10)
        self.top_background.setStyleSheet("background-color: #D3D3D3")

        self.set_audio_format = QComboBox(self)
        self.set_audio_format.setGeometry(255, 490, 100, 25)
        self.set_audio_format.addItem("MP3")
        self.set_audio_format.addItem("WAV")

        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setGeometry(100,100,50,30)
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
    window_2 = convert_window(self)
    window_2.get_data( location, filename)
    window_2.show()




