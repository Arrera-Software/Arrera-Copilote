from arreraSoftware.fncArreraNetwork import*

class CHistorique :
    def __init__(self,fncArreraNetwork:fncArreraNetwork,gestionnaire:gestionNetwork):
        # Declaration des varriable est de objet
        self.__fileHist = jsonWork(gestionnaire.getEmplacementFileHist())
        self.__dateToday = ""
        self.__dateTowmorow = ""
        self.__objFNCArrera = fncArreraNetwork
        self.__objDate = fncDate()
        self.__dictHist = dict
        self.__histToday = []
        self.__histTowmorow = []
        self.__listAction = []
        
        self.__setDateToday()
        self.__loadFile()

    
    def __setDateToday(self):
        self.__objDate.rafraichisement()
        self.__dateToday = self.__objDate.getDateToday()
        self.__dateTowmorow = self.__objDate.dateTowmoro()
    
    def __loadFile(self):
        self.__dictHist = self.__fileHist.getContenuJSON()
        if (self.__dictHist != {}):
            if (self.__dateToday in self.__dictHist):
                self.__histToday = self.__dictHist[self.__dateToday]
            if (self.__dateTowmorow in self.__dictHist):
                self.__histTowmorow = self.__dictHist[self.__dateTowmorow]
            
            self.__dictHist = {}
            self.__fileHist.writeDictOnJson(self.__dictHist)
    
    def setAction(self,action:str):
        if (action != ""):
            self.__histToday.append(action)
            return True
        else :
            return False
    
    def saveHistorique(self):
        if (self.__histToday != []):
            self.__dictHist[self.__dateToday] = self.__histToday
            self.__fileHist.writeDictOnJson(self.__dictHist)
            return True
        else :
            return False
    
    def verfiHist(self):
        listAction = []
        if (not self.__histTowmorow):
            histTowmorow = False
        else :
            nbTowmorow = len(self.__histTowmorow)-1
            histTowmorow = True 
        
        if (not self.__histToday) :
            histToday = False 
        else :
            nbToday = len(self.__histToday)-1
            histToday = True
            
        if ((histToday == False) and (histTowmorow == False)):
            return False 
        else :
            if ((histToday == True) and (histTowmorow == True)):
                for i in range(0,nbToday+1):
                    sortie = self.__verifAction(self.__histToday[i])
                    if (sortie != "none"):
                        listAction.append(sortie)
                for i in range(0,nbTowmorow+1):
                    sortie = self.__verifAction(self.__histTowmorow[i])
                    if (sortie != "none"):
                        listAction.append(sortie)
                self.__listAction = self.__verifClose(listAction,self.__histToday)
                self.__listAction = self.__verifClose(listAction,self.__histTowmorow)
                
            else :
                if ((histToday == True) and (histTowmorow == False)):
                    for i in range(0,nbToday+1):
                        sortie = self.__verifAction(self.__histToday[i])
                        if (sortie != "none"):
                            listAction.append(sortie)
                    self.__listAction = self.__verifClose(listAction,self.__histToday)
                    
                else :
                    if ((histToday == False) and (histTowmorow == True)):
                        for i in range(0,nbTowmorow+1):
                            sortie = self.__verifAction(self.__histTowmorow[i])
                            if (sortie != "none"):
                                listAction.append(sortie)
                        self.__listAction = self.__verifClose(listAction,self.__histTowmorow)           
        if (len(self.__listAction) == 0 ):
            return False
        else :
            return True
                        
    
    def __verifClose(self, listAction: list, listHist: list) -> list:
        newListAction = listAction.copy()
        
        for hist_item in listHist:
            if "Fermeture du fichier exel" in hist_item:
                file = hist_item.replace("Fermeture du fichier exel", "").strip()
                actions_to_remove = [
                    f"{file} open computer tableur",
                    f"open exel {file}",
                    f"{file} open tableur assistant"
                ]
            elif "Fermeture du fichier word" in hist_item:
                file = hist_item.replace("Fermeture du fichier word", "").strip()
                actions_to_remove = [
                    f"{file} open computer word",
                    f"open word {file}",
                    f"{file} open word assistant"
                ]
            elif "Fermeture du projet" in hist_item:
                project = hist_item.replace("Fermeture du projet", "").strip()
                actions_to_remove = [f"open projet {project}"]
            else:
                continue
            
            newListAction = [action for action in newListAction if action not in actions_to_remove]
        
        return newListAction
    
    def __verifAction(self,action:str):
        if ("Lancement de la radio" in action):
            radio = action.replace("Lancement de la radio")
            return "radio launch "+radio
        else :
            if ("Ouverture organisateur de varriable" in action):
                return "open orga var"
            else :
                if ("Ouverture selecteur de couleur" in action):
                    return "open select color"
                else :
                    if ("Ouverture de logiciel de gestion github" in action):
                        return "open gest github"
                    else :
                        if ("Ouverture de la librairy codehelp" in action):
                            return "lib codehelp"
                        else :
                            if ("Ouverture du logciel de présentation" in action):
                                return "soft presentation"
                            else :
                                if ("Ouverture du navigateur internet" in action):
                                    return "soft internet"
                                else :
                                    if ("Ouverture du logiciel de note" in action):
                                        return "soft note"
                                    else :
                                        if ("Ouverture du logiciel d'ecoute du musique" in action):
                                            return "soft music"
                                        else :
                                            if ("Ouverture du logiciel" in action):
                                                soft = action.replace("Ouverture du logiciel","")
                                                return "soft "+soft
                                            else :
                                                if ("Ouverture de youtube" in action):
                                                    return "site youtube"
                                                else :
                                                    if ("Ouverture du site de stokage cloud" in action):
                                                        return "site cloud"
                                                    else :
                                                        if ("Ouverture du site" in action):
                                                            site = action.replace("Ouverture du site","")
                                                            return "site "+site
                                                        else :
                                                            if ("Ouverture du logiciel de telechargement en mode video" in action):
                                                                return "soft arrera download video"
                                                            else :
                                                                if ("Ouverture du logiciel de telechargement en mode musique" in action):
                                                                    return "soft arrera download music"
                                                                else :
                                                                    if ("Ouverture de la calculatrice en mode nombre complex" in action):
                                                                        return "calculatrice complex"
                                                                    else :
                                                                        if ("Ouverture de la calculatrice en mode pythagore" in action):
                                                                            return "calculatrice pythagore"
                                                                        else :
                                                                            if ("Ouverture de la calculatrice" in action):
                                                                                return "calculatrice"
                                                                            else :
                                                                                if (("Ouverture du fichier tableur" in action) and ("sur l'ordinateur" in action)):
                                                                                    file = action.replace("Ouverture du fichier tableur","").replace("sur l'ordinateur","").replace(" ","")
                                                                                    return file+" open computer tableur"
                                                                                else :
                                                                                    if (("Ouverture d'un fichier exel" in action) or 
                                                                                        (("Ouverture du fichier tableur" in action) and ("sur l'ordinateur" in action)) or 
                                                                                        (("Ouverture du tableur" in action) and ("dans l'interface de l'assistant" in action))):
                                                                                        file = action.replace("Ouverture d'un fichier exel","").replace(" ","")
                                                                                        file = file.replace("Ouverture du fichier tableur","").replace("sur l'ordinateur","").replace(" ","")
                                                                                        file = file.replace("Ouverture du tableur","").replace("dans l'interface de l'assistant","").replace(" ","")
                                                                                        return "open exel "+file
                                                                                    else :
                                                                                        if (("Ouverture d'un fichier word" in action) or 
                                                                                            (("Ouverture du word" in action) and ("dans l'interface de l'assistant" in action)) or 
                                                                                            (("Ouverture du fichier word" in action) and ("sur l'ordinateur" in action))):
                                                                                            file = action.replace("Ouverture d'un fichier word","").replace(" ","")
                                                                                            file = file.replace("Ouverture du word","").replace("dans l'interface de l'assistant","").replace(" ","")
                                                                                            file = file.replace("Ouverture du fichier word","").replace("sur l'ordinateur","").replace(" ","")
                                                                                            return "open word "+file
                                                                                        else :
                                                                                            if (("Ouverture du projet" in action) or ("Creation d'un projet nommer" in action)):
                                                                                                project = action.replace("Ouverture du projet","").replace("Creation d'un projet nommer","").replace(" ","")
                                                                                                return "open projet "+project 
                                                                                            else :
                                                                                                return "none" 
    
    def startHistAction(self):
        if (len(self.__listAction) == 0):
            return False
        else :
            for i in (0,len(self.__listAction)-1):
                sortie = self.__launchAction(self.__listAction[i])
                if (sortie == False):
                    return False
            return True
            
    def __launchAction(self,action:str):
        if (action != ""):
            match action :
                case "calculatrice"  :
                    self.__objFNCArrera.sortieCalculatrice("0")
                    return True
                case "calculatrice pythagore"  :
                    self.__objFNCArrera.sortieCalculatrice("1")
                    return True
                case "calculatrice complex"  :
                    self.__objFNCArrera.sortieCalculatrice("2")
                    return True
                case "soft arrera download music" :
                    self.__objFNCArrera.sortieDownloadMusic()
                    return True
                case "soft arrera download video" :
                    self.__objFNCArrera.sortieDownloadVideo()
                    return True
                case "radio launch europe 1" :
                    self.__objFNCArrera.sortieStartRadio(1)
                    return True
                case "radio launch europe 2" :
                    self.__objFNCArrera.sortieStartRadio(2)
                    return True
                case "radio launch france info" :
                    self.__objFNCArrera.sortieStartRadio(3)
                    return True
                case "radio launch france inter" :
                    self.__objFNCArrera.sortieStartRadio(4)
                    return True
                case "radio launch france musique" :
                    self.__objFNCArrera.sortieStartRadio(5)
                    return True
                case "radio launch france culture" :
                    self.__objFNCArrera.sortieStartRadio(6)
                    return True
                case "radio launch france bleu" :
                    self.__objFNCArrera.sortieStartRadio(7)
                    return True
                case "radio launch fun radio" :
                    self.__objFNCArrera.sortieStartRadio(8)
                    return True
                case "radio launch nrj " :
                    self.__objFNCArrera.sortieStartRadio(9)
                    return True
                case "radio launch rfm" :
                    self.__objFNCArrera.sortieStartRadio(10)
                    return True
                case "radio launch nostalgi" :
                    self.__objFNCArrera.sortieStartRadio(11)
                    return True
                case "radio launch skyrock" :
                    self.__objFNCArrera.sortieStartRadio(12)
                    return True
                case "radio launch rtl" :
                    self.__objFNCArrera.sortieStartRadio(13)
                    return True
                case "open orga var" :
                    self.__objFNCArrera.sortieOpenOrgaVar()
                    return True
                case "open select color" :
                    self.__objFNCArrera.sortieOpenColorSelecteur()
                    return True
                case "open gest github" :
                    self.__objFNCArrera.sortieOpenGuiGithub()
                    return True
                case "lib codehelp" :
                    self.__objFNCArrera.sortieOpenLibrairy()
                    return True
                case "site youtube" :
                    self.__objFNCArrera.sortieOpenYoutube()
                    return True
            if ("site" in action):
                site = action.replace("site","").replace(" ","")
                return self.__objFNCArrera.openWebSiteAssistant(site)
            else : 
                if ("soft" in action):
                    soft = action.replace("soft","").replace(" ","")
                    return self.__objFNCArrera.openSoftwareAssistant(soft)
                else :
                    if ("open exel" in action):
                        exel = action.replace("open exel","").replace(" ","")
                        self.__objFNCArrera.sortieOpenTableurDirect(exel)
                        return True
                    else :
                        if ("open word" in action):
                            word = action.replace("open word","").replace(" ","")
                            self.__objFNCArrera.sortieOpenWordDirect(word)
                            return True
                        else :
                            if ("open projet" in action):
                                projet = action.replace("open projet","").replace(" ","")
                                self.__objFNCArrera.sortieOpenProjetDirect(projet)
                                return True
                            else :
                                return False
                
        else :
            return False  
        
        
    """
    def __get5oldAction(self,index:int,vlist:list):
        _summary_

        Args:
            index (int): L'index le plus grand possible dans la liste
            vlist (list): La liste
        
        outList = []
        for i in range ((index-5),index):
            outList.append(vlist[i])
        
        return outList
    """                                                                                                                                                   