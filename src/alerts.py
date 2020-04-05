from libraries import *


def no_link(self):
    msg_link = QMessageBox()
    msg_link.setWindowTitle("Ostrzeżenie")
    msg_link.setText("Nie podałeś linku")
    msg_link.setIcon(QMessageBox.Critical)
    msg_link.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_link.exec_()


def no_location(self):
    msg_location = QMessageBox()
    msg_location.setWindowTitle("Ostrzeżenie")
    msg_location.setText("Nie podałeś lokalizacji")
    msg_location.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_location.setIcon(QMessageBox.Critical)
    msg_location.exec_()


def download_finished_window():
    msg_download = QMessageBox()
    msg_download.setWindowTitle("Informacja")
    msg_download.setText("Pobieranie zostało zakończone!")
    msg_download.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_download.setIcon(QMessageBox.Information)
    msg_download.exec_()


def convert_finished_window():
    msg_convert = QMessageBox()
    msg_convert.setWindowTitle("Informacja")
    msg_convert.setText("Konwersja została zakończona!")
    msg_convert.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_convert.setIcon(QMessageBox.Information)
    msg_convert.exec_()

def download_error():
    msg_error = QMessageBox()
    msg_error.setWindowTitle("Błąd")
    msg_error.setText("Wystąpił bląd podczas pobierania. Sprawdź link.")
    msg_error.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_error.setIcon(QMessageBox.Critical)
    msg_error.exec_()

def information_error():
    msg_information_error = QMessageBox()
    msg_information_error.setWindowTitle("Błąd")
    msg_information_error.setText("Nie możemy pobrać danych z serwera!")
    msg_information_error.setWindowIcon(QIcon("resources/icons/YouTube-icon.png"))
    msg_information_error.setIcon(QMessageBox.Critical)
    msg_information_error.exec_()
