from objet.parreraclient import *
from ObjetsNetwork.gestion import*

class socketAssistant :
    def __init__(self,name:str,enable:bool):
        self.__socket = PArreraClient(name)
        self.__serverOn = self.__socket.connectToServeur("ws://127.0.0.1:6666")
        if not self.__serverOn and enable:
            self.__socket = None


    def receivedMessageServer(self):
        message = self.__socket.receiveMessage()
        if message:
            # Traitement du message reçu
            self.__sortieMessage = message
            print(message)
            return True
        else:
            return False

    def sendData(self, data):
        if self.__serverOn == True :
            return self.__socket.sendMessage(data)
        else :
            return False

    def getMessageServer(self):
        return self.__sortieMessage

    def stopSocket(self):
        self.__socket.disconnect()
        self.__serverOn = False

    def getServeurOn(self):
        return self.__serverOn