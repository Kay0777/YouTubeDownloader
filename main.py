from PyQt5.QtWidgets import QApplication
from core import MyCoreWindow, Loader, Open
from pytube import YouTube
from threading import Thread
import sys
import re
import os
import time

REGEXs = [
    "http[s]?://(?:[a-zA-Z]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
    "^www?.(?:[-\w.]|[$-_@.&+]|[!*\(\),])*"
]

URL = ''
RES = ''
OUTPUT_URL = ''


class YouTubeK(MyCoreWindow):
    def __init__(self):
        super().__init__()
        self.url.textChanged.connect(self.clear)
        self.where.clicked.connect(self.get_output_path)
        self.download.clicked.connect(self.download_video)

    def clear(self):
        if self.url.text() == '':
            self.status.setText('')

    def download_video(self):
        self.loader = Loader()
        print(OUTPUT_URL)

        def download_now():
            global URL, RES, OUTPUT_URL, REGEXs

            URL = self.url.text()
            RES = self.format.currentText()
            self.status.setText("Please! Wait")
            if (re.search(REGEXs[0], URL) or re.search(REGEXs[1], URL)):
                try:
                    yt = YouTube(url=URL)
                    video = yt.streams.filter(
                        file_extension='mp4',
                        res=f'{RES}',
                        progressive="True")[0]
                    video.download(output_path=OUTPUT_URL)
                    self.status.setText("Video downloaded")
                except Exception as e:
                    print(f'{e}')
                    self.status.setText('Not found!')
            else:
                self.status.setText('Please! Check url')
            time.sleep(0.5)
            self.loader.check = True
            self.loader.close()

        download = Thread(target=download_now)
        download.start()

    def get_output_path(self):
        global OUTPUT_URL

        where = Open()
        if where.exec_():
            OUTPUT_URL = where.directory().absolutePath()


def main():
    app = QApplication(sys.argv)
    _yt_downloader = YouTubeK()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
