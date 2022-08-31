from Audio import Audio
from Video import Video
from Playlist import Playlist

print("<>"*15)
nome = input("Qual o nome da sua playlist?")
print("<>"*15)
playlist = Playlist(titulo=nome)
print("Bem vindo ao -- SUA PLAYLIST")
print(f"    Gerenciando {playlist.get_titulo()}...")
while True:
    print("<>"*15)
    op = int(input("O QUE DESEJA FAZER? \n[0] - SAIR \n[1] - ADICIONAR VIDEO \n[2] - ADICIONAR ÁUDIO \n[3] - REMOVER MÍDIA \n[4] "
                   "- EXIBIR PLAYLIST \n[5] - BAIXAR PLAYLIST \n[6] - RENOMEAR PLAYLIST \n[7] - COMPARTILHAR NO WHATSAPP"))
    if op == 1:
        print("-"*30)
        link_video = input("Digite o link do video: ")
        qualidade = input("Digite a qualidade do video: ")
        print("-"*30)
        video = Video(link_video, qualidade)
        playlist.adicionar(video)
    elif op == 2:
        print("-" * 30)
        link_audio = input("Digite o link da musica que deseja baixar: ")
        print("-" * 30)
        audio = Audio(link_audio)
        playlist.adicionar(audio)
    elif op == 3:
        print("-"*35)
        playlist.exibir()
        remov = int(input("Qual das suas mídias deseja remover? "))
        playlist.remover(remov=remov)
    elif op == 4:
        playlist.exibir()
    elif op == 5:
        playlist.baixarTodos()
    elif op == 6:
        print("-"*40)
        newNome = input("PRA QUAL NOME DESEJA ALTERAR SUA PLAYLIST? ")
        playlist.renomear(novoNome=newNome)
    elif op == 0:
        print("-"*35)
        print("VOCÊ ENCERROU O PROGRAMA, OBRIGADO!!!")
        print("-" * 35)
        break