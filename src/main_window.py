import button_function
from libraries import *

WIDTH = 800
HEIGHT = 600


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.qss_file = open("qss/style.qss").read()

        self.setWindowTitle("YouTube Video Downloader by KorzenTM")
        self.setFixedSize(WIDTH, HEIGHT)
        self.setStyleSheet(self.qss_file)
        self.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))

        self.top_background = QLabel(self)
        self.top_background.resize(780, 100)
        self.top_background.move(10, 10)
        self.top_background.setObjectName("top")

        self.middle_background = QLabel(self)
        self.middle_background.resize(780, 260)
        self.middle_background.move(10, 150)
        self.middle_background.setObjectName("other")

        self.download_background = QLabel(self)
        self.download_background.resize(780, 100)
        self.download_background.move(10, 420)
        self.download_background.setObjectName("other")

        self.status_background = QLabel(self)
        self.status_background.resize(800, 50)
        self.status_background.move(0, 550)
        self.status_background.setObjectName("appstatus")

        self.label_hello = QLabel("YouTube Downloader", self)
        self.label_hello.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.label_hello.setObjectName("hello")
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
        self.link.setObjectName("link")
        self.link.resize(700, 200)
        self.link.move(20, 183)

        self.link_textbox = QLineEdit(self)
        self.link_textbox.move(105, 180)
        self.link_textbox.resize(500, 30)
        self.link_textbox.setPlaceholderText("Example:http://www.youtube.com/watch?v=ecsCrOEYl7c")
        self.link_textbox.textChanged.connect(lambda: self.if_link_box_is_empty())

        self.if_link_correct = QLabel(self)
        self.if_link_correct.resize(50, 50)
        self.if_link_correct.move(610, 170)

        self.check_button = QPushButton(self)
        self.check_button.setGeometry(660, 175, 40, 40)
        self.check_button.setIcon(QIcon("resources/icons/fetch.png"))
        self.check_button.setIconSize(QSize(40, 40))
        self.check_button.setAutoFillBackground(True)
        self.check_button.setObjectName("check")
        self.check_button.setToolTip("Sprawdza podany link")
        self.check_button.clicked.connect(
            lambda: button_function.check_state_link_textbox(self, self.link_textbox.text()))

        self.add_to_list_button = QPushButton(self)
        self.add_to_list_button.setGeometry(700, 175, 40, 40)
        self.add_to_list_button.setIcon(QIcon("resources/icons/add.jpg"))
        self.add_to_list_button.setIconSize(QSize(40, 40))
        self.add_to_list_button.setAutoFillBackground(True)
        self.add_to_list_button.setObjectName("add")
        self.add_to_list_button.setToolTip("Dodaje do listy pobierania")
        self.add_to_list_button.clicked.connect(lambda: button_function.add_to_list(self, self.link_textbox.text(),
                                                                                    self.save_location.text(),
                                                                                    self.set_format.itemData(
                                                                                        self.set_format.currentIndex())))

        self.reset_button = QPushButton(self)
        self.reset_button.setGeometry(740, 175, 40, 40)
        self.reset_button.setObjectName("reset")
        self.reset_button.setToolTip("Wyczyszcza wszystkie pola")
        self.reset_button.setIcon(QIcon("resources/icons/clear.png"))
        self.reset_button.setIconSize(QSize(40, 40))
        self.reset_button.setAutoFillBackground(True)
        self.reset_button.clicked.connect(lambda: button_function.clear(self))

        self.image_label = QLabel(self)
        self.image_label.resize(240, 120)
        self.image_label.move(540, 240)

        self.information = QLabel("Informacje o filmie", self)
        self.information.setAlignment(Qt.AlignLeft)
        self.information.setObjectName("information")
        self.information.resize(400, 100)
        self.information.move(200, 220)

        self.description = QTextEdit(self)
        self.description.setReadOnly(True)
        self.description.setObjectName("information")
        self.description.resize(510, 120)
        self.description.move(20, 240)

        self.format = QLabel("Jakość:", self)
        self.format.setAlignment(Qt.AlignLeft)
        self.format.setObjectName("format")
        self.format.resize(400, 100)
        self.format.move(590, 375)

        self.set_format = QComboBox(self)
        self.set_format.setGeometry(650, 370, 130, 30)

        self.location = QLabel("Lokalizacja:", self)
        self.location.setAlignment(Qt.AlignLeft)
        self.location.setObjectName("location")
        self.location.resize(500, 200)
        self.location.move(20, 370)

        self.save_location = QLineEdit(self)
        self.save_location.resize(400, 30)
        self.save_location.move(130, 370)

        self.button_browse = QPushButton("...", self)
        self.button_browse.resize(50, 30)
        self.button_browse.move(535, 370)
        self.button_browse.setObjectName("search")
        self.button_browse.clicked.connect(lambda: button_function.save_directory(self))
        self.button_browse.setToolTip("Wybierz miejsce zapisu")

        self.download_status = QLabel("Status pobierania", self)
        self.download_status.setAlignment(Qt.AlignLeft)
        self.download_status.setObjectName("download_status")
        self.download_status.resize(150, 100)
        self.download_status.move(200, 430)

        self.status = QProgressBar(self)
        self.status.setGeometry(50, 460, 450, 25)

        self.button_download = QPushButton("POBIERZ", self)
        self.button_download.resize(215, 40)
        self.button_download.move(535, 425)
        self.button_download.setObjectName("download_button")
        self.button_download.setToolTip("Pobiera plik w wskazane miejsce")
        self.button_download.clicked.connect(
            lambda: button_function.download_video(self))

        self.convert_button = QPushButton("Konwertuj", self)
        self.convert_button.resize(215, 40)
        self.convert_button.move(535, 475)
        self.convert_button.setObjectName("convert_button")
        self.convert_button.setToolTip("Konwertuje na wybrany format muzyczny")

        self.app_status = QStatusBar(self)
        self.app_status.showMessage("Status: Oczekiwanie")
        self.app_status.setGeometry(0, 555, 800, 40)
        self.app_status.setObjectName("status")
        self.time = QLabel(self)
        self.date = QLabel(self)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        self.showTime()
        timer.start(1000)  # update every second
        datetime = QDate.currentDate()
        self.date.setText(datetime.toString(Qt.DefaultLocaleLongDate))

        self.app_status.addPermanentWidget(self.date)
        self.app_status.addPermanentWidget(self.time)

    def showTime(self):
        currentTime = QTime.currentTime()
        displayTxt = currentTime.toString('hh:mm:ss')
        self.time.setText(displayTxt)

    def if_link_box_is_empty(self):
        if self.link_textbox.text() == "":
            self.if_link_correct.clear()
            self.description.clear()
            self.image_label.clear()
            self.set_format.clear()
            self.save_location.clear()
            self.status.setValue(0)
            self.app_status.showMessage("Status: Oczekiwanie")
