import os
from llama_cpp import Llama

LISTMODELSUPPROT = [
    "arrera_model_2026",
    "model_gguf"
]

class ArreraIALoad:
    def __init__(self):
        self.__model_type = None
        self.__model = None
        self.__tokeniser = None
        self.__classes = None
        self.__is_loaded = False
        self.__system_context_is_loaded = False
        self.__system_context = ""

    # Methode private
    """
    def __predict_arrera_2026_model(self, sentence: str, confidence_threshold: float = 0.70):
        if not self.__is_loaded:
            return None, 0.0

        input_tensor = tf.constant([sentence], dtype=tf.string)

        if len(input_tensor.shape) == 1:
            input_tensor = tf.expand_dims(input_tensor, axis=-1)

        predictions = self.__model.predict(input_tensor, verbose=0)

        prediction = predictions[0]

        max_index = np.argmax(prediction)
        confidence = prediction[max_index]

        predicted_tag = self.__classes[max_index]

        if confidence < confidence_threshold:
            return None, float(confidence)

        return predicted_tag, float(confidence)
    """

    def __predict_gguf_model(self, prompt, max_tokens=512):
        consigne_langue = "\n\n(Réponds impérativement en français, même si je parle anglais ou technique)."
        if self.__system_context_is_loaded:
            content = f"{self.__system_context}\n\nInstruction utilisateur : {prompt}{consigne_langue}"
            messages = [{"role": "user", "content": content}]
        else:
            messages = [{"role": "user", "content": prompt + consigne_langue}]

        output = self.__model.create_chat_completion(
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.7,
        )

        return output['choices'][0]['message']['content']

    # Methode public
    """
    def loadArreraModel2026(self, model_path:str, classes_path:str):
        if not os.path.exists(model_path) or not os.path.exists(classes_path):
            raise ValueError("Erreur : Fichiers modèles introuvables.")

        try:
            # 1. Chargement du modèle Keras complet (avec la couche TextVectorization incluse)
            self.__model = tf.keras.models.load_model(model_path)

            # 2. Chargement des noms de classes (labels)
            with open(classes_path, 'r', encoding='utf-8') as f:
                self.__classes = json.load(f)

            self.__is_loaded = True
            self.__model_type = LISTMODELSUPPROT[0]
            return True
        except Exception as e:
            raise ValueError(f"Erreur lors du chargement du chatbot : {e}")
    """

    def load_help_file(self, file_path: str):
        if os.path.exists(file_path):
            try :
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.__system_context = f"Utilise les informations suivantes pour aider l'utilisateur :\n\n{content}"
                    self.__system_context_is_loaded = True
                return True
            except :
                self.__system_context_is_loaded = False
                return False
        else:
            self.__system_context_is_loaded = False
            return False

    def unload_help(self):
        self.__system_context_is_loaded = False
        self.__system_context = ""

    def load_model_gguf(self, model_path:str, n_ctx:int=2048):
        if not os.path.exists(model_path):
            raise ValueError(f"Le fichier modèle n'existe pas : {model_path}")

        try:
            self.__model = Llama(
                model_path=model_path,
                n_ctx=n_ctx,
                n_gpu_layers=0,
                verbose=False
            )

            self.__is_loaded = True
            self.__model_type = LISTMODELSUPPROT[1]
            return True
        except Exception as e:
            raise ValueError(f"Erreur lors du chargement : {e}")

    def send_request(self, sentence: str, confidence_threshold: float = 0.70):
        if self.__model_type == LISTMODELSUPPROT[0]:
            return None, 0.0
        elif self.__model_type == LISTMODELSUPPROT[1]:
            return self.__predict_gguf_model(sentence)
        else:
            return None, 0.0