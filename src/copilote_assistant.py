from brain.brain import ABrain,confNeuron
from lynx_gui.arrera_lynx import arrera_lynx
from src.copilote_gui import copilote_gui
from src.version_demon import demon,soft_config
from lib.arrera_tk import *

THEME_FILE = "asset/theme/theme_bleu_violet.json"

SOFT_CONF = soft_config(
    name_soft="arrera-copilote",
    version="I2026-0.00"
)

class copilote_assistant():
    def __init__(self):
        self.__conf_ryley = confNeuron(
            name="Arrera Copilote Ryley",
            lang="fr",
            asset="asset/",
            icon="asset/icone/six-ryley/ryley.png",
            assistant_color="#041f75",
            assistant_texte_color="white",
            bute="",
            createur="Baptiste P",
            listFonction=[],
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
            lienDoc="www.google.com", # TODO : A changer plus tart
            fichierLangue="language/tutoiment/", # Path to language files
            fichierKeyword="keyword/",            # Path to keyword files
            voiceAssistant=False
        )

        self.__conf_six = confNeuron(
            name="Arrera Copilote Six",
            lang="fr",
            asset="asset/",
            icon="asset/icone/six-ryley/six.png",
            assistant_color="#e0e0e0",
            assistant_texte_color="black",
            bute="",
            createur="Baptiste P",
            listFonction=[],
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
            lienDoc="www.google.com", # TODO : A changer plus tart
            fichierLangue="language/vouvoiment/", # Path to language files
            fichierKeyword="keyword/",            # Path to keyword files
            voiceAssistant=True
        )

        # Demon de MAJ
        self.__demon = demon(SOFT_CONF, "https://arrera-software.fr/depots.json")

        # Demarage du reseau de neuron
        self.__six = ABrain(self.__conf_six)
        self.__ryley = ABrain(self.__conf_ryley)

        self.__gestionnaire = self.__six.getGestionnaire()

        # Var
        self.__firt_boot = self.__gestionnaire.getUserConf().getFirstRun()
        self.__state_conf = False

    def active(self):
        if self.__firt_boot:
            l = arrera_lynx(self.__gestionnaire,
                            "json_conf/configLynx.json",
                            THEME_FILE)
            self.__state_conf = l.return_state_lynx()
        else :
            self.__state_conf = True
        self.__boot()

    def __boot(self):
        if not self.__state_conf:
            w = aTk(title="Arrera Copilote", resizable=False, width=500, height=350,
                    theme_file=THEME_FILE)
            img_cavas = aBackgroundImage(w,
                                         background_dark="asset/GUI/dark/no_config.png",
                                         background_light="asset/GUI/light/no_config.png",
                                         width=500, height=350)
            label_text = aLabel(w, text="Désoler mais vous avez pas configuer l'assistant correctement",
                                police_size=20, fg_color="#452446",
                                text_color="white", wraplength=300, justify="left")
            btn_conf = aButton(w, text="Configurer",
                               size=20, command=lambda: self.__restartConf(w))
            img_cavas.pack()
            label_text.place(x=190, y=40)
            btn_conf.placeBottomCenter()
            w.mainloop()
        else :
            assistant = copilote_gui(iconFolder="asset/icone/",
                                     iconName="icon",
                                     six_brain=self.__six,
                                     ryley_brain=self.__ryley,
                                     theme_file=THEME_FILE,
                                     version=self.__demon.getVersionSoft())
            assistant.active(self.__firt_boot,self.__demon.checkUpdate())

    def __restartConf(self,windows:aTk):
        windows.destroy()
        self.active()