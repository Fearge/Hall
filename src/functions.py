import scipy.io.wavfile as wavfile
from scipy import signal

def normalize(amp_list):
    amp_list /= max(abs(amp_list))
    amp_list *= (2 ** 15 - 1)
    amp_list = amp_list.astype('int16')
    return amp_list

#  Metadaten der Datei ausgeben
def showStats(file):

    roomfn = file
    rate, data = wavfile.read(roomfn)
    N = data.shape[0]
    CHN = data.shape[1] if len(data.shape) == 2 else 1

    print(f"Audiodatei {roomfn} mit Abtastrate {rate}Hz")
    print(f"Anzahl der Abtastwerte in der Datei: {N}")
    print(f"Anzahl der Audio-Kanäle (1=Mono, 2=Stereo): {CHN}")
    print(f"Dauer: {N / rate:.3f}s")
    print("Die ersten Vier Abtastwerte:")
    print(data[:4])


# Ergebnis ausgeben, entweder auf Soundkarte oder als .wav
def ausgabe(fileToPrint,rateToPrint,isSpeichern):
    # als .wav
    if(isSpeichern):
        wavfile.write(input("Bitte geben Sie einen Namen für die zu speichernde Datei an: ") + ".wav", rateToPrint, fileToPrint)
    else:
        sd.play(fileToPrint,rateToPrint)
        input("Drücke die Eingabetaste, um den Sound anzuhalten")
        sd.stop()