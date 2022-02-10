# Toca um arquivo de MP3 do dispositivo
from pygame import mixer 
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Aperte Enter para pausar a música.')