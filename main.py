import pyttsx3
from datetime import datetime
engine = pyttsx3.init()
taxa = 155

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('volume', 1.0)

agora = datetime.now()
hora = agora.hour
minuto = agora.minute
dia = datetime.today().day
mes = datetime.today().month
ano = datetime.today().year
texto = "Agora são " + str(hora) + "horas e " + str(minuto) + "minutos"
texto +="do dia " + str(dia) + "do mês " + str(mes) + " do ano " + str(ano)
en = pyttsx3.init() #inicia a fala
en.setProperty('rate', 155)
en.setProperty('volume', 1.0)
en.setProperty('voice', b'brasil')
en.say(texto)
en.runAndWait()



msg = 'Good Morning Paola Bernardes'

for i in range(1):
    engine.setProperty('rate',taxa)
    engine.say(msg)
    engine.runAndWait()
    taxa += 20