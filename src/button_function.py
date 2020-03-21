from importing_modules import *
 
 
def data_reset(self):
    self.description.setText("")  
    self.link_textbox.setText("")
    self.set_format.clear()
    self.image_label.clear()
    self.save_location.clear()

def bad_link_warning():
    msg=QMessageBox()
    msg.setWindowTitle("Ostrzeżenie")
    msg.setText("Podano zły link!")
    msg.setIcon(QMessageBox.Critical)
    x=msg.exec_()
    
def download_finished_window():
    msg=QMessageBox()
    msg.setWindowTitle("Informacja")
    msg.setText("Pobieranie zostało zakończone!")
    msg.setIcon(QMessageBox.Information)
    x=msg.exec_()
    
def convert_finished_window():
    msg=QMessageBox()
    msg.setWindowTitle("Informacja")
    msg.setText("Konwersja została zakończona!")
    msg.setIcon(QMessageBox.Information)
    x=msg.exec_()
     
def download_video(self,location,link):
    if self.link_textbox.text()=="":
        msg=QMessageBox()
        msg.setWindowTitle("Ostrzeżenie")
        msg.setText("Nie podałeś linku")
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()
    if self.save_location.text()=="":
        msg=QMessageBox()
        msg.setWindowTitle("Ostrzeżenie")
        msg.setText("Nie podałeś lokalizacji")
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()
    else:
        def progress_function(chunk,file_handle,bytes_remaining):
            progres=round((1-bytes_remaining/self.video.filesize)*100, 3)
            self.status.setValue(progres)
            
        self.video_url =link 
        self.youtube = pytube.YouTube(self.video_url,on_progress_callback=progress_function)
        self.video = self.youtube.streams.get_by_itag(self.set_format.itemData(self.set_format.currentIndex()))
        file_name=str(self.video.default_filename.split('.')[0])        
        temp=file_name+'.'+'mp4'
        print(temp)
        if self.convert_mp3_check.isChecked():
            self.video.download(location)
            for file in[n for n in os.listdir(location) if n==self.video.default_filename]:
                full_path=os.path.join(location,file)
                output_path=os.path.join(location,os.path.splitext(file)[0]+'.mp3')
                clip=mp.AudioFileClip(full_path)
                clip.write_audiofile(output_path)
                self.status.setValue(clip.iter_chunks)
            convert_finished_window();
        else:
            self.video.download(location)
            download_finished_window()
        

def save_directory(self):
    dialog = QFileDialog()
    dialog.setOption(QFileDialog.ShowDirsOnly, True)
    dialog.setWindowTitle("Wybierz folder")
    dialog.setAcceptMode(QFileDialog.AcceptOpen)
    dialog.setFileMode(QFileDialog.DirectoryOnly)
    if dialog.exec_() == QFileDialog.Accepted:
        self.save_location.setText(dialog.selectedFiles()[0])
      
def check_state_link_textbox(self,link):
    if self.link_textbox.text()=="":
        self.check_button.setEnabled(False)
    else:
        self.reset_button.setEnabled(True)
        self.video_url =link #video link
        try:
            self.youtube = pytube.YouTube(self.video_url)
        except:
            bad_link_warning()
        else:
            url=pytube.YouTube(self.video_url).thumbnail_url
            data=urllib.request.urlopen(url).read()
            self.thumb=QPixmap()
            self.thumb.loadFromData(data)
            self.scaled=self.thumb.scaled(180,125,Qt.KeepAspectRatio,Qt.FastTransformation)
            self.image_label.setPixmap(self.scaled)
            self.video = self.youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')
            self.description.setText("Tytuł: %s\n\nAutor: %s\n\nOpis: %s" %(self.youtube.title,self.youtube.author,self.youtube.description))
            tag = ""
            for i in self.video:
                tag = re.split(r" itag=\"|\" mime_type", str(i))
                temp=(str(i).split()[2].split("=")[1].split("/")[1]+" "+str(i).split()[3].split("=")[1]).replace('"',"").upper()
                self.set_format.addItem(temp,int(tag[1]))
            
        
    

def center(self):
        #geometry of the main window
        qr=self.frameGeometry()
        #center point of screen
        cp=QDesktopWidget().availableGeometry().center()
        #move rectangle's center point to screen's center poit
        qr.moveCenter(cp)
        #top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())