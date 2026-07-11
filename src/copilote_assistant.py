from brain.brain import confNeuron
from src.copilote_gui import copilote_gui
from config.tiger_demon import tiger_demon

THEME_FILE = "asset/theme/theme_bleu_violet.json"

VERSION = "dev"

class copilote_assistant():
    def __init__(self):
        self.__conf_ryley = confNeuron(
            name="Arrera Copilote Ryley",
            lang="fr",
            asset="asset/",
            icon="asset/icone/linux/icon.png",
            assistant_color="#442446",
            assistant_texte_color="white",
            bute="Je suis un assistant spécialisé dans l'aide au développement et les services utilitaires.",
            createur="Baptiste P",
            listFonction=["Ouvrir une application",
                          "Aider aux recherches sur Internet",
                          "Donner la météo",
                          "Faire un résumé des actualités",
                          "Aider à organiser son travail",
                          "Donner l'heure",
                          "Créer des projets",
                          "Éditer des fichiers Word",
                          "Éditer des tableurs",
                          "Outil d'aide au développement informatique"],
            moteurderecherche="google",
            etatService=1,
            etatTime=1,
            etatOpen=0,
            etatSearch=0,
            etatChatbot=0,
            etatApi=0,
            etatCodehelp=1,
            etatWork=0,
            etatSocket=0,
            lienDoc="https://arrera-software.fr/docCopilote",
            fichierLangue="language/tutoiment/",
            fichierKeyword="keyword/",
            voiceAssistant=False
        )

        self.__conf_six = confNeuron(
            name="Arrera Copilote Six",
            lang="fr",
            asset="asset/",
            icon="asset/icone/linux/icon.png",
            assistant_color="#442446",
            assistant_texte_color="black",
            bute="Je suis un assistant polyvalent pour la recherche, la bureautique et l'ouverture d'applications.",
            createur="Baptiste P",
            listFonction=["Ouvrir une application",
                          "Aider aux recherches sur Internet",
                          "Donner la météo",
                          "Faire un résumé des actualités",
                          "Aider à organiser son travail",
                          "Donner l'heure",
                          "Créer des projets",
                          "Éditer des fichiers Word",
                          "Éditer des tableurs",
                          "Outil d'aide au développement informatique"],
            moteurderecherche="google",
            etatService=0,
            etatTime=0,
            etatOpen=1,
            etatSearch=1,
            etatChatbot=1,
            etatApi=1,
            etatCodehelp=0,
            etatWork=1,
            etatSocket=1,
            lienDoc="https://arrera-software.fr/docRyley",
            fichierLangue="language/vouvoiment/",
            fichierKeyword="keyword/",
            voiceAssistant=True
        )

        # Demon de MAJ
        self.__demon = tiger_demon("copilot",VERSION)


    def active(self):
        self.__boot()

    def __boot(self):
        assistant = copilote_gui(iconFolder="asset/icone/",
                                 iconName="icon",
                                 conf_six=self.__conf_six,
                                 conf_ryley=self.__conf_ryley,
                                 theme_file=THEME_FILE,
                                 version=self.__demon.get_local_version())
        assistant.active(self.__demon.checkUpdate())