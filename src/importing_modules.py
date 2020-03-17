import sys
import subprocess
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import QCheckBox,QComboBox,QTextEdit,QVBoxLayout,QProgressBar,QApplication, QToolButton,QWidget, QMainWindow, QLabel, QPushButton,QFileDialog ,QMessageBox, QDesktopWidget, QLineEdit, QFileSystemModel, QTreeView, QVBoxLayout
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt, QUrl,QProcess  #ma wiele atrybutów do widgetow
import urllib
import webbrowser
import os
import time
import pytube
from bs4 import BeautifulSoup
import re
import moviepy.editor as mp