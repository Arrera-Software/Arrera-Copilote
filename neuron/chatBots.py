import datetime
#fichier
from ObjetsNetwork.formule import*
from ObjetsNetwork.gestion import*
from ObjetsNetwork.enabledNeuron import*
from neuron.CNeuronBase import neuronBase


class neuroneDiscution(neuronBase) :
    def __init__(self, fncArreraNetwork:fncArreraNetwork, gestionnaire:gestionNetwork,objHist:CHistorique,gestionnaireFormule:formule):
        #Init objet
        super().__init__(fncArreraNetwork, gestionnaire,objHist)
        self.__formule = gestionnaireFormule
        self._gestNeuron = self._gestionNeuron.getEtatNeuronObjet()
        self.__language = self._gestionNeuron.getLanguageObjet()

    def neurone(self,requette:str):
        #Initilisation des variable nbRand et text et valeur
        self._listSortie = ["", ""]
        self._valeurOut = 0
        if self._gestNeuron.getChatbot() == True :
            #Recuperation de l'heure
            hour = datetime.now().hour
            text = ""
            #Recuperation atribut de l'assistant
            listOldSortie = self._gestionNeuron.getOld()
            oldrequette = listOldSortie[0]
            oldsortie = listOldSortie[1]
            name = self._gestionNeuron.getName()
            #Reponse chat bot
            if  (("salut" in requette)   or ("bonjour" in requette)  or( "bonsoir" in requette)):
                text = self.__formule.bootNoHist(hour)

            elif (("raconter une blague" in requette) or ("raconte moi une blague" in requette) or ("raconte une blague" in requette)) :
                if (("vous etes pas drole" in oldrequette) or( "tu es pas drole" in oldrequette)
                    or ("c'est pas drole" in oldrequette) or ("pas drole" in oldrequette)) :

                    text = self.__language.getPhraseChatBotNormal("ph1Blague")

                else :

                    nbRand = random.randint(0,8)
                    text = self.__language.getBlague(nbRand)+" "+self.__language.getReponseBlague(nbRand)

            elif (("vous etes pas drole" in requette)  or ("tu es pas drole" in requette)
                    or ("c'est pas drole" in requette) or ("pas drole" in requette)) :

                    if (("raconter une blague" in oldrequette) or ("raconte moi une blague" in oldrequette)
                        or ("raconte une blague" in oldrequette) or ("je vous en raconte une" in oldsortie)
                        or ("je t'en raconte une" in oldsortie)):
                        nbRand = random.randint(0,2)
                        text = self.__language.getPhraseChatBotList("ph2Blague")[nbRand]
                    else :
                        nbRand = random.randint(0,1)
                        text = self.__language.getPhraseChatBotList("ph3Blague")[nbRand]

            elif (("Avant de dire sa , laisse t'en raconter une" in oldsortie)
                    or ("Avant de dire sa , laissez-vous en raconter une" in oldsortie)) :

                    if ("non" in requette) :

                        nbRand = random.randint(0,1)
                        text = self.__language.getPhraseChatBotList("ph4Blague")[nbRand]

                    elif ("oui" in requette) :

                            nbRand = random.randint(0,8)
                            text = (self.__language.getPhraseChatBotNormal("ph5Blague") +
                                    self.__language.getBlague(nbRand) + " " +
                                    self.__language.getReponseBlague(nbRand) + " .")

                    elif (("vasy" in requette) or ("comme tu veux" in requette)
                            or ("si vous voulez" in requette)) :

                            nbRand = random.randint(0,8)
                            text = (self.__language.getPhraseChatBotNormal("ph5Blague") +
                                    self.__language.getBlague(nbRand) + " " +
                                    self.__language.getReponseBlague(nbRand) + " .")

                    elif ("pas besoin" in requette) :

                            nbRand = random.randint(0,1)
                            text = self.__language.getPhraseChatBotList("ph6Blague")[nbRand]

            elif (("Je peux vous en racontez une autre" in oldsortie)
                    or ("Je peux t'en raconter une autre" in oldsortie)
                    or ("Si tu veux je peux t'en raconter une autre" in oldsortie)) :
                    if (("vasy" in requette) or ("comme tu veux" in requette) or ("si vous voulez" in requette)) :

                        nbRand = random.randint(0,8)
                        text = self.__language.getPhraseChatBotNormal("ph7Blague")+self.__language.getBlague(nbRand)+" "+self.__language.getReponseBlague(nbRand)+"."

            elif (("Désoler de ne pas etre drole pour vous " in oldsortie)
                    or ("Désoler si je ne suis pas drole" in oldsortie)
                    or ("Désoler de ne pas etre drole pour toi" in oldsortie)) :
                    if ("pas grave" in requette) :
                        text = self.__language.getPhraseChatBotNormal("ph8Blague")

                    elif (("ne sois pas desoler" in requette)
                            or ("c'est tres grave" in requette)) :
                            text = self.__language.getPhraseChatBotNormal("ph9Blague")

            elif (("comment ça va " in requette) or ("ca va" in requette)
                    or ("ça va" in requette) or( "comment vas tu" in requette)
                    or ("comment allez vous" in requette) or ("tu vas bien" in requette)
                    or ("vous allez bien" in requette) or ("est ce que tout va bien" in requette)
                    or ("tout va bien pour toi" in requette) or ("tout va bien pour vous" in requette)):

                    nbRand = random.randint(0,1)
                    text = self.__language.getPhraseChatBotList("ph10Phrase")[nbRand]

            elif (("tu peux me parler de toi" in requette)
                    or ("tu peux te presenter" in requette)
                    or ("presente toi" in requette)) :
                    if (("tu es qui" in oldrequette) or ("présente toi" in oldrequette)
                        or ("présentation" in oldrequette) or ("qui es tu" in oldrequette)
                        or ("qui es tu" in oldrequette)):

                        phrase = self.__language.getPhraseChatBotNormal("ph1Presentation")
                    else :
                        phrase = self.__language.getPhraseChatBotNormal("ph2Presentation")
                    text = "Ok ," + phrase

            elif (("toujours la"  in requette)  or ("es tu la" in requette)
                    or (name in requette) or ("tu es la" in requette)
                    or ("vous étes la" in requette) or ("vous etes la" in requette)) :

                    nbRand = random.randint(0,2)
                    text = self.__language.getPhraseChatBotList("ph1Other")[nbRand]

            elif (("quesque tu peux faire" in requette) or
                        ("tu peux faire quoi" in requette) or
                        ("vous pouvez faire quoi" in requette)) :

                    text = self.__language.getPhraseListeFonction()

            elif ("non" in requette) :
                    text = self.__language.getPhraseChatBotNormal("phNon")

            elif ("oui" in requette) :
                    text = self.__language.getPhraseChatBotNormal("phOui")

            elif ("merci" in requette) :
                    text = self.__language.getPhraseChatBotNormal("phMerci")

            elif  ("ta gueule" in requette or "tais toi" in requette) :
                    text = self.__language.getPhraseChatBotNormal("phTG")

            #Mise a jour de la valeur
            self._valeurOut = self._gestionNeuron.verrifSortie(text)
            #Retour des valeur
            self._listSortie = [text, ""]