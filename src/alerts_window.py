
from libraries import *
import audio_converter_window

def no_link(self):
    msg_link = QMessageBox()
    msg_link.setWindowTitle("Ostrzeżenie")
    msg_link.setText("Nieprawidłowy link!")
    msg_link.setInformativeText("Nie podałeś linku bądź jest on nieprawidłowy. Sprawdź podany link.")
    msg_link.setIcon(QMessageBox.Critical)
    msg_link.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_link.exec_()


def no_location(self):
    msg_location = QMessageBox()
    msg_location.setWindowTitle("Ostrzeżenie")
    msg_location.setText("Nie podałeś lokalizacji.")
    msg_location.setInformativeText("Nie podałeś lokalizacji zapisu bądź jest on nieprawidłowy. Sprawdż podaną lokalizację.")
    msg_location.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_location.setIcon(QMessageBox.Critical)
    msg_location.exec_()


def bad_link_warning(self):
    self.pixmap_2 = QPixmap("resources/icons/wrong.png")
    self.scaled_pix_2 = self.pixmap_2.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
    self.if_link_correct.setPixmap(self.scaled_pix_2)
    self.app_status.showMessage("Nieprawidłowy link")
    self.loading = QMovie("resources/gif/yt_loading.gif")
    self.loading.setScaledSize(QSize(240, 120))
    self.image_label.setMovie(self.loading)
    self.loading.start()


def download_finished_window(self):
    msg_download = QMessageBox()
    msg_download.setWindowTitle("Informacja")
    msg_download.setText("Pobieranie zostało zakończone!")
    msg_download.setText("Plik został zapisany w podanej lokalizacji. ")
    msg_download.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_download.setIcon(QMessageBox.Information)
    msg_download.exec_()


def download_error(self):
    msg_error = QMessageBox()
    msg_error.setWindowTitle("Błąd")
    msg_error.setText("Wystąpił bląd podczas pobierania!")
    msg_error.setInformativeText("Nie jest możliwe rozpoczęcie pobierania. Sprawdź link bądź połączenie z internetem.")
    msg_error.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_error.setIcon(QMessageBox.Critical)
    msg_error.exec_()


def information_error():
    msg_information_error = QMessageBox()
    msg_information_error.setWindowTitle("Błąd")
    msg_information_error.setText("Nie możemy pobrać danych z serwera!")
    msg_information_error.setInformativeText("Nie jest możliwe pobranie informacji o filmie. Sprawdź połączenie sieciowe.")
    msg_information_error.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_information_error.setIcon(QMessageBox.Critical)
    msg_information_error.exec_()


def convert_finished(self):
    msg_convert_finished = QMessageBox()
    msg_convert_finished.setWindowTitle("Informacja")
    msg_convert_finished.setText("Konwersja została zakończona!")
    msg_convert_finished.setInformativeText("Konwersja do wybranego typu została zakończona. Okno zostanie zamknięte po wciśnieciu przycisku OK.")
    msg_convert_finished.setWindowIcon(QIcon("resources/icons/converter.png"))
    msg_convert_finished.setIcon(QMessageBox.Information)
    msg_convert_finished.exec_()

def convert_error(self):
    msg_convert_error = QMessageBox()
    msg_convert_error.setWindowTitle("Błąd")
    msg_convert_error.setText("Wystąpił problem z konwersją!")
    msg_convert_error.setInformativeText("Proces konwersji nie może zostać rozpoczęty. Sprawdź format bądź jakość.")
    msg_convert_error.setWindowIcon(QIcon("resources/icons/converter.png"))
    msg_convert_error.setIcon(QMessageBox.Critical)
    msg_convert_error.exec_()


def file_exist(self, location, filename):
    msg_file = QMessageBox()
    msg_file.setWindowTitle("Informacja")
    msg_file.setText("Ten plik został już pobrany.")
    msg_file.setInformativeText("Plik został już pobrany do podanej lokacji. Wciśnij ok - aby skonwertować plik do wybranego formatu lub cancel - aby wrócić do aplikacji. ")
    msg_file.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_file.setIcon(QMessageBox.Information)
    msg_file.setIcon(QMessageBox.Information)
    msg_file.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return_value = msg_file.exec_()

    if return_value == QMessageBox.Ok:
        audio_converter_window.converter(self, location, filename)





