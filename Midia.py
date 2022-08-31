from pytube import YouTube
from abc import ABC, abstractmethod     #ABC(abstract class)algo que nao implemento
                                        #Nao posso criar instancias dessa classe

class Midia(ABC):

    def __init__(self, url: str):       #Defino um tipo pra url (Posso botar qualquer coisa se nao tiver)
        video = YouTube(url)            #Instancio o objeto Youtube do pacote pytube
        self.__titulo = video.title     #Acesso a propriedade title e canal do objeto YouTube
        self.__canal = video.author
        self.__url = url

    def get_titulo(self):
        return self.__titulo

    def get_url(self):
        return self.__url

    def get_canal(self):
        return self.__canal

    def apresentar(self):
        print(f"Titulo: {self.__titulo}, canal: {self.__canal} ({self.__url})")

    @abstractmethod                 #Obrigo que os filhos sobrescrevam esse metodo
    def download(self, path: str):  #path: significa o local que vai ser salvo, o diretorio do windows
        pass                        #Não esta implementado ainda