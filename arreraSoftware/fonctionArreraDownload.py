from pytube import*
from librairy.travailJSON import *
from tkinter import*
from tkinter.messagebox import showinfo
from tkinter import messagebox
import os
import webbrowser

class fncArreraVideoDownload :
    def __init__(self,ConfigNeuron:jsonWork):
        #variable
        self.__fichierGestion = ConfigNeuron
        self.__color = self.__fichierGestion.lectureJSON("interfaceColor")
        self.__textColor = self.__fichierGestion.lectureJSON("interfaceTextColor")
        self.__name = self.__fichierGestion.lectureJSON("name")
        self.__icon = self.__fichierGestion.lectureJSON("iconAssistant")
        self.__listChoix = ["simple","playlist"]
        self.__fileMusic = "download"
        self.__fileVideo = "download"
        self.__btnColor = "red"
        self.__textBTNcolor = "white"
        
    def fenetreDownload(self,mode):
        #fenetre TK
        self.__screen = Toplevel()
        self.__varChoix = StringVar(self.__screen)
        self.__screen.title(self.__name+": Youtube Download")
        self.__screen.config(bg=self.__color)
        self.__screen.iconphoto(False,PhotoImage(file=self.__icon))
        self.__screen.maxsize(500,300)
        self.__screen.minsize(500,300)
        #cadre
        self.__cadreDownload = Frame(self.__screen,bg=self.__color,width=450,height=250)
        self.__cadreWait = Frame(self.__screen,bg=self.__color,width=450,height=250)
        #entry
        self.__entryURL = Entry(self.__cadreDownload,width=30,border=2,font=("arial",15))
        #label
        self.__labelindiction = Label(self.__cadreDownload,font=("arial",15),bg=self.__color,fg=self.__textColor)
        self.__labelWait = Label(self.__cadreWait,text="En court",font=("arial",25),bg=self.__color,fg=self.__textColor)
        #option menu
        self.__menu = OptionMenu(self.__cadreDownload,self.__varChoix,*self.__listChoix)
        #button
        self.__boutonDownload = Button(self.__cadreDownload,text="Télécharger",bg=self.__btnColor,fg=self.__textBTNcolor,font=("arial",15))
        self.__boutonYoutube = Button(self.__cadreDownload,text="Ouvrir Youtube",bg=self.__btnColor,fg=self.__textBTNcolor,font=("arial",15),command= lambda : webbrowser.open("https://www.youtube.com/"))
        #affichage
        
        self.__labelindiction.place(x=100,y=0)
        self.__menu.place(x=0,y=0)
        self.__entryURL.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.__boutonDownload.place(x=330,y=210)
        self.__boutonYoutube.place(relx=0.5, rely=1.0, anchor="s")
        
        self.__labelWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
        if mode == "video" :
            self.__labelindiction.configure(text="Copier L'URL d'une video")
            self.downloadView()
            self.__boutonDownload.config(command=self.downloadVideo)
            self.__screen.mainloop()
        else :
            if mode == "music" :
                self.__labelindiction.configure(text="Copier L'URL d'une musique")
                self.downloadView()
                self.__boutonDownload.config(command=self.downloadMusique)
                self.__screen.mainloop()
            else :
                messagebox.showwarning("Attention", "Le mode que vous demandez n'existe pas.")
    
    def downloadVideoSimple(self):
        self.waitView()
        valURL = self.__entryURL.get()
        self.__entryURL.delete(0,END)
        Media = YouTube(valURL)
        downloadMedia = Media.streams.get_by_itag(18)
        downloadMedia.download(self.__fileVideo)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadVideoPlaylist(self):
        self.waitView()
        valURL = self.__entryURL.get()
        self.__entryURL.delete(0,END)
        playlist = Playlist(valURL)
        for videos in playlist.videos:
            videos.streams.get_by_itag(18).download(self.__fileVideo)      
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadMusiqueSimple(self):
        self.waitView()
        valURL = self.__entryURL.get()
        self.__entryURL.delete(0,END)
        Media = YouTube(valURL)
        downloadMedia = Media.streams.filter(only_audio=True).first()
        out_file = downloadMedia.download(self.__fileMusic)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadMusiquePlaylist(self):
        self.waitView()
        valURL = self.__entryURL.get()
        self.__entryURL.delete(0,END)
        playlist = Playlist(valURL)
        for videos in playlist.videos:
            downloadMedia = videos.streams.filter(only_audio=True).first()
            out_file = downloadMedia.download(self.__fileMusic)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        showinfo(title="Youtube Downloader",message="Video Télécharger")
        self.waitNoView()
    
    def downloadVideo(self):
        var = self.__varChoix.get()
        if var == "simple" :
            self.downloadVideoSimple()
        else :
            self.downloadVideoPlaylist()
    
    def downloadMusique(self):
        var = self.__varChoix.get()
        if var == "simple" :
            self.downloadMusiqueSimple()
        else :
            self.downloadMusiquePlaylist()
    
        
    def downloadView(self):
        
        self.__cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)
        self.__varChoix.set(self.__listChoix[0])
        
    def waitView(self):
        self.__cadreDownload.place_forget()
        self.__cadreWait.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    def waitNoView(self):
        self.__cadreWait.place_forget()
        self.__cadreDownload.place(relx=0.5,rely=0.5,anchor=CENTER)        