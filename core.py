from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from PyQt5.QtWidgets import QLineEdit, QComboBox, QGridLayout
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtGui import QMovie


class MyCoreWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_settings()
        self.set_widgets()
        self.show()

    def set_settings(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(QSize(350, 120))
        self.setStyleSheet("""
            QLabel, QPushButton, QComboBox{
                font-family: Arial;
                font-weight: bold;}""")

    def set_widgets(self):
        lay = QGridLayout()
        lay.setSpacing(5)
        self.setLayout(lay)

        lay.addWidget(QLabel('Url:'), 0, 0, 1, 1)

        self.url = QLineEdit()
        self.url.setPlaceholderText('https://youtu.be/x1ZtIVuHph0')
        lay.addWidget(self.url, 0, 1, 1, 11)

        self.format = QComboBox()
        self.format.setCursor(Qt.PointingHandCursor)
        self.format.addItems(['360p', '720p', '1080p'])
        lay.addWidget(self.format, 0, 12, 1, 2)

        lay.addWidget(QLabel('Where to save:'), 1, 5, 1, 3)

        self.where = QPushButton('open')
        self.where.setCursor(Qt.PointingHandCursor)
        lay.addWidget(self.where, 1, 8, 1, 2)

        self.download = QPushButton('download')
        self.download.setCursor(Qt.PointingHandCursor)
        lay.addWidget(self.download, 1, 10, 1, 4)

        self.status = QLabel()
        self.status.setMaximumHeight(10)
        self.status.setStyleSheet("""
            QLabel{
                font-family: Arial;
                font-size: 10px;}""")
        self.status.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        lay.addWidget(self.status, 8, 9, 1, 5)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Escape:
            self.close()


class Loader(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(QSize(150, 100))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        scene = QLabel(self)
        self.gif = QMovie('assets/loader4.gif')
        scene.setMovie(self.gif)
        self.gif.start()
        self.show()
