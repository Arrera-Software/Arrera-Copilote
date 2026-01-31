from librairy.parreraclient import PArreraClient
import time

class gestSocket :
    def __init__(self,name:str):
        self.__sortieMessage = None
        self.__socket = PArreraClient(name)
        self.__serverOn = self.__socket.connectToServeur("ws://127.0.0.1:6666")
        self.__messageIsReceived = False
        self.__running = True
        if not self.__serverOn:
            self.__socket = None
        else :
            if not self.__socket.sendMessage("ArreraSoftConnected"):
                self.__serverOn = False
                self.__socket = None


    def receivedMessageServer(self):
        # print("Thread de réception WebSocket démarré...")
        while self.__running and self.__serverOn:
            try:
                # print("Attente message serveur...")
                message = self.__socket.receiveMessage()
                if message:
                    # Traitement du message reçu
                    self.__sortieMessage = message
                    self.__messageIsReceived = True
                    # print(f"Message reçu: {message}")
                else:
                    # Petit délai pour éviter une boucle trop rapide
                    time.sleep(0.1)
            except Exception as e:
                # print(f"Erreur lors de la réception du message: {e}")
                time.sleep(1)  # Attendre avant de réessayer
        # print("Thread de réception WebSocket arrêté.")

    def sendData(self, data):
        if self.__serverOn:
            return self.__socket.sendMessage(data)
        else :
            return False

    def getMessageServer(self):
        return self.__sortieMessage

    def stopSocket(self):
        self.__running = False
        self.__socket.disconnect()
        self.__serverOn = False

    def getServeurOn(self):
        return self.__serverOn

    def getMessageIsReceived(self):
        if self.__messageIsReceived :
            self.__messageIsReceived = False
            return True
        else :
            return False