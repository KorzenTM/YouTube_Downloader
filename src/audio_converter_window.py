from libraries import *
import button_function
import alerts_window

WIDTH = 480
HEIGHT = 320


def converter(self, location, filename):
    window_2 = convert_window(self)
    window_2.get_data(location, filename)
    window_2.show()


class convert_window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(convert_window, self).__init__(*args, **kwargs)
        self.setWindowTitle("Audio Converter")
        self.setWindowIcon(QIcon("resources/icons/converter.png"))
        self.setFixedSize(WIDTH, HEIGHT)

        self.sound_quality = "64k"
        self.format = ""

        self.settings_background = QLabel(self)
        self.settings_background.resize(460, 300)
        self.settings_background.move(10, 10)
        self.settings_background.setStyleSheet(
            "background-color: #D3D3D3; border: 2px solid black; border-radius: 25px;")

        self.format = QLabel("Format:", self)
        self.format.setGeometry(60, 110, 100, 30)
        self.mp3_button = QPushButton("mp3", self)
        self.mp3_button.setToolTip("Wybranie formatu .mp3")
        self.mp3_button.setGeometry(30, 140, 50, 30)
        self.mp3_button.setStyleSheet('background-color: #8B0000')
        self.mp3_button.setCheckable(True)
        self.wav_button = QPushButton("wma", self)
        self.wav_button.setToolTip("Wybranie formatu .wav")
        self.wav_button.setGeometry(90, 140, 50, 30)
        self.wav_button.setStyleSheet('background-color: #8B0000')
        self.wav_button.setCheckable(True)
        self.ogg_button = QPushButton("ogg", self)
        self.ogg_button.setToolTip("Wybranie formatu .ogg")
        self.ogg_button.setGeometry(30, 175, 50, 30)
        self.ogg_button.setStyleSheet('background-color: #8B0000')
        self.ogg_button.setCheckable(True)
        self.btn_group = QButtonGroup(self)
        self.btn_group.addButton(self.mp3_button, 1)
        self.btn_group.addButton(self.wav_button, 2)
        self.btn_group.addButton(self.ogg_button, 3)
        self.btn_group.buttonClicked.connect(self.on_button_clicked)
        self.format = QLabel("Jakość", self)
        self.format.setGeometry(330, 110, 150, 30)
        self.quality = QSlider(Qt.Horizontal, self)
        self.quality.setGeometry(280, 140, 150, 30)
        self.quality.setFocusPolicy(Qt.StrongFocus)
        self.quality.setTickPosition(QSlider.TicksBothSides)
        self.quality.setTickInterval(1)
        self.quality.setMinimum(0)
        self.quality.setMaximum(3)
        self.quality.valueChanged[int].connect(self.change_value)
        self.quality_info = QLabel(self)
        self.quality_info.setText("Ekonomiczny\n64 kbps")
        self.quality_info.setGeometry(330, 170, 100, 60)

        self.convert_button = QPushButton("Konwertuj", self)
        self.convert_button.setObjectName("convert")
        self.convert_button.setToolTip("Rozpocznij konwersję do wybranego formatu")
        self.convert_button.setGeometry(160, 230, 150, 50)
        self.convert_button.clicked.connect(self.convert_button_clicked)
        self.progres = QLabel(self)
        self.progres.setGeometry(320, 230, 50, 50)
        self.app_status = QStatusBar(self)
        self.app_status.showMessage("Status: Oczekiwanie")
        self.app_status.setGeometry(10, 280, 460, 20)

        self.logo = QLabel(self)
        self.pixmap = QPixmap("resources/img/converter_logo.png")
        self.scaled_pix = self.pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo.setPixmap(self.scaled_pix)
        self.logo.resize(50, 50)
        self.logo.move(400, 240)

    def on_button_clicked(self):
        if self.btn_group.checkedId() == 1:
            self.mp3_button.setStyleSheet('background-color: #006400')
            self.wav_button.setStyleSheet('background-color: #8B0000')
            self.ogg_button.setStyleSheet('background-color: #8B0000')
            self.format = ".mp3"
        if self.btn_group.checkedId() == 2:
            self.wav_button.setStyleSheet('background-color: #006400')
            self.mp3_button.setStyleSheet('background-color: #8B0000')
            self.ogg_button.setStyleSheet('background-color: #8B0000')
            self.format = ".wav"
        if self.btn_group.checkedId() == 3:
            self.ogg_button.setStyleSheet('background-color: #006400')
            self.wav_button.setStyleSheet('background-color: #8B0000')
            self.mp3_button.setStyleSheet('background-color: #8B0000')
            self.format = ".ogg"

    def change_value(self, value=0):
        if value == 0:
            self.sound_quality = "64k"
            self.quality_info.setText("Ekonomiczna\n64 kbps")
        if value == 1:
            self.sound_quality = "128k"
            self.quality_info.setText("Standard\n128 kbps")
        if value == 2:
            self.sound_quality = "192k"
            self.quality_info.setText("Dobra\n192 kbps")
        if value == 3:
            self.sound_quality = "320k"
            self.quality_info.setText("Najlepsza\n320 kbps")

    def get_data(self, location, filename):
        location = location
        filename = filename

        self.name_info = QLabel("Plik:", self)
        self.name_info.setGeometry(15, 30, 50, 30)
        self.file_name = QLineEdit(self)
        self.file_name.setGeometry(50, 30, 400, 30)
        self.file_name.setText(filename)
        self.file_name.setReadOnly(True)

        self.location_info = QLabel("Lokalizacja: ", self)
        self.location_info.setGeometry(15, 60, 100, 30)
        self.file_location = QLineEdit(self)
        self.file_location.setGeometry(100, 60, 350, 30)
        self.file_location.setText(location)
        self.file_location.setReadOnly(True)

    def convert_button_clicked(self):
        def set_status(message):
            self.app_status.showMessage(message)

            self.loading = QMovie("resources/gif/convert_progres.gif")
            self.loading.setScaledSize(QSize(50, 50))
            self.progres.setMovie(self.loading)
            self.loading.start()

            self.pixmap_1 = QPixmap("resources/icons/wrong.png")
            self.scaled_pix_1 = self.pixmap_1.scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)

            self.pixmap_2 = QPixmap("resources/icons/check.png")
            self.scaled_pix_2 = self.pixmap_2.scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation)

            if message == "Status: Wystąpił błąd podczas konwersji. Sprawdź ustawienia":
                self.progres.clear()
                self.progres.setPixmap(self.scaled_pix_1)
                alerts_window.convert_error(self)
            if message == "Status: Konwersja zakończona!":
                self.progres.clear()
                self.progres.setPixmap(self.scaled_pix_2)
                alerts_window.convert_finished(self)
                self.close()

        location = self.file_location.text()
        file = self.file_name.text()
        full_path = os.path.join(location, file)
        output_path = os.path.join(location, os.path.splitext(file)[0] + str(self.format))
        quality = self.sound_quality
        self.conv = convert()
        self.thread_1 = QThread()
        self.conv.moveToThread(self.thread_1)
        self.conv.started.connect(self.conv.run)
        self.conv.processSignal.connect(set_status)
        self.conv.convert(full_path, output_path, quality)


class convert(QThread):
    processSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(convert, self).__init__()
        self.full_path = None
        self.output_path = None
        self.sound_quality = None

    def convert(self, full_path, output_path, sound_quality):
        self.full_path = full_path
        self.output_path = output_path
        self.sound_quality = sound_quality

        self.start()

    def run(self):
        message = "Status: Konwersja"
        error_message = "Status: Wystąpił błąd podczas konwersji. Sprawdź ustawienia"
        self.processSignal.emit(message)
        try:
            clip = AudioFileClip(self.full_path)
            clip.write_audiofile(self.output_path, fps=44100, nbytes=4, bitrate=self.sound_quality)
        except:
            self.processSignal.emit(error_message)
        else:
            os.remove(self.full_path)
            message_2 = "Status: Konwersja zakończona!"
            self.processSignal.emit(message_2)


