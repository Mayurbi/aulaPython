import os
from gtts import gTTS
from pygame import mixer

diretorio = input("Digite o local do arquivo: ")
teste = os.path.isfile(diretorio)

if teste:
    print("Carregando arquibo. Por favor, aguarde... não me mate")
    with open(diretorio) as file_data:
        arquivo = file_data.read()
        print("Arquivo carregado")
        print("efetuando a leitura... Por favor, aguarde")
        voz = gTTS(arquivo, lang='pt')
        voz.save("voz.mp3")
        print("Falando...")
        mixer.init()
        mixer.music.load("voz.mp3")
        mixer.music.play()
        input("BeBÊ calma calma")
else:
    print("Diretorio não encontrado")
# voz = gTTS("por vocÊ eu bebo o mar de canudinho, atravesso o polo norte de shortinho", lang='pt')
# voz.save("voz.mp3") #slava o audio na pasta projeot
mixer.init()
mixer.music.load("voz.mp3")
mixer.music.play()

fim = input("Digite algo pra finalizar")