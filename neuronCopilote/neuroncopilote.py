from ObjetsNetwork.arreraNeuron import*
from copilotefonction.copiloteTableur import*

class neuronCopilote : 
    def __init__(self,configUser):
        self.__jsonUser = jsonWork(configUser)
        self.__fncTableur = CArreraCopiloteTableurGUI()
    
    def neuron(self,var:str):
        statement = chaine.netoyage(var)
        if "tu es qui" in statement or "présente toi" in statement or "présentation" in statement or "qui es tu" in statement or "qui es tu" in statement or "vous etes qui" in statement :
            sortie=[
                "Je suis SIX un assistant personnel développer par Arrera Software",
                "Et moi je suis Ryley le frere de Six. Et a deux nous avons pour but d'optimiser votre façon de travailler"
                ]
            nb = 1 
        else :
            if ("tableur graphique" in statement):
                sortie = ["Okay je vous ouvre le logiciel d'edition de tableur","J'espere que sa te sera utile"]
                self.__fncTableur.active()
                nb = 1 
            else : 
                if ("ouvre un fichier tableur"in statement):
                    sortie = ["La fonction n'est pas encore developper","Je suis desoler "+self.__jsonUser.lectureJSON("user")]
                    nb = 1
                else :
                    sortie = ["",""]
                    nb = 0 
        
        return nb , sortie