from objet.CArreraDownload import*
from ObjetsNetwork.gestion import*
import threading as th
from tkinter import*
from librairy.asset_manage import resource_path

class fncArreraVideoDownload :
    def __init__(self,configNeuron:jsonWork,gestUser:gestionNetwork) :
        self.__nameAssistant = configNeuron.lectureJSON("name")+" : Video Download"
        self.__interfaceColor = configNeuron.lectureJSON("interfaceColor")
        self.__textColor = configNeuron.lectureJSON("interfaceTextColor")
        self.__icon = resource_path(configNeuron.lectureJSON("iconAssistant"))
        self.__aDownload = CArreraDownload()
        self.__gestUser = gestUser

    def __windows(self):
        windows = Toplevel()
        windows.minsize(400,500)
        windows.maxsize(400,500)
        windows.iconphoto(False,PhotoImage(file=self.__icon))
        windows.title(self.__nameAssistant)
        windows.configure(bg=self.__interfaceColor)
        # Widget 
        labelTitle = Label(windows,text="Arrera Download"
                           ,font=("Arial",30),bg=self.__interfaceColor
                           ,fg=self.__textColor)
        self.__eDownload = Entry(windows,font=("Arial","15"),highlightthickness=2,
                          highlightbackground="black")
        self.__btnDownload = Button(windows,text="Télécharger"
                                    ,font=("Arial",15),bg=self.__interfaceColor
                                    ,fg=self.__textColor)
        
        # Affichage 
        labelTitle.place(relx=0.5, rely=0.0, anchor="n") 
        self.__eDownload.place(relx=0.5, rely=0.5, anchor="center")
        self.__btnDownload.place(relx=0.5, rely=1.0, anchor="s") 
    
    def activeMusique(self):
        self.__windows()
        self.__btnDownload.configure(command=lambda : self.__downloadGUI(1))
    
    def activeVideo(self):
        self.__windows()
        self.__btnDownload.configure(command=lambda : self.__downloadGUI(2))
    
    def __downloadGUI(self,mode:int):
        """
        Args:
            mode (int): 1 -> Musique 2->Video
        """
        self.download(mode,self.__eDownload.get())
        self.__eDownload.delete(0,END)
    
    def download(self,mode:int,url:str):
        """
        Args:
            mode (int): 1 -> Musique 2->Video
            url (str): Url de la video
        """
        if (url != ""):
            if (self.__gestUser.getEmplacementDownload()==""):
                sortie = self.__aDownload.setDownloadFolder()
            else :
                sortie = self.__aDownload.setDownloadFolderDur(self.__gestUser.getEmplacementDownload())
            
            if (sortie == True):
                match mode :
                    case 1 :
                        self.__aDownload.setMode(2)
                        self.__aDownload.setURL(url)
                    case 2 :
                        self.__aDownload.setMode(1)
                        self.__aDownload.setURL(url)
                
                tDownload = th.Thread(target=self.__aDownload.download)
                tDownload.start()
                tDownload.join()
                del tDownload
                return True
            else :
                return False
        else :
            return False