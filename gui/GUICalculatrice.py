from tkinter import PhotoImage, END
import customtkinter as ctk
from tkinter.messagebox import showerror
from gui.guibase import GuiBase,gestionnaire
import math

class GUICalculatrice(GuiBase) :
    def __init__(self,gestionnaire:gestionnaire):
        super().__init__(gestionnaire,"Calculatrice")
        self.__operateurChooseComplex = ""

    def _mainframe(self):
        self._screen.minsize(500,500)
        self._screen.grid_rowconfigure(0, weight=1)
        self._screen.grid_columnconfigure(0, weight=1)
        #cadre
        # Partie calculatrice
        self.__mainView = self._arrtk.createFrame(self._screen)
        fclavier = self._arrtk.createFrame(self.__mainView)
        # Partie historique
        self.__fhistorique = self._arrtk.createFrame(self._screen)
        # Partie Complex
        self.__fComplex = self._arrtk.createFrame(self._screen)
        fEntryNB1 = self._arrtk.createFrame(self.__fComplex)
        fOperateurComplex = self._arrtk.createFrame(self.__fComplex)
        fEntryNB2 = self._arrtk.createFrame(self.__fComplex)
        # Partie pythagore
        self.__fPythagore = self._arrtk.createFrame(self._screen)

        # Configuration des frame
        fclavier.grid_columnconfigure(0, weight=1, uniform="col")
        fclavier.grid_columnconfigure(1, weight=1, uniform="col")
        fclavier.grid_columnconfigure(2, weight=1, uniform="col")
        fclavier.grid_columnconfigure(3, weight=1, uniform="col")
        fclavier.grid_columnconfigure(4, weight=1, uniform="col")
        fclavier.grid_columnconfigure(5, weight=1, uniform="col")
        fclavier.grid_columnconfigure(6, weight=1, uniform="col")

        fclavier.grid_rowconfigure(0, weight=1)
        fclavier.grid_rowconfigure(1, weight=1)
        fclavier.grid_rowconfigure(2, weight=1)
        fclavier.grid_rowconfigure(3, weight=1)
        fclavier.grid_rowconfigure(4, weight=1)
        fclavier.grid_rowconfigure(5, weight=1)
        fclavier.grid_rowconfigure(6, weight=1)

        self.__mainView.grid_rowconfigure(0, weight=1)  # la zone texte prend de la place en vertical
        self.__mainView.grid_rowconfigure(1, weight=2)  # la zone clavier peut prendre plus
        self.__mainView.grid_columnconfigure(0, weight=1)

        self.__fhistorique.grid_columnconfigure(0, weight=1)
        self.__fhistorique.grid_rowconfigure(0, weight=1)
        self.__fhistorique.grid_rowconfigure(1, weight=3)

        self.__fComplex.grid_columnconfigure(0, weight=1)
        self.__fComplex.grid_rowconfigure(1, weight=1)
        self.__fComplex.grid_rowconfigure(6, weight=1)

        self.__fPythagore.grid_columnconfigure(0, weight=1)
        self.__fPythagore.grid_columnconfigure(1, weight=0)
        self.__fPythagore.grid_columnconfigure(2, weight=0, minsize=60)
        self.__fPythagore.grid_columnconfigure(3, weight=0)
        self.__fPythagore.grid_columnconfigure(4, weight=1)
        self.__fPythagore.grid_rowconfigure(3, weight=1)

        # widget
        self.__zoneCalcule = self._arrtk.createText(self.__mainView, ptaille=30,
                                                    ppolice="Arial", pstyle="bold", center=True)
        #touche clavier
        #chiffre
        btnNb0 = self._arrtk.createButton(fclavier,text="0", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("0"),pstyle="bold",ptaille=20)
        btnNb1 = self._arrtk.createButton(fclavier,text="1", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("1"),pstyle="bold",ptaille=20)
        btnNb2 = self._arrtk.createButton(fclavier,text="2", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("2"),pstyle="bold",ptaille=20)
        btnNb3 = self._arrtk.createButton(fclavier,text="3", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("3"),pstyle="bold",ptaille=20)
        btnNb4 = self._arrtk.createButton(fclavier,text="4", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("4"),pstyle="bold",ptaille=20)
        btnNb5 = self._arrtk.createButton(fclavier,text="5", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("5"),pstyle="bold",ptaille=20)
        btnNb6 = self._arrtk.createButton(fclavier,text="6", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("6"),pstyle="bold",ptaille=20)
        btnNb7 = self._arrtk.createButton(fclavier,text="7", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("7"),pstyle="bold",ptaille=20)
        btnNb8 = self._arrtk.createButton(fclavier,text="8", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("8"),pstyle="bold",ptaille=20)
        btnNb9 = self._arrtk.createButton(fclavier,text="9", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("9"),pstyle="bold",ptaille=20)
        btnPI = self._arrtk.createButton(fclavier,text="PI", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("3.1415926535897932"),pstyle="bold",ptaille=20)
        # operateur
        btnVirgule = self._arrtk.createButton(fclavier,text=".", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("."),pstyle="bold",ptaille=20)
        btnPuissanceDix = self._arrtk.createButton(fclavier,text="10^", bg=self._btnColor, fg=self._btnTexteColor,
                                        command= lambda : self.__ecritureCarractere("*10**"),pstyle="bold",ptaille=20)
        btnEgal = self._arrtk.createButton(fclavier,text="=", bg=self._btnColor, fg=self._btnTexteColor,
                                command=self.__calcule,pstyle="bold",ptaille=30)
        btnplus = self._arrtk.createButton(fclavier,text="+", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("+"),pstyle="bold",ptaille=30)
        btnMoin = self._arrtk.createButton(fclavier,text="-", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("-"),pstyle="bold",ptaille=30)
        btnFois = self._arrtk.createButton(fclavier,text="*", bg=self._btnColor, fg=self._btnTexteColor,
                                command= lambda : self.__ecritureCarractere("*"),pstyle="bold",ptaille=30)
        btnDiviser = self._arrtk.createButton(fclavier,text="/", bg=self._btnColor, fg=self._btnTexteColor,
                                   command= lambda : self.__ecritureCarractere("/"),pstyle="bold",ptaille=30)
        btnParenthese1 = self._arrtk.createButton(fclavier,text="(", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("("),pstyle="bold",ptaille=30)
        btnParenthese2 = self._arrtk.createButton(fclavier,text=")", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere(")"),pstyle="bold",ptaille=30)
        btnRacine = self._arrtk.createButton(fclavier,text="sqrt", bg=self._btnColor, fg=self._btnTexteColor,
                                  command= lambda : self.__ecritureCarractere("math.sqrt("),pstyle="bold",ptaille=20)
        btnExposant = self._arrtk.createButton(fclavier,text="^", bg=self._btnColor, fg=self._btnTexteColor,
                                    command= lambda : self.__ecritureCarractere("**"),pstyle="bold",ptaille=30)
        btnExpodentiel = self._arrtk.createButton(fclavier,text="e^", bg=self._btnColor, fg=self._btnTexteColor,
                                       command= lambda : self.__ecritureCarractere("math.exp("),pstyle="bold",ptaille=30)
        btnLN = self._arrtk.createButton(fclavier,text="ln", bg=self._btnColor, fg=self._btnTexteColor,
                              command= lambda : self.__ecritureCarractere("math.log(x,math.e)"),pstyle="bold",ptaille=20)
        btnLOG = self._arrtk.createButton(fclavier,text="log", bg=self._btnColor, fg=self._btnTexteColor,
                               command= lambda : self.__ecritureCarractere("math.log(x,10)"),pstyle="bold",ptaille=20)
        #cercle trigo
        btnSIN = self._arrtk.createButton(fclavier,text="SIN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.sin("),pstyle="bold",ptaille=20)
        btnCOS = self._arrtk.createButton(fclavier,text="COS", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda : self.__ecritureCarractere("math.cos("),pstyle="bold",ptaille=20)
        btnTAN = self._arrtk.createButton(fclavier,text="TAN", bg=self._btnColor, fg=self._btnTexteColor,
                               command=lambda :self.__ecritureCarractere("math.tan("),pstyle="bold",ptaille=20)
        btnARCSIN = self._arrtk.createButton(fclavier,text="SIN-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.asin("),pstyle="bold",ptaille=18)
        btnARCCOS = self._arrtk.createButton(fclavier,text="COS-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.acos("),pstyle="bold",ptaille=18)
        btnARCTAN = self._arrtk.createButton(fclavier,text="TAN-1", bg=self._btnColor, fg=self._btnTexteColor,
                                  command=lambda : self.__ecritureCarractere("math.cos("),pstyle="bold",ptaille=18)
        #autre
        btnClear = self._arrtk.createButton(fclavier,text="C",command=self.__clearAll,
                                                   bg=self._btnColor, fg=self._btnTexteColor,pstyle="bold",ptaille=20)
        btnSuppr = self._arrtk.createButton(fclavier,text="CE",bg=self._btnColor,
                                                   fg=self._btnTexteColor,command=self.__suppr,pstyle="bold",ptaille=20)
        #btn fonction special
        btnAngle = self._arrtk.createButton(fclavier, text="Randian en degres", ppolice="Arial",pstyle="bold",ptaille=14
                                                   , bg=self._btnColor, fg=self._btnTexteColor, command=self.__convertiseurDegRad)
        btnPythagore = self._arrtk.createButton(fclavier, text="Theoreme de pythagore", ppolice="Arial",pstyle="bold",ptaille=16
                                                       , bg=self._btnColor, fg=self._btnTexteColor,command=self.__viewPythagore)
        btnNbComplex = self._arrtk.createButton(fclavier, text="Nombre Complex", ppolice="Arial",pstyle="bold",ptaille=15
                                                     , bg=self._btnColor, fg=self._btnTexteColor,command=self.__viewComplex)
        btnHist = self._arrtk.createButton(fclavier, text="Historique", ppolice="Arial",pstyle="bold",ptaille=20
                                          , bg=self._btnColor, fg=self._btnTexteColor,command=self.__viewHistorique)

        # Frame Historique
        labelHist = self._arrtk.createLabel(self.__fhistorique, text="Historique",
                                            ppolice="Arial", ptaille=20)
        self.__affichageHistorique = self._arrtk.createText(self.__fhistorique)
        scroll_y = ctk.CTkScrollbar(self.__fhistorique, orientation="vertical", command=self.__affichageHistorique.yview)
        self.__affichageHistorique.configure(state='disabled')
        btnBackHist = self._arrtk.createButton(self.__fhistorique, text="Retour", ppolice="Arial", ptaille=25,
                                               bg=self._btnColor, fg=self._btnTexteColor,
                                               command=self.__viewCalcule)

        # Frame Complex
        lTitleNombreComplex = self._arrtk.createLabel(self.__fComplex, text="Nombre Complex",
                                                      ppolice="Arial", ptaille=25, pstyle="bold")

        lComplexNB1 = self._arrtk.createLabel(fEntryNB1, text=" j ", ppolice="Arial", ptaille=20)
        self.__entryComplexNB1_1 = self._arrtk.createEntry(fEntryNB1, ppolice="Arial", ptaille=20)
        self.__entryComplexNB1_2 = self._arrtk.createEntry(fEntryNB1, ppolice="Arial", ptaille=20)

        lComplexNB2 = self._arrtk.createLabel(fEntryNB2, text=" j ", ppolice="Arial", ptaille=20)
        self.__entryComplexNB2_1 = self._arrtk.createEntry(fEntryNB2, ppolice="Arial", ptaille=20)
        self.__entryComplexNB2_2 = self._arrtk.createEntry(fEntryNB2, ppolice="Arial", ptaille=20)

        # Bouton operateur Complex
        btnComplexPlus = self._arrtk.createButton(fOperateurComplex, text="+", ppolice="Arial", ptaille=30,
                                                  bg=self._btnColor, fg=self._btnTexteColor,command=self.__additionComplex)
        btnComplexMoin = self._arrtk.createButton(fOperateurComplex, text="-", ppolice="Arial", ptaille=30,
                                                  bg=self._btnColor, fg=self._btnTexteColor,command=self.__soustrationComplex)
        btnComplexFois = self._arrtk.createButton(fOperateurComplex, text="*", ppolice="Arial", ptaille=30,
                                                  bg=self._btnColor, fg=self._btnTexteColor,command=self.__multiplicationComplex)
        btnComplexDiv = self._arrtk.createButton(fOperateurComplex, text="/", ppolice="Arial", ptaille=30,
                                                  bg=self._btnColor, fg=self._btnTexteColor,command=self.__divisionComplex)

        # Resultat Complex
        self.__lResultatComplex = self._arrtk.createLabel(self.__fComplex,text="",ppolice="Arial", ptaille=25)

        btnBackComplex = self._arrtk.createButton(self.__fComplex, text="Retour", ppolice="Arial", ptaille=25,
                                                    bg=self._btnColor, fg=self._btnTexteColor,command=self.__viewCalcule)

        # Partie Pythagore
        lTitlePythagore = self._arrtk.createLabel(self.__fPythagore, text="Theoreme de Pythagore",
                                                    ppolice="Arial", ptaille=25, pstyle="bold")
        self.__entryPythagoreNB1 = self._arrtk.createEntry(self.__fPythagore, ppolice="Arial", ptaille=20)
        self.__entryPythagoreNB2 = self._arrtk.createEntry(self.__fPythagore, ppolice="Arial", ptaille=20)
        btnPythagoreTheoreme = self._arrtk.createButton(self.__fPythagore, text="Theoreme", ppolice="Arial", ptaille=20,
                                                        bg=self._btnColor, fg=self._btnTexteColor,command=self.__theoremePythagore)
        btnPythagoreRecibroque = self._arrtk.createButton(self.__fPythagore, text="Réciproque", ppolice="Arial", ptaille=20,
                                                        bg=self._btnColor, fg=self._btnTexteColor,command=self.__reciproquePythagore)
        btnBackPythagore = self._arrtk.createButton(self.__fPythagore, text="Retour", ppolice="Arial", ptaille=20,
                                                    bg=self._btnColor, fg=self._btnTexteColor,command=self.__viewCalcule)

        # Affichage des widgets
        # Clavier
        btnClear.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        btnSuppr.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        btnParenthese1.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        btnParenthese2.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)
        btnDiviser.grid(row=0, column=4, sticky="nsew", padx=2, pady=2)
        btnFois.grid(row=0, column=5, sticky="nsew", padx=2, pady=2)
        btnExposant.grid(row=0, column=6, sticky="nsew", padx=2, pady=2)
        btnRacine.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        btnPuissanceDix.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        btnPI.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        btnVirgule.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
        btnSIN.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)
        btnCOS.grid(row=1, column=5, sticky="nsew", padx=2, pady=2)
        btnTAN.grid(row=1, column=6, sticky="nsew", padx=2, pady=2)
        btnNb7.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        btnNb8.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        btnNb9.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        btnMoin.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
        btnARCSIN.grid(row=2, column=4, sticky="nsew", padx=2, pady=2)
        btnARCCOS.grid(row=2, column=5, sticky="nsew", padx=2, pady=2)
        btnARCTAN.grid(row=2, column=6, sticky="nsew", padx=2, pady=2)
        btnNb4.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        btnNb5.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        btnNb6.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
        btnplus.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
        btnExpodentiel.grid(row=3, column=4, sticky="nsew", padx=2, pady=2)
        btnLN.grid(row=3, column=5, sticky="nsew", padx=2, pady=2)
        btnLOG.grid(row=3, column=6, sticky="nsew", padx=2, pady=2)
        btnNb1.grid(row=4, column=0, sticky="nsew", padx=2, pady=2)
        btnNb2.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
        btnNb3.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
        btnEgal.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=2, pady=2)
        btnHist.grid(row=4, column=4, rowspan=2, columnspan=3, sticky="nsew", padx=2, pady=2)
        btnNb0.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=2, pady=2)
        btnAngle.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=2, pady=4)
        btnPythagore.grid(row=6, column=2, columnspan=3, sticky="nsew", padx=2, pady=4)
        btnNbComplex.grid(row=6, column=5, columnspan=2, sticky="nsew", padx=2, pady=4)
        # affichage historique
        labelHist.grid(row=0, column=0)
        self.__affichageHistorique.grid(row=1, column=0, sticky="nsew", padx=(10, 0), pady=10)
        scroll_y.grid(row=1, column=1, sticky="ns", padx=(0, 10), pady=10)
        btnBackHist.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        # Affichage MainView
        self.__zoneCalcule.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        fclavier.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 8))
        # Frame Complex
        self.__entryComplexNB1_1.pack(side="left")
        self.__entryComplexNB1_2.pack(side="left")
        lComplexNB1.pack(side="left")

        self.__entryComplexNB2_1.pack(side="left")
        self.__entryComplexNB2_2.pack(side="left")
        lComplexNB2.pack(side="left")

        btnComplexPlus.pack(side="left")
        btnComplexMoin.pack(side="left")
        btnComplexFois.pack(side="right")
        btnComplexDiv.pack(side="right")

        lTitleNombreComplex.grid(row=0, column=0, sticky="n", padx=10, pady=(10, 0))
        fEntryNB1.grid(row=2, column=0, sticky="n", padx=10, pady=(0, 8))
        fOperateurComplex.grid(row=3, column=0, sticky="n", padx=10, pady=(0, 8))
        fEntryNB2.grid(row=4, column=0, sticky="n", padx=10, pady=(0, 8))
        self.__lResultatComplex.grid(row=5, column=0, sticky="n", padx=10, pady=(0, 8))

        btnBackComplex.grid(row=6, column=0, sticky="ew", padx=10, pady=(0, 10))

        lTitlePythagore.grid(row=0, column=0, columnspan=5, sticky="n", pady=(10, 20))
        self.__entryPythagoreNB1.grid(row=1, column=1, sticky="", padx=(10, 0), pady=(0, 12))
        self.__entryPythagoreNB2.grid(row=1, column=3, sticky="", padx=(0, 10), pady=(0, 12))
        btnPythagoreTheoreme.grid(row=2, column=1, sticky="", padx=(10, 0), pady=(6, 0))
        btnPythagoreRecibroque.grid(row=2, column=3, sticky="", padx=(0, 10), pady=(6, 0))

        btnBackPythagore.grid(row=4, column=0, columnspan=5, sticky="ew", padx=0, pady=(15, 10))

        self.__viewCalcule()
        # Configuration de la zone de calcul
        self.__zoneCalcule.bind("<KeyPress-Return>",self.__enterPressed)
        self.__zoneCalcule.bind("<KeyPress>",self.__carractereInterdit)

    
    def __viewCalcule(self):
        self.__fhistorique.grid_forget()
        self.__fComplex.grid_forget()
        self.__fPythagore.grid_forget()
        self.__mainView.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self._screen.update()

    def __viewHistorique(self):
        self.__mainView.grid_forget()
        self.__fComplex.grid_forget()
        self.__fPythagore.grid_forget()
        self.__fhistorique.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self._screen.update()

    def __viewComplex(self):
        self.__mainView.grid_forget()
        self.__fhistorique.grid_forget()
        self.__fPythagore.grid_forget()
        self.__fComplex.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self._screen.update()

    def __viewPythagore(self):
        self.__mainView.grid_forget()
        self.__fhistorique.grid_forget()
        self.__fComplex.grid_forget()
        self.__fPythagore.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        self._screen.update()

    def __addHistorique(self,texte:str):
        """Ajoute un texte à l'historique de la calculatrice."""
        if not texte:
            return
        self.__affichageHistorique.configure(state='normal')
        self.__affichageHistorique.insert(END, texte + "\n")
        self.__affichageHistorique.see(END)
        self.__affichageHistorique.configure(state='disabled')

    
    def __carractereInterdit(self,event):
        carractereSpeciaux = "'_,?;§!ùµ*£$¤¨@ç|~&²¹#`\°"
        carractereSpeciaux2 = '"'
        if event.char.isalpha():
            return "break"
        elif event.char in carractereSpeciaux:
            return "break"
        elif event.char in carractereSpeciaux2:
            return "break"
        self._arrtk.centerTextOnTextWidget(self.__zoneCalcule)
        
    def __enterPressed(self,event):
        self.__calcule()
        return "break"
        
    def __ecritureCarractere(self,crc:str):
        self.__zoneCalcule.insert("end",crc)
        self._arrtk.centerTextOnTextWidget(self.__zoneCalcule)
        self._screen.update()
        
    def __clearAll(self):
        self.__zoneCalcule.delete("1.0",END)
        self._screen.update()
        
    def __suppr(self):
        # Récupérer le contenu actuel du widget Text
        contenu = self.__zoneCalcule.get("1.0", "end-1c")

        if contenu:
            # Supprimer le dernier caractère
            contenu = contenu[:-1]

            # Mettre à jour le widget Text avec le nouveau contenu
            self.__zoneCalcule.delete("1.0", "end")
            self.__zoneCalcule.insert("1.0", contenu)
            self._arrtk.centerTextOnTextWidget(self.__zoneCalcule)
        self._screen.update()
            
    def __calcule(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        contenu = contenu.replace(" ", "")
        try:
            resultat = eval(contenu)
            self.__affichageHistorique.update()
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(resultat))
            self.__addHistorique(contenu + " = " + str(resultat))
        except Exception as e:
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
        self._screen.update()

    def __convertiseurDegRad(self):
        contenu = self.__zoneCalcule.get("1.0", END)
        if contenu == "":
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere("Erreur 'clear pour uttiliser la calculatrice'")
        else:
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(str(math.degrees(int(contenu))))
        self._screen.update()

    def __additionComplex(self):
        """Additionne deux nombres complexes."""
        try:
            nb1_1 = int(self.__entryComplexNB1_1.get())
            nb1_2 = int(self.__entryComplexNB1_2.get())
            nb2_1 = int(self.__entryComplexNB2_1.get())
            nb2_2 = int(self.__entryComplexNB2_2.get())
            self._gestionnaire.getGestFNC().getFNCCalculatrice().setComplexNb(nb1_1, nb1_2, nb2_1, nb2_2)
            resultat = self._gestionnaire.getGestFNC().getFNCCalculatrice().aditionNbComplex()
            self.__lResultatComplex.configure(text=str(resultat))
        except ValueError:
            showerror("Erreur", "Veuillez entrer des nombres valides.")
        self._screen.update()

    def __soustrationComplex(self):
        """Additionne deux nombres complexes."""
        try:
            nb1_1 = int(self.__entryComplexNB1_1.get())
            nb1_2 = int(self.__entryComplexNB1_2.get())
            nb2_1 = int(self.__entryComplexNB2_1.get())
            nb2_2 = int(self.__entryComplexNB2_2.get())
            self._gestionnaire.getGestFNC().getFNCCalculatrice().setComplexNb(nb1_1, nb1_2, nb2_1, nb2_2)
            resultat = self._gestionnaire.getGestFNC().getFNCCalculatrice().soustrationNbComplex()
            self.__lResultatComplex.configure(text=str(resultat))
        except ValueError:
            showerror("Erreur", "Veuillez entrer des nombres valides.")
        self._screen.update()

    def __multiplicationComplex(self):
        """Additionne deux nombres complexes."""
        try:
            nb1_1 = int(self.__entryComplexNB1_1.get())
            nb1_2 = int(self.__entryComplexNB1_2.get())
            nb2_1 = int(self.__entryComplexNB2_1.get())
            nb2_2 = int(self.__entryComplexNB2_2.get())
            self._gestionnaire.getGestFNC().getFNCCalculatrice().setComplexNb(nb1_1, nb1_2, nb2_1, nb2_2)
            resultat = self._gestionnaire.getGestFNC().getFNCCalculatrice().multiplicationNbComplex()
            self.__lResultatComplex.configure(text=str(resultat))
        except ValueError:
            showerror("Erreur", "Veuillez entrer des nombres valides.")
        self._screen.update()

    def __divisionComplex(self):
        try:
            nb1_1 = int(self.__entryComplexNB1_1.get())
            nb1_2 = int(self.__entryComplexNB1_2.get())
            nb2_1 = int(self.__entryComplexNB2_1.get())
            nb2_2 = int(self.__entryComplexNB2_2.get())
            self._gestionnaire.getGestFNC().getFNCCalculatrice().setComplexNb(nb1_1, nb1_2, nb2_1, nb2_2)
            resultat = self._gestionnaire.getGestFNC().getFNCCalculatrice().divisionNbComplex()
            self.__lResultatComplex.configure(text=str(resultat))
        except ValueError:
            showerror("Erreur", "Veuillez entrer des nombres valides.")
        self._screen.update()

    def __theoremePythagore(self):
        """Calcule le théorème de Pythagore."""
        try:
            a = int(self.__entryPythagoreNB1.get())
            b = int(self.__entryPythagoreNB2.get())
            self._gestionnaire.getGestFNC().getFNCCalculatrice().setNbPythagore(a, b)
            resultat = self._gestionnaire.getGestFNC().getFNCCalculatrice().theoremePythagore()
            calcule = self._gestionnaire.getGestFNC().getFNCCalculatrice().getCalculePythagore()
            self.__viewCalcule()
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(f"{calcule} = {resultat}")
            self.__entryPythagoreNB1.delete(0, END)
            self.__entryPythagoreNB2.delete(0, END)
        except ValueError:
            showerror("Erreur", "Veuillez entrer des nombres valides.")
        self._screen.update()

    def __reciproquePythagore(self):
        """Calcule le théorème de Pythagore."""
        try:
            a = int(self.__entryPythagoreNB1.get())
            b = int(self.__entryPythagoreNB2.get())
            self._gestionnaire.getGestFNC().getFNCCalculatrice().setNbPythagore(a, b)
            resultat = self._gestionnaire.getGestFNC().getFNCCalculatrice().reciproquePythagore()
            calcule = self._gestionnaire.getGestFNC().getFNCCalculatrice().getCalculePythagore()
            self.__viewCalcule()
            self.__zoneCalcule.delete("1.0", END)
            self.__ecritureCarractere(f"{calcule} = {resultat}")
            self.__entryPythagoreNB1.delete(0, END)
            self.__entryPythagoreNB2.delete(0, END)
        except ValueError:
            showerror("Erreur", "Veuillez entrer des nombres valides.")
        self._screen.update()

    def activeCalcule(self):
        self.active()
        self.__viewCalcule()

    def activePythagore(self):
        self.active()
        self.__viewPythagore()

    def activeComplex(self):
        self.active()
        self.__viewComplex()