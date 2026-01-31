from dataclasses import dataclass, field
from typing import List

@dataclass
class confNeuron:
    name: str
    lang: str
    icon: str
    asset:str
    assistant_color: str
    assistant_texte_color: str
    bute: str
    createur: str
    listFonction: List[str] = field(default_factory=list)
    moteurderecherche: str = ""
    etatService: int = 0
    etatTime: int = 0
    etatOpen: int = 0
    etatSearch: int = 0
    etatChatbot: int = 0
    etatApi: int = 0
    etatCodehelp: int = 0
    etatWork: int = 0
    etatSocket: int = 0
    lienDoc: str = ""
    fichierLangue:str = ""
    fichierKeyword:str = ""
    voiceAssistant:bool = False