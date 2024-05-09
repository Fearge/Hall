#eigene Funktionen
import functions

#Todo: Fehlerbehandlung
sampleRate = 44100
zuFaltendeDatei = ""
impulsAntwort = ""
gefalteteDatei = ""

if __name__ == '__main__':

    eingabe = input("Möchtest Du eine eigene Datei mit Hall versehen oder das bereits vorhandene Preset nutzen? (P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

    if (eingabe.upper() == "E"):

        print("Wähle eine Datei aus, auf die Hall gelegt werden soll")
        zuFaltendeDatei = functions.select_file()

        eingabe = input("Möchtest du eine eigene Impulsantwort nutzen oder das bereits vorhandene Preset? (P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

        if(eingabe.upper()=="E"):
            print("Wähle eine Datei für die Impulsantwort aus")
            impulsAntwort = functions.select_file()

        elif (eingabe.upper() == "P"):
            eingabe = input("Wähle ein Preset. Preset 1 (classroom.wav) = 1, Preset 2 (big_hall.wav) = 2 \nBitte Wahl eintippen: ")

            if(eingabe == "1"):
                impulsAntwort = 'classroom.wav'

            elif(eingabe == "2"):
                impulsAntwort = 'big_hall.wav'

    elif (eingabe.upper() == "P"):
        zuFaltendeDatei = 'WiiShopChannel.wav'
        impulsAntwort = 'big_hall.wav'

    #Todo: abfragen wie ausgegeben werden soll
    #Faltung
    gefalteteDatei, sampleRate = functions.convolve(zuFaltendeDatei, impulsAntwort)

    eingabe = ()

    eingabe = (input("Möchtest Du die Datei speichern oder über dein Ausgabegerät abspielen? (S = Speichern / A = Ausgabe) \nBitte Wahl eintippen: "))

    if (eingabe.upper() == "S"):
        functions.ausgabe(gefalteteDatei, sampleRate, 1)

    elif (eingabe.upper() == "A"):
        functions.ausgabe(gefalteteDatei, sampleRate, 0)




    """
    else:
        print("Sie haben keinen gültigen Buchstaben eingeben!")
    """