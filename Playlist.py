import os

from Midia import Midia


class Playlist:

    def __init__(self, titulo: str):
        self.__titulo = titulo
        self.__midias: list[Midia] = []

    def get_titulo(self):
        return self.__titulo

    def renomear(self, novoNome):
        print(f"Você alterou a PLAYLIST {self.__titulo} para {novoNome}")
        self.__titulo = novoNome

    def exibir(self):
        print()
        print("*"*35)
        print(f"AQUI ESTÁ SUA PLAYLIST {self.__titulo}")
        print("*" * 35)
        if len(self.__midias) == 0:
            print("PLAYLIST VAZIA")
            return
        for i in range(len(self.__midias)):
            print(f"Mídia {i+1}- ", end="")
            self.__midias[i].apresentar()
        print()

    def baixarTodos(self):
        if len(self.__midias) == 0:
            print("PLAYLIST VAZIA")
            return
        for i in range(len(self.__midias)):
            self.__midias[i].download(path=os.getcwd()+"\\dowload") #Diz qual pasta esta o arquivo atual

    def adicionar(self, midia: Midia):
        self.__midias.append(midia)
        print(f"{midia.get_titulo()}, foi adicionado com sucesso a: PLAYLIST {self.__titulo}")

    def remover(self, remov):
        del self.__midias[remov - 1]
        print(f"Você removeu a mídia: {remov}")
