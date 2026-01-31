from neuron.CNeuronBase import neuronBase,gestionnaire
import random
from datetime import time,datetime

class interface(neuronBase):
    def __init__(self,gestionnaire:gestionnaire) -> None:
        super().__init__(gestionnaire)

    def neurone(self,requette:str):
        if self._keyword.checkInterface(requette,"erreuropensoft") :
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseInterfaceOpenSoft("2"),""]
        elif self._keyword.checkInterface(requette,"noopensoft") :
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseInterfaceOpenSoft("3"),""]
        elif self._keyword.checkInterface(requette,"opensoft") :
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseInterfaceOpenSoft("1"),""]
        elif self._keyword.checkInterface(requette,"breef"):
            if time(6,0) <= datetime.now().time() < time(11,0):
                texte = self._language.getPhraseMorningBreef("1")
                self._gestGUI.activeBreef()
                outInt = 19
            else :
                out = self._gestFNC.getFNCBreef().summarizeAll()
                texte = self._language.getPhraseResumerAll("2")
                if out is not None:
                    outInt = 19
                    self._gestGUI.activeViewResumer(dict=out,list=None,intIn=outInt)
                else :
                    outInt = 20
            self._listSortie = [texte,""]
            self._valeurOut = outInt

        elif self._keyword.checkInterface(requette,"meteo"):
            state = self._gestFNC.getFNCMeteo().getMeteoCurrentHour()
            if state:
                texte =  self._language.getPhraseMeteo(str(random.randint(5, 6)),
                                                       self._gestFNC.getFNCMeteo().getNameTown(),
                                                       self._gestFNC.getFNCMeteo().getDescription(),
                                                       self._gestFNC.getFNCMeteo().getTemperature()
                                                     )[random.randint(0, 1)]
            else :
                texte =  self._language.getPhraseMeteoError(str(random.randint(5, 6)))
            self._valeurOut = 0
            self._listSortie = [texte,""]
        elif self._keyword.checkInterface(requette,"task"):
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseTime("9"), ""]
            self._gestGUI.activeTache()
        elif self._keyword.checkInterface(requette,"agenda"):
            self._valeurOut = 1
            self._listSortie = [self._language.getPhraseTime("8"), ""]
            self._gestGUI.activeAgenda()
        elif self._keyword.checkInterface(requette,"modeone"):
            self._valeurOut = 1
            name = requette.replace(self._keyword.getListKeyword("interface","modeone")[0],"").strip()
            self._listSortie = [self._language.getPhraseInterfaceLaunchModeLieu("1",name),""]
            self._gestHist.add_action("open_mode","mode1")
            self._gestionnaire.setModeIsEnabled(True)
        elif self._keyword.checkInterface(requette,"modetwo"):
            self._valeurOut = 1
            name = requette.replace(self._keyword.getListKeyword("interface","modetwo")[0],"").strip()
            self._listSortie = [self._language.getPhraseInterfaceLaunchModeLieu("2",name),""]
            self._gestHist.add_action("open_mode","mode2")
            self._gestionnaire.setModeIsEnabled(True)
        elif self._keyword.checkInterface(requette,"modetheer"):
            self._valeurOut = 1
            name = requette.replace(self._keyword.getListKeyword("interface","modetheer")[0],"").strip()
            self._listSortie = [self._language.getPhraseInterfaceLaunchModeLieu("3",name),""]
            self._gestHist.add_action("open_mode","mode3")
            self._gestionnaire.setModeIsEnabled(True)
        elif self._keyword.checkInterface(requette,"modefoor"):
            self._valeurOut = 1
            name = requette.replace(self._keyword.getListKeyword("interface","modefoor")[0],"").strip()
            self._listSortie = [self._language.getPhraseInterfaceLaunchModeLieu("4",name),""]
            self._gestHist.add_action("open_mode","mode4")
            self._gestionnaire.setModeIsEnabled(True)
        elif self._keyword.checkInterface(requette,"modefive"):
            self._valeurOut = 1
            name = requette.replace(self._keyword.getListKeyword("interface","modefive")[0],"").strip()
            self._listSortie = [self._language.getPhraseInterfaceLaunchModeLieu("5",name),""]
            self._gestHist.add_action("open_mode","mode5")
            self._gestionnaire.setModeIsEnabled(True)
        elif self._keyword.checkInterface(requette,"modesix"):
            self._valeurOut = 1
            name = requette.replace(self._keyword.getListKeyword("interface","modesix")[0],"").strip()
            self._listSortie = [self._language.getPhraseInterfaceLaunchModeLieu("6",name),""]
            self._gestHist.add_action("open_mode","mode6")
            self._gestionnaire.setModeIsEnabled(True)
        elif self._keyword.checkInterface(requette,"errorlaunchmode"):
            self._valeurOut = 1
            self._listSortie = ["Erreur mode",""]
        elif self._keyword.checkInterface(requette,"closemode"):
            self._valeurOut = 1
            name = requette.replace(self._keyword.getListKeyword("interface","closemode")[0],"").strip()
            self._listSortie = [self._language.getPhraseCloseMode(),""]
            self._gestHist.add_action("close_mode",name)
            self._gestionnaire.setModeIsEnabled(False)
        elif self._keyword.checkInterface(requette,"close"):
            self._valeurOut = 15