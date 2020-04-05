import button_function
from libraries import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        qss_file = open("qss/style.qss").read()

        self.setWindowTitle("YouTube Video Downloader by KorzenTM")
        self.resize(800, 600)
        self.setStyleSheet(qss_file)
        self.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))

        # backgrounds
        self.top_background = QLabel(self)
        self.top_background.resize(780, 100)
        self.top_background.move(10, 10)
        self.top_background.setStyleSheet("background-color: #B22222")
        self.middle_background = QLabel(self)
        self.middle_background.resize(780, 260)
        self.middle_background.move(10, 150)
        self.middle_background.setStyleSheet("background-color: #D3D3D3")
        self.download_background = QLabel(self)
        self.download_background.resize(780, 100)
        self.download_background.move(10, 420)
        self.download_background.setStyleSheet("background-color: #D3D3D3")


        self.label_hello = QLabel("YouTube Downloader", self)
        self.label_hello.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.label_hello.setStyleSheet("font: 25pt Times New Roman")
        self.label_hello.resize(400, 100)
        self.label_hello.move(0, 10)

        self.logo = QLabel(self)
        self.pixmap = QPixmap("resources/img/logo_yt.png")
        self.scaled_pix = self.pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.logo.setPixmap(self.scaled_pix)
        self.logo.resize(200, 200)
        self.logo.move(550, -45)

        self.link = QLabel("Video Url:", self)
        self.link.setAlignment(Qt.AlignLeft)
        self.link.setStyleSheet("font: 15pt Times New Roman")
        self.link.resize(700, 200)
        self.link.move(20, 183)

        self.wrong_pic = QLabel(self)
        self.wrong_pic.resize(50, 50)
        self.wrong_pic.move(630, 170)
        self.warning = QLabel(self)
        self.warning.setAlignment(Qt.AlignLeft)
        self.warning.setStyleSheet("font: 10pt Times New Roman")
        self.warning.resize(400, 100)
        self.warning.move(660, 185)

        self.link_textbox = QLineEdit(self)
        self.link_textbox.move(130, 180)
        self.link_textbox.resize(500, 30)
        self.link_textbox.setPlaceholderText("Example:http://www.youtube.com/watch?v=ecsCrOEYl7c")
        self.link_textbox.textChanged.connect(lambda: button_function.clear(self))
        self.check_button = QPushButton(self)
        self.check_button.setGeometry(730, 180, 50, 30)
        self.check_button.setIcon(QIcon("resources/icons/fetch.png"))
        self.check_button.clicked.connect(
            lambda: button_function.check_state_link_textbox(self, self.link_textbox.text()))
        self.image_label = QLabel(self)
        self.image_label.resize(240, 120)
        self.image_label.move(540, 240)

        self.information = QLabel("Informacje o filmie", self)
        self.information.setAlignment(Qt.AlignLeft)
        self.information.setStyleSheet("font: 10pt Times New Roman")
        self.information.resize(400, 100)
        self.information.move(200, 220)

        self.description = QTextEdit(self)
        self.description.setReadOnly(True)
        self.description.setObjectName("information")
        self.description.resize(510, 120)
        self.description.move(20, 240)

        self.format = QLabel("Jakość:", self)
        self.format.setAlignment(Qt.AlignLeft)
        self.format.setStyleSheet("font: 12pt Times New Roman")
        self.format.resize(400, 100)
        self.format.move(590, 375)

        self.set_format = QComboBox(self)
        self.set_format.setGeometry(650, 370, 130, 30)

        self.location = QLabel("Zapisz do:", self)
        self.location.setAlignment(Qt.AlignLeft)
        self.location.setStyleSheet("font: 15pt Times New Roman")
        self.location.resize(700, 200)
        self.location.move(20, 370)

        self.save_location = QLineEdit(self)
        self.save_location.resize(400, 30)
        self.save_location.move(130, 370)

        self.button_browse = QPushButton("...", self)
        self.button_browse.resize(50, 30)
        self.button_browse.move(535, 370)
        self.button_browse.setObjectName("search")
        self.button_browse.clicked.connect(lambda: button_function.save_directory(self))
        self.button_browse.setToolTip("Przegląda dysk")

        self.download_status = QLabel("Status pobierania", self)
        self.download_status.setAlignment(Qt.AlignLeft)
        self.download_status.setStyleSheet("font: 10pt Times New Roman")
        self.download_status.resize(150, 100)
        self.download_status.move(200, 430)

        self.status = QProgressBar(self)
        self.status.setGeometry(50, 460, 450, 25)

        self.convert_mp3_check = QCheckBox("Konwersja po pobraniu na:", self)
        self.convert_mp3_check.setGeometry(50, 425, 250, 150)
        self.convert_mp3_check.setStyleSheet("font: 10pt Times New Roman")

        self.button_download = QPushButton("POBIERZ", self)
        self.button_download.resize(215, 50)
        self.button_download.move(535, 450)
        self.button_download.setObjectName("download")
        self.button_download.clicked.connect(lambda: button_function.download_video(self, self.save_location.text(), self.link_textbox.text()))

        self.app_status = QStatusBar(self)
        self.app_status.showMessage("Status: Oczekiwanie")
        self.app_status.setGeometry(0, 560, 800, 40)
        self.app_status.setObjectName("status")
        self.write = QLabel("Problem z aplikacją?", self)
        self.button_help = QPushButton("Napisz!", self)
        self.button_help.setObjectName("support")
        self.button_help.setToolTip("Problem? Skontaktuj się ze mną.")
        self.app_status.addPermanentWidget(self.write)
        self.app_status.addPermanentWidget(self.button_help)