import scipy.io.wavfile as wavfile
from scipy import signal

#TODO:Abfragen, ob eigene Datei oder preset

    #TODO:Datei einlesen

    #TODO:Preset Dateien auswählen

#Wavfile und IR einlesen
rate1, x = wavfile.read('C:/Users/Fearge/Downloads/Audioprojekt/spoken.wav')
rate2, h = wavfile.read('big_hall.wav')

assert(rate1 == rate2)
x = x.mean(axis=1) if len(x.shape) > 1 else x
h = h.mean(axis=1) if len(h.shape) > 1 else x

#Faltung
y = signal.fftconvolve(x, h)
#Skalierung auf +-32765 und umwandeln in Integer
y /= max(abs(y))
y *= (2**15-1)
y = y.astype('int16')
#Ergebnis abspeichern
wavfile.write('y.wav', rate1, y)
