#eigene Funktionen
import functions

#Todo: Fehlerbehandlung
sampleRate = 44100
zuFaltendeDatei = ""
impulsAntwort = ""
gefalteteDatei = ""

if __name__ == '__main__':

    eingabe = input("Hallo :) Möchtest du eigene Dateien mit Hall belegen oder welche von unseren Presets nutzen? (P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

    if (eingabe.upper() == "E"):
        print("Wähle eine Datei aus, auf die Hall gelegt werden soll")
        zuFaltendeDatei = functions.select_file()
        eingabe = input("Möchtest du eine eigene Impulsantwort nutzen oder die bereits vorhandene (big_hall)? (P = Presets / E = Eigene)")

        if(eingabe.upper()=="E"):
            impulsAntwort = functions.select_file()

        elif (eingabe.upper() == "P"):
            impulsAntwort = 'big_hall.wav'

    elif (eingabe.upper() == "P"):
        zuFaltendeDatei = 'WiiShopChannel.wav'
        impulsAntwort = 'big_hall.wav'

    #Todo: abfragen wie ausgegeben werden soll
    #Faltung
    gefalteteDatei, sampleRate = functions.convolve(zuFaltendeDatei, impulsAntwort)

    eingabe = (input("Möchtest Du die Datei speichern oder über dein Ausgabegerät abspielen? (S = Speichern / A = Ausgabe) \nBitte Wahl eintippen: "))

    if (eingabe.upper() == "S"):
        functions.ausgabe(gefalteteDatei, sampleRate, 1)

    elif (eingabe.upper() == "A"):
        functions.ausgabe(gefalteteDatei, sampleRate, 0)



    """
    else:
        print("Sie haben keinen gültigen Buchstaben eingeben!")
    """