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
        btnApropos = Button(frameBottom,bg=self.__mainColor)
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
                radom = random.randint(0,1)
                if (radom==0):
                    self.__labelReponseSix.configure(text="Il est impossible pour moi et mon frere de vous repondre")
                else :
                    self.__labelReponseRyley.configure(text="Il est impossible pour moi et ma soeur de te repondre")
            else:
                self.__labelReponseSix.configure(text=sortieSix[0])
        else :
            self.__labelReponseRyley.configure(text=sortieRyley[0])