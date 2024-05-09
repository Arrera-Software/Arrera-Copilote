from neuronCopilote.neuroncopilote import*
from gazelle.arreraAssistantSetting import *
from lynx.arreraLynx import*
from PIL import Image, ImageTk

class ArreraCopilote :
    def __init__(self):
        # Verification des configuaration 
        if self.__verifBoot()==False:
            self.__bootWithLynx()
        #objet assistant
        self.__assistantSix = ArreraNetwork("configuration/configUser.json",
                                          "configuration/six.json",
                                          "configuration/listFete.json")
        self.__assistantRyley = ArreraNetwork("configuration/configUser.json",
                                          "configuration/ryley.json",
                                          "configuration/listFete.json")
        # varriable couleur
        self.__mainColor = "white"
        self.__textMainColor = "black"
        #fenetre tkinter
        self.__screen = Tk()
        self.__screen.title("Arrera : Copilote")
        self.__screen.maxsize(700,700)
        self.__screen.minsize(700,700)
        # objet Parametre
        self.__parametre = ArreraSettingAssistant("configuration/configSetting.json",
                                                  "configuration/six.json",
                                                  "configuration/copilote.json",
                                                  "configuration/configUser.json")
        # Neuron copilote
        self.__copiloteNeuron = neuronCopilote("configuration/configUser.json")
        # emplacement icon 
        self.__emplacementIconSix = "asset/icon/six/logo-normal.png"
        self.____emplacementIconRyley = "asset/icon/ryley/icon.png"
        self.__emplacementIconCopilote = "asset/icon/copilote/icon.png"
        # Ajout icon a la fenetre
        self.__screen.iconphoto(False,PhotoImage(file=self.__emplacementIconCopilote))
        # Mise en place de l'interface
        frameTop = Frame(self.__screen,bg=self.__mainColor,width=700,height=100)
        frameReponse =  Frame(self.__screen,bg=self.__mainColor,width=700,height=450)
        frameInput = Frame(self.__screen,bg=self.__mainColor,width=700,height=100)
        frameBottom = Frame(self.__screen,bg=self.__mainColor,width=700,height=50)
        # Widget frameTop
        labelTitle = Label(frameTop,text="Arrera Copilote",bg=self.__mainColor,fg=self.__textMainColor,font=("arial","35"))
        # Widget frameReponse
        labelIconRyley = Label(frameReponse,bg=self.__mainColor)
        labelIconSix = Label(frameReponse,bg=self.__mainColor)
        iconSix = ImageTk.PhotoImage((Image.open(self.__emplacementIconSix).resize((60,60))))
        iconRyley = ImageTk.PhotoImage((Image.open(self.____emplacementIconRyley).resize((60,60))))
        labelIconSix.image_names = iconSix
        labelIconRyley.image_names = iconRyley
        labelIconSix.configure(image=iconSix)
        labelIconRyley.configure(image=iconRyley)
        self.__labelReponseSix = Label(frameReponse,font=("arial","15"),bg=self.__mainColor,text="")
        self.__labelReponseRyley = Label(frameReponse,font=("arial","15"),bg=self.__mainColor,text="")
        # Widget frameInput
        input = Frame(frameInput)
        self.__entryInput = Entry(input,width=35,font=("arial","20"),relief=SOLID)
        btnSend = Button(input,text="Envoyer",bg=self.__mainColor,fg=self.__textMainColor,font=("arial","15"),command=self.__envoie)
        # Widget frameBottom
        btnApropos = Button(frameBottom,bg=self.__mainColor,command=self.__Apropop)
        iconApropos = ImageTk.PhotoImage((Image.open("asset/icon/copilote/apropos.png").resize((30,30))))
        btnApropos.image_names=iconApropos
        btnApropos.configure(image=iconApropos)
        btnPara = Button(frameBottom,bg=self.__mainColor,command=self.__setting)
        iconParametre = ImageTk.PhotoImage((Image.open("asset/icon/copilote/parametre.png").resize((30,30))))
        btnPara.image_names=iconParametre
        btnPara.configure(image=iconParametre)
        btnMicro = Button(frameBottom,width=350,bg=self.__mainColor)
        iconMicro = ImageTk.PhotoImage((Image.open("asset/icon/copilote/microphoneCopilote.png").resize((30,30))))
        btnMicro.image_names=iconMicro 
        btnMicro.configure(image=iconMicro )
        self.__labelDocxOpen = Label(frameBottom,bg=self.__mainColor,fg=self.__textMainColor,font=("arial","13"))
        self.__labelTableurOpen = Label(frameBottom,bg=self.__mainColor,fg=self.__textMainColor,font=("arial","13"))
        # Affichage general
        # Frame
        frameTop.pack(side="top")
        frameReponse.pack()
        frameInput.pack()
        frameBottom.pack(side="bottom")
        # Widget
        labelTitle.place(relx=0.5,rely=0.5,anchor="center")
        labelIconSix.place(x=25,y=25)
        labelIconRyley.place(x=25,y=225)
        self.__labelReponseSix.place(x=90,y=25)
        self.__labelReponseRyley.place(x=90,y=225)
        self.__entryInput.pack(side="left")
        btnSend.pack(side="right")
        input.place(relx=0.5,rely=0.5,anchor="center")
        btnApropos.place(relx=0, rely=0.5, anchor="w")
        btnMicro.place(relx=0.5,rely=0.5,anchor="center")
        btnPara.place(relx=1, rely=0.5, anchor="e")
        self.__labelDocxOpen.place(x=40, y=10)
        self.__labelTableurOpen.place(x=535, y=10)


    def active(self):
        self.__bootCopilote()
        self.__screen.mainloop()

    def __bootCopilote(self):
        self.__ryleySpeak(self.__assistantRyley.boot())
        self.__sixSpeak(self.__assistantSix.boot())

    def __envoie(self):
        reponse =  self.__entryInput.get()
        textSix = str
        textRyley = str
        listReponseRyley = ["C'est Six que peux te repondre sur cette question ","Je peux pas te repondre. Regardes la reponse de Six "]
        listReponseSix = ["C'est Ryley que peux vous repondre sur cette question ","Je peux pas vous repondre. Regardez la reponse de Ryley "]
        self.__entryInput.delete(0,END)
        varSortie = int 
        varSortie,sortieNeuronCopilote = self.__copiloteNeuron.neuron(reponse)
        if (varSortie == 0) :
            varSortie, sortieRyley = self.__assistantRyley.neuron(reponse)
            if (varSortie==0):
                requette = chaine.netoyage(reponse)
                if(("ajouter un rendez-vous" in requette) or 
                   ("ajout un rendez-vous"  in requette) or ("ajout evenement" in requette) 
                   or ("ajout rappel" in requette) or ("ajout un evenement" in requette) 
                   or ("ajout un rappel" in requette) or ("ajouter un evenement" in requette) 
                   or ("ajouter  un rappel" in requette) or ("suppr un rendez-vous" in requette) 
                   or ("supprimer un rendez-vous"  in requette) or ("suppr evenement" in requette)
                   or ("suppr rappel" in requette) or ("suppr un evenement" in requette) 
                   or ("suppr un rappel" in requette) or ("supprimer un evenement" in requette) 
                   or ("supprimer un rappel" in requette) or ("evenement d'aujourd'hui" in requette) 
                   or ("evenement du jour" in requette) or ("rendez-vous d'aujourd'hui" in requette )
                   or ("rappel aujourd'hui" in requette)):
                    varSortie = 0 
                    sortieSix = ["",""]
                else :
                    varSortie, sortieSix = self.__assistantSix.neuron(reponse)
                if (varSortie == 0) :
                    textSix = "Il est impossible pour moi et mon frere de vous repondre"
                    textRyley = "Il est impossible pour moi et ma soeur de te repondre"    
                else:
                    textSix = sortieSix[0]
                    textRyley = listReponseRyley[random.randint(0,1)]
            else :
                textRyley = sortieRyley[0]
                textSix = listReponseSix[random.randint(0,1)]
        else :
            textSix = sortieNeuronCopilote[0]
            textRyley = sortieNeuronCopilote[1]
        if(varSortie==12):                  
            textSix = sortieSix[0]+"\n"+sortieSix[1]+"\n"+"La fete du jour est : "+sortieSix[2]
            textRyley = sortieSix[3]+"\n"+sortieSix[4]+"\n"+sortieSix[5]
        if (varSortie==3):
            textSix = "Les actualités du jour sont "+sortieSix[0]+"\n"+sortieSix[1]+"."
            textRyley = "Et la derniere est "+sortieSix[2]
        self.__sixSpeak(textSix)
        self.__ryleySpeak(textRyley)
        self.__testFichierOpen()
    
    def __Apropop(self):
        #Variable
        nameApp = "Arrera Copilote"#Definir le nom de l'app
        versionApp = "I2024-1.00-dev"#Definir le nom de la version
        imagePath = self.__emplacementIconCopilote #Indiquer l'emplacement de l'icon
        copyrightApp = "Copyright Arrera Software by Baptiste P 2023-2024"
        color = self.__mainColor
        #Creation de la fenetre
        about = Toplevel()
        about.title("A propos : "+nameApp)
        about.maxsize(400,300)
        about.minsize(400,300)
        about.configure(bg=color)
        about.iconphoto(False,PhotoImage(file=imagePath))
        #Traitement Image
        icon = ImageTk.PhotoImage(Image.open(imagePath).resize((100,100)))
        #Label
        labelIcon = Label(about,bg=color)
        labelIcon.image_names = icon
        labelIcon.configure(image=icon)
        labelName = Label(about,text="\n"+nameApp+"\n",font=("arial","12"),bg=color)
        labelVersion = Label(about,text=versionApp+"\n",font=("arial","11"),bg=color)
        labelCopyright = Label(about,text=copyrightApp,font=("arial","9"),bg=color)
        #affichage
        labelIcon.pack()
        labelName.pack()
        labelVersion.pack()
        labelCopyright.pack()

    def __ryleySpeak(self,texte:str):
        self.__labelReponseRyley.configure(text=texte, justify="left",wraplength=600)
        
    
    def __sixSpeak(self,texte:str):
        self.__labelReponseSix.configure(text=texte, justify="left",wraplength=600)
    
    def __setting(self):
        parametre = Toplevel()
        self.__parametre.windows(parametre,"light")
    
    def __verifBoot(self):
        if not jsonWork("configuration/configUser.json").lectureJSON("user") and not jsonWork("configuration/configUser.json").lectureJSON("genre") :
            return False
        else :
            return True

    def __bootWithLynx(self):
        screen =  Tk()
        lynx = ArreraLynx(screen,jsonWork("configuration/lynx.json"),jsonWork("configuration/configUser.json"),jsonWork("configuration/six.json"))
        lynx.active()
        screen.mainloop()

    def __testFichierOpen(self):
        if(self.__copiloteNeuron.getDocOpen()==True):
            self.__labelDocxOpen.configure(text="Document ouvert") 
        else :
            self.__labelDocxOpen.configure(text="")     
        if(self.__copiloteNeuron.getTableurOpen()==True):
            self.__labelTableurOpen.configure(text="Tableur ouvert")
        else :
            self.__labelTableurOpen.configure(text="")