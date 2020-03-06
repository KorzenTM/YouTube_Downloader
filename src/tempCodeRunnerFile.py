 def download_video(self):
        ydl_opts = {}
        os.chdir(self.save_location.text())
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link_textbox.text()])
    def open_directory(self):
          #print(self.save_location.text())
          webbrowser.open(self.save_location.text())
          
    def save_directory(self):
        dialog = QFileDialog()
        dialog.setOption(QFileDialog.ShowDirsOnly, True)
        dialog.setWindowTitle("Test")
        dialog.setAcceptMode(QFileDialog.AcceptOpen)
        #dialog.setNameFilter(nameFilter)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        if dialog.exec_() == QFileDialog.Accepted:
            self.save_location.setText(dialog.selectedFiles()[0])

    def open_link(self):
       # print(self.link_textbox.text())
        webbrowser.open(self.link_textbox.text())