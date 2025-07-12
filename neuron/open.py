from neuron.CNeuronBase import *

class neuroneOpen(neuronBase) :

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self._gestNeuron.getOpen():
            #fonction neuron Open
            if ("ouvre" in requette) or ("ouvrir" in requette):
                if self._fonctionArreraNetwork.openSoftwareAssistant(requette):
                    self._listSortie = [self._fonctionArreraNetwork.sortieOpenSoftware(requette), ""]
                else :
                    if "youtube" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieOpenYoutube(), ""]
                        self._objHistorique.setAction("Ouverture de youtube")
                    else :
                        siteOpen = self._fonctionArreraNetwork.openWebSiteAssistant(requette)
                        if siteOpen:
                            self._listSortie = [self._fonctionArreraNetwork.sortieOpenSite(requette,siteOpen), ""]
                        elif self._gestNeuron.getSocket():
                            if self._socket.getServeurOn():
                                soft = requette.replace("ouvre","").strip()
                                soft = soft.replace("ouvrir","").strip()
                                self._socket.sendData("ouvre " + soft)
                                self._listSortie = [self._language.getPhraseSocket("openSoftSocket").format(softSocket=soft)
                                    ,""]
                        elif self._gestNeuron.getSocket():
                            if self._socket.getServeurOn():
                                soft = requette.replace("ouvrir","").replace("ouvre","").strip()
                                if soft == "":
                                    self._listSortie = [self._fonctionArreraNetwork.sortieNoOpen(), ""]
                                elif soft == "arrera postite" or soft == "postite":
                                    self._listSortie = [self._language.getPhraseSocket("openArreraPostite")
                                        , ""]
                                    self._socket.sendData("ouvre " + "arrerra postite")
                                elif soft == "arrera video download" or soft == "video download":
                                    self._listSortie = [self._language.getPhraseSocket("openArreraVideoDownload")
                                        , ""]
                                    self._socket.sendData("ouvre " + "arrera video download")
                                elif soft == "arrera raccourci" or soft == "raccourci":
                                    self._listSortie = [self._language.getPhraseSocket("openArreraRaccourci")
                                        , ""]
                                    self._socket.sendData("ouvre " + "arrera raccourci")
                                else :
                                    self._socket.sendData("ouvre " + soft)
                                    self._listSortie = [self._language.getPhraseSocket("openSoftSocket").format(softSocket=soft),""]
                        else :
                            self._listSortie = [self._fonctionArreraNetwork.sortieNoOpen(), ""]

            elif "lance" in requette:
                if "europe 1" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(1), ""]
                        self._objHistorique.setAction("Lancement de la radio europe 1")
                elif "europe 2" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(2), ""]
                        self._objHistorique.setAction("Lancement de la radio europe 2")
                elif "france info" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(3), ""]
                        self._objHistorique.setAction("Lancement de la radio france info")
                elif "france inter" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(4), ""]
                        self._objHistorique.setAction("Lancement de la radio france inter")
                elif "france musique" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(5), ""]
                        self._objHistorique.setAction("Lancement de la radio france musique")
                elif "france culture" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(6), ""]
                        self._objHistorique.setAction("Lancement de la radio france culture")
                elif "fun radio" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(8), ""]
                        self._objHistorique.setAction("Lancement de la radio fun radio")
                elif "nrj" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(9), ""]
                        self._objHistorique.setAction("Lancement de la radio nrj")
                elif "rfm" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(10), ""]
                        self._objHistorique.setAction("Lancement de la radio rfm")
                elif "nostalgi" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(11), ""]
                        self._objHistorique.setAction("Lancement de la radio nostalgi")
                elif "skyrock" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(12), ""]
                        self._objHistorique.setAction("Lancement de la radio skyrock")
                elif "rtl" in requette:
                        self._listSortie = [self._fonctionArreraNetwork.sortieStartRadio(13), ""]
                        self._objHistorique.setAction("Lancement de la radio rtl")

            elif (("liste les logiciels" in requette)or("quelles sont les logiciels enregister" in requette)
                    or("quelles sont les logiciel enregister" in requette) or("quelles sont les logiciels enregiste" in requette)
                    or("quelles sont les logiciels enregiste" in requette) or ("fais une liste des logiciel"in requette)
                    or ("fais une liste des logiciels"in requette) or ("liste les logiciel" in requette)):
                        self._listSortie = [self._fonctionArreraNetwork.sortieListLogiciel(), ""]
            elif (("liste les sites" in requette)or("quelles sont les sites enregister" in requette)
                or("quelles sont les site enregister" in requette) or("quelles sont les sites enregiste" in requette)
                or("quelles sont les sites enregiste" in requette) or ("fais une liste des site"in requette)
                or ("fais une liste des sites"in requette) or ("liste les site" in requette)):
                    self._listSortie = [self._fonctionArreraNetwork.sortieListSite(), ""]
            elif ("liste" in requette) and ("radio" in requette):
                self._listSortie = [self._fonctionArreraNetwork.sortieListRadio()
                                     ,"radio"]
                self._valeurOut = 17


            #Mise a jour de la valeur
            if self._valeurOut == 0:
                self._valeurOut = self._gestionNeuron.verrifSortie(self._listSortie[0])