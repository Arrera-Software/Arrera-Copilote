from ObjetsNetwork.arreraNeuron import*
from PIL import Image, ImageTk

class ArreraCopilote :
    def __init__(self):
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
        btnSend = Button(input,text="Envoyer",bg=self.__mainColor,fg=self.__textMainColor,font=("arial","15"),command=self.__neuron)
        # Widget frameBottom
        btnApropos = Button(frameBottom,bg=self.__mainColor,command=self.__Apropop)
        iconApropos = ImageTk.PhotoImage((Image.open("asset/icon/copilote/apropos.png").resize((30,30))))
        btnApropos.image_names=iconApropos
        btnApropos.configure(image=iconApropos)
        btnPara = Button(frameBottom,bg=self.__mainColor)
        iconParametre = ImageTk.PhotoImage((Image.open("asset/icon/copilote/parametre.png").resize((30,30))))
        btnPara.image_names=iconParametre
        btnPara.configure(image=iconParametre)
        btnMicro = Button(frameBottom,width=350,bg=self.__mainColor)
        iconMicro = ImageTk.PhotoImage((Image.open("asset/icon/copilote/microphoneCopilote.png").resize((30,30))))
        btnMicro.image_names=iconMicro 
        btnMicro.configure(image=iconMicro )
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


    def active(self):
        self.__bootCopilote()
        self.__screen.mainloop()

    def __bootCopilote(self):
        self.__labelReponseRyley.configure(text=self.__assistantRyley.boot())
        self.__labelReponseSix.configure(text=self.__assistantSix.boot())

    def __neuron(self):
        reponse =  self.__entryInput.get()
        self.__entryInput.delete(0,END)
        self.__labelReponseSix.configure(text="")
        self.__labelReponseRyley.configure(text="")
        varSortie = int 
        varSortie, sortieRyley = self.__assistantRyley.neuron(reponse)
        if (varSortie==0):
            varSortie, sortieSix = self.__assistantSix.neuron(reponse)
            if (varSortie==0) :
                reponse = chaine.netoyage(reponse)
                if "tu es qui" in reponse or "présente toi" in reponse or "présentation" in reponse or "qui es tu" in reponse or "qui es tu" in reponse or "vous etes qui" in reponse :
                    self.__labelReponseSix.configure(text="je suis SIX un assistant personnel développer par Arrera Software")
                    self.__labelReponseRyley.configure(text="Et moi je suis Ryley le frere de Six. Et a deux nous avons pour but d'optimiser votre façon de travailler")
                else:
                    radom = random.randint(0,1)
                    if (radom==0):
                        self.__labelReponseSix.configure(text="Il est impossible pour moi et mon frere de vous repondre")
                    else :
                        self.__labelReponseRyley.configure(text="Il est impossible pour moi et ma soeur de te repondre")
            else:
                self.__labelReponseSix.configure(text=sortieSix[0])
        else :
            self.__labelReponseRyley.configure(text=sortieRyley[0])
    
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
        if int(len(texte)) > 6 :
            texte1,texte2 = self.__division(texte,6)
            allTexte = texte1+"\n"+texte2
            if int(len(texte2)) > 6 :
                texte2,texte3 = self.__division(texte2,6)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
                if int(len(texte3)) > 6 :
                    texte3,texte4 = self.__division(texte3,6)
                    allTexte = texte1+"\n"+texte2+"\n"+texte3+"\n"+texte4
        else :
            allTexte = texte
        self.__labelReponseRyley.configure(text=allTexte)
    
    def __sixSpeak(self,texte:str):
        if int(len(texte)) > 6 :
            texte1,texte2 = self.__division(texte,6)
            allTexte = texte1+"\n"+texte2
            if int(len(texte2)) > 6 :
                texte2,texte3 = self.__division(texte2,6)
                allTexte = texte1+"\n"+texte2+"\n"+texte3
                if int(len(texte3)) > 6 :
                    texte3,texte4 = self.__division(texte3,6)
                    allTexte = texte1+"\n"+texte2+"\n"+texte3+"\n"+texte4
        else :
            allTexte = texte
        self.__labelReponseSix.configure(text=allTexte)