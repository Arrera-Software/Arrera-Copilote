import requests
import platform
import os
import json

class model_downloader:
    def __init__(self):

        self.__dictModel = {"leger-gemma":{"name":"Gemma 2B Q5_K_M",
                                           "url":"https://huggingface.co/ironlanderl/gemma-2-2b-it-Q5_K_M-GGUF/resolve/main/gemma-2-2b-it-q5_k_m.gguf?download=true",
                                           "description":"Petit modèle Google Gemma, parfait pour tourner sur un PC sans carte graphique ou NPU."},
                            "leger-llama":{"name":"LLaMA 3.2 1B Q4_K_M",
                                           "url":"https://huggingface.co/hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF/resolve/main/llama-3.2-1b-instruct-q4_k_m.gguf?download=true",
                                           "description":"Petit modèle Meta(Facebook) LLaMA, parfait pour tourner sur un PC sans carte graphique ou NPU."},
                            "leger-mistral":{"name":"Mistral‑Nemo 4B Q4_K_M",
                                             "url":"https://huggingface.co/Nehal07/Mistral-Nemo-Instruct-2407-Q4_K_M-GGUF/resolve/main/mistral-nemo-instruct-2407-q4_k_m.gguf?download=true",
                                             "description":"Petit modèle de Mistral(Boite française), parfait pour tourner sur un PC sans carte graphique ou NPU."},
                            "moyen-gemma":{"name":"Gemma 2 9B Q4_K_M",
                                           "url":"https://huggingface.co/quixotedav/gemma-2-9b-it-Q4_K_M-GGUF/resolve/main/gemma-2-9b-it-q4_k_m.gguf?download=true",
                                           "description":"Modèle Google Gemma de taille moyenne, parfait pour tourner sur un PC avec une carte graphique ou équipé de NPU."},
                            "moyen-llama":{"name":"LLaMA 3.1 8B Q4_K_M",
                                           "url":"https://huggingface.co/YorkieOH10/Meta-Llama-3.1-8B-Instruct-hf-Q4_K_M-GGUF/resolve/main/meta-llama-3.1-8b-instruct-hf-q4_k_m.gguf?download=true",
                                           "description":"Modèle Meta(Facebook) LLaMA de taille moyenne, parfait pour tourner sur un PC avec une carte graphique ou équipé de NPU."},
                            "moyen-mistral":{"name":"Mistral‑7B Instruct v0.3 Q4_K_M",
                                             "url":"https://huggingface.co/jfer1015/Mistral-7B-Instruct-v0.3-Q4_K_M-GGUF/resolve/main/mistral-7b-instruct-v0.3-q4_k_m.gguf?download=true",
                                             "description":"Modèle de Mistral(Boite française) de taille moyenne, parfait pour tourner sur un PC avec une carte graphique ou équipé de NPU."},
                            "lourd-gemma":{"name":"Gemma 3 27B en FP16",
                                           "url":"https://huggingface.co/ALHAJERI/gemma_3_27b_endo_finetuned_fp16-gguf/resolve/main/gemma_3_27b_endo_finetuned_merged_fp16.gguf?download=true",
                                           "description":"Modèle Google Gemma 3, lourd pour les PC avec une carte graphique de 12 Go de NVRAM ou plus."},
                            "lourd-llama":{"name":"LLaMA 3.1 34B FP16",
                                           "url":"https://huggingface.co/TheBloke/CodeLlama-34B-Instruct-GGUF/resolve/main/codellama-34b-instruct.Q4_0.gguf?download=true",
                                           "description":"Modèle Meta(Facebook) LLaMA 3.1, lourd pour les PC avec une carte graphique de 12 Go de NVRAM ou plus."},
                            "lourd-mistral":{"name":"Mixtral 8x22B Q4_K_M",
                                             "url":"https://huggingface.co/bartowski/Mixtral-8x22B-v0.1-GGUF/resolve/main/Mixtral-8x22B-v0.1-IQ3_M-00001-of-00005.gguf?download=true",
                                             "description":"Modèle de Mistral(Boite française), lourd pour les PC avec une carte graphique de 12 Go de NVRAM ou plus."}}

        os_name = platform.system()

        if os_name == "Linux" or os_name == "Darwin":
            self.__modelDir = os.path.join(os.path.expanduser("~"), ".config", "arrera-model") + os.sep
        elif os_name == "Windows":
            self.__modelDir = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "arrera-model") + os.sep

        self.__modelDownloadFile = os.path.join(self.__modelDir, "model_download.json")

        if not os.path.isfile(self.__modelDownloadFile):
            os.makedirs(os.path.dirname(self.__modelDownloadFile), exist_ok=True)
            with open(self.__modelDownloadFile, "x", encoding="utf-8") as f:
                json.dump({"models": []}, f, ensure_ascii=False, indent=2)

    def get_model_list(self):
        return list(self.__dictModel.keys())

    def get_data_model(self,key:str):
        data = self.__dictModel[key]
        return data["name"],data["url"],data["description"]

    def get_model_download(self):
        with open(self.__modelDownloadFile, 'r' , encoding='utf-8') as openfile:
            return list(json.load(openfile)["models"])

    def download_model(self,key:str):
        url = self.get_data_model(key)[1]
        if key in self.get_model_download():
            return False

        try :
            response = requests.get(url, stream=True)

            if response.status_code == 200:
                full_path = self.__modelDir + key + ".gguf"

                with open(full_path, 'wb') as f:
                    # On télécharge par paquets de 8 Ko (ou plus)
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                    openfile = open(self.__modelDownloadFile, 'r' , encoding='utf-8')
                    dict = json.load(openfile)
                    openfile.close()
                    writeFile = open(self.__modelDownloadFile, 'w', encoding='utf-8')
                    dict["models"].append(key)
                    json.dump(dict,writeFile,indent=2)
                    writeFile.close()
                return True
            else :
                return False
        except Exception as e :
            return False

    def get_path_model(self,key:str):
        if key in self.get_model_download():
            return self.__modelDir+key+".gguf"
        else :
            return None