from neuronCopilote.neuronCopiloteAngenda import*
from copilotefonction.copiloteTableur import*
from fonctionnalites.arreradocument import*

class neuronCopilote : 
    def __init__(self,configUser):
        self.__jsonUser = jsonWork(configUser)
        self.__fncTableur = CArreraCopiloteTableurGUI()
        self.__neuronAgenda = neuronAgendatCopilote(self.__jsonUser)
        self.__emplacementFileTableur = ""
        self.__emplacementFileDocument = ""
        self.__oldSortie = ""
        self.__fncDocx = None
        self.__fncEcritureTableur = None
        self.__fichierDocxOpen = False
        self.__fichierTableurOpen = False
    
    def __verifCase(self,chaine):
        # Expression régulière pour vérifier la chaîne
        regex = r"^[A-Z]\d$"

        # Vérification de la chaîne avec l'expression régulière
        if re.match(regex, chaine):
            return True
        else:
            return False
    
    def neuron(self,var:str):
        statement = chaine.netoyage(var)
        statementNoClear = var
        nameUser = self.__jsonUser.lectureJSON("user")
        genreUser = self.__jsonUser.lectureJSON("genre")
        if (("tu es qui" in statement) or ("présente toi" in statement) or ("présentation" in statement) 
            or ("qui es tu" in statement) or ("qui es tu" in statement) or ("vous etes qui" in statement)) :
            sortie=["Je suis SIX un assistant personnel développer par Arrera Software",
                "Et moi je suis Ryley le frere de Six. Et a deux nous avons pour but d'optimiser votre façon de travailler"]
            nb = 1 
        else :
            if (("tableur en graphique" in statement)or("tableur graphique" in statement)
                or("fichier exel en graphique"in statement)):
                sortie = self.__fncTableur.activeGUI()
                if(sortie==True):
                    sortie = ["Okay je vous ouvre le logiciel d'edition de tableur","J'espere que sa te sera utile"]
                else :
                    sortie = ["Je ne peux pas ouvrir si vous selectionner pas un fichier "+genreUser+" "+nameUser,
                              "J'espere que sa te sera utile"]
                nb = 1 
            else : 
                if (("ouvre un fichier tableur"in statement)or("ouvre un fichier exel"in statement)
                    or("ouvre un fichier libreoffice calc"in statement)or("ouvre un fichier libre office calc"in statement)):
                    result = messagebox.askquestion(
                                "Choix de l'action", 
                                "Voulez-vous crée un fichier ?")
                    if (result=="yes"):
                        file = filedialog.asksaveasfilename(
                            defaultextension='.xlsx', 
                            filetypes=[("Fichiers Excel", "*.xlsx"),("Fichiers ODF", "*.ods")])  
                    else :
                        file = filedialog.askopenfilename(
                            filetypes=[("Fichiers Excel", "*.xlsx"),("Fichiers ODF", "*.ods")])
                    if (file==""):
                        sortie = ["Je suis desoler  "+genreUser+" "+nameUser+
                                    " mais vous avez pas selection de fichier",
                                    "Selectionne bien un fichier dans la fenetre de l'explorateur de fichier"]
                    else :
                        sortie = ["Okay je vous est ouvert votre fichier tableur "+genreUser+" "+nameUser,
                                "Les fonction qui son possible d'utiliser son :"+
                                "\n-Selectionner un case pour en suite ecrire en nous disant 'selectionne une case'"+
                                "\n-Lire le contennu du tableur en nous disant 'lis le fichier' ou 'lis le tableur'"+
                                "\n- Fermer le tableur en nous disant 'ferme l'exel' ou 'ferme le tableur'"]
                        self.__fncEcritureTableur = CArreraTableur(file)
                        self.__fichierTableurOpen = True
                        self.__emplacementFileTableur = file
                    nb = 1
                else :
                    if((self.__fichierTableurOpen==True)and("selectionne une case"in statement)):
                        sortie = ["Tres bien quelle case vous voulez selectionner ?",
                                  "Marquer juste le numero de case au format Lettre majuscule et numero comme cette exemple 'A1'"]
                        nb = 1
                    else :
                        if(("selectionne une case"in self.__oldSortie)and(self.__fichierTableurOpen==True)
                           and(self. __verifCase(statementNoClear)==True)):
                            sortie = ["Il vous reste plus qu'a suivre les information de l'interface graphique. Et votre vous pourrer modifier votre tableur"
                                      ,"Les fonction qui son possible d'utiliser son :"+
                                        "\n-Selectionner un case pour en suite ecrire en nous disant 'selectionne une case'"+
                                        "\n-Lire le contennu du tableur en nous disant 'lis le fichier' ou 'lis le tableur'"+
                                        "\n- Fermer le tableur en nous disant 'ferme l'exel' ou 'ferme le tableur'"]
                            self.__fncTableur.activeEcritureDirect(statementNoClear,self.__fncEcritureTableur)
                            nb = 1
                        else :
                            if((self.__fichierTableurOpen==True)and("lis le fichier"in statement)
                               or("lis le tableur"in statement)):
                                contenu = self.__fncEcritureTableur.read()
                                text = ""
                                for cell_position, cell_value in contenu.items():
                                    text = text+"\n"+"Cellule "+str(cell_position)+" : "+str(cell_value)
                                sortie = ["Ryley vous montre le contenu du fichier\nJe vous montre les fonction :"+
                                        "\n-Selectionner un case pour en suite ecrire en nous disant 'selectionne une case'"+
                                        "\n-Lire le contennu du tableur en nous disant 'lis le fichier' ou 'lis le tableur'"+
                                       "\n- Fermer le tableur en nous disant 'ferme l'exel' ou 'ferme le tableur'",text]
                                nb = 1 
                            else :
                                if((("ouvre un fichier doc"in statement)or("ouvre un fichier docx"in statement)or("ouvre un fichier traitement de texte"in statement)
                                or("ouvre un fichier word"in statement)or ("ouvre un fichier writer"in statement)or ("ouvre un fichier libre office"in statement)
                                or ("ouvre un document word"in statement)or ("ouvre document libreoffice"in statement)or("ouvre un document"in statement))):
                                    result = messagebox.askquestion(
                                            "Choix de l'action", 
                                            "Voulez-vous crée un fichier ?")
                                    if (result=="yes"):
                                        file = filedialog.asksaveasfilename(
                                            defaultextension='.xlsx', 
                                            filetypes=[('Fichiers Word', '*.docx')])
                                        self.__fncDocx = CArreraDocx(file)
                                        self.__fncDocx.write("")
                                    else :
                                        file = filedialog.askopenfilename(
                                            filetypes=[('Fichiers Word', '*.docx')])
                                        self.__fncDocx = CArreraDocx(file)                             
                                    if (file==""):
                                        sortie = ["Je suis desoler  "+genreUser+" "+nameUser+
                                                " mais vous avez pas selection de fichier","Selectionne bien un fichier dans la fenetre de l'explorateur de fichier"]
                                    else :
                                        sortie = ["Okay je vous est ouvert votre fichier de traitement de texte "+genreUser+" "+nameUser,
                                                "Les fonction qui son possible d'utiliser son :"
                                                +"\n-Ecrire dans le fichier en nous disant 'ecrit dans le document' et en mettant ce que vous voulez ecrire deriere"+
                                                "\n-Lire en nous disant 'lis le document'"+
                                                "\n-Fermer le document en nous disant 'ferme le word' ou 'ferme le document'"]
                                        
                                        self.__fichierDocxOpen = True
                                        self.__emplacementFileDocument = file
                                    nb = 1
                                else :
                                    if ((self.__fichierDocxOpen==True)and("lis le document"in statement)):
                                        sortie = ["Ryley vous montre le contenu du document",
                                                self.__fncDocx.read()]
                                        nb = 1
                                    else :
                                        if ((self.__fichierDocxOpen==True)and("ecrit dans le document"in statement)):
                                            ligne = statement.replace("ecrit dans le document","")
                                            self.__fncDocx.write(ligne)
                                            sortie = ["Okay "+genreUser+" c'est ecrit",
                                                "Okay je vous est ouvert votre fichier de traitement de texte "+genreUser+" "+nameUser,
                                                "Les fonction qui son possible d'utiliser son :"
                                                +"\n-Ecrire dans le fichier en nous disant 'ecrit dans le document' et en mettant ce que vous voulez ecrire deriere"+
                                                "\n-Lire en nous disant 'lis le document'"+
                                                "\n-Fermer le document en nous disant 'ferme le word' ou 'ferme le document'"]
                                            nb = 1
                                        else :
                                            if((self.__fichierTableurOpen==True)and(("ferme le tableur" in statement)or("ferme le exel"in statement))):
                                                del self.__fncEcritureTableur 
                                                self.__fncEcritureTableur = None
                                                self.__fichierTableurOpen = False
                                                sortie = ["Ok je vous ferme le tableur","J'espere que cette fonction a ete utile"]
                                                nb = 1 
                                            else :
                                                if((self.__fichierDocxOpen==True)and(("ferme le document" in statement)or("ferme le word"in statement))):
                                                    self.__fichierDocxOpen = False
                                                    del self.__fncDocx 
                                                    self.__fncDocx = None
                                                    sortie = ["Ok je vous ferme le fichier de traitement de texte","J'espere que cette fonction a ete utile"]
                                                    nb = 1 
                                                else :
                                                    nb , sortie = self.__neuronAgenda.neuron(statement)
                                                    if (nb==0):
                                                        sortie = ["",""]
                                                        nb = 0 
        self.__oldSortie = statement   
        return nb , sortie
        
    def getDocOpen(self):
        return self.__fichierDocxOpen

    def getTableurOpen(self):
        return self.__fichierTableurOpen
    
    def getEmplacementDocument(self):
        return self.__emplacementFileDocument

    def getEmplacementTableur(self):
        return self.__emplacementFileTableur

    def openTableur(self,file:str):
        self.__fncEcritureTableur = CArreraTableur(file)
        self.__fichierTableurOpen = True
        self.__emplacementFileTableur = file
    
    def openDocument(self,file:str):
        self.__fichierDocxOpen = True
        self.__emplacementFileDocument = file
        self.__fncDocx = CArreraDocx(file) 