#eigene Funktionen
import functions
import file

zuFaltendeDatei = ""
impulsAntwort = ""
gefalteteDatei = ""

if __name__ == '__main__':

    eingabe = input("Möchtest Du eine eigene Datei mit Hall versehen oder das bereits vorhandene Preset nutzen? (P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

    if (eingabe.upper() == "E"):

        print("Wähle eine Datei aus, auf die Hall gelegt werden soll")
        zuFaltendeDatei = functions.select_file()
        zuFaltendeDatei = file.setUp(zuFaltendeDatei)

        eingabe = input("Möchtest du eine eigene Impulsantwort nutzen oder das bereits vorhandene Preset? (P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

        if(eingabe.upper()=="E"):
            print("Wähle eine Datei für die Impulsantwort aus")
            impulsAntwort = functions.setUp(functions.select_file())

        elif (eingabe.upper() == "P"):
            eingabe = input("Wähle ein Preset. Preset 1 (classroom.wav) = 1, Preset 2 (big_hall.wav) = 2 \nBitte Wahl eintippen: ")

            if(eingabe == "1"):
                impulsAntwort = file.setUp('classroom.wav')

            elif(eingabe == "2"):
                impulsAntwort = file.setUp('big_hall.wav')

    elif (eingabe.upper() == "P"):
        zuFaltendeDatei = 'WiiShopChannel.wav'
        impulsAntwort = 'big_hall.wav'

    #beide Dateien sollen Mono sein
    zuFaltendeDatei.makeMono()
    impulsAntwort.makeMono()
    #Faltung
    gefalteteDatei = functions.convolve(zuFaltendeDatei, impulsAntwort)
    # normalisieren für Ausgabe
    gefalteteDatei.normalize()

    # Stats
    eingabe = input(
        "Möchtest du dir die Stats zu der zu faltenden Datei anzeigen lassen? (J = Ja / N = Nein) \nBitte Wahl eintippen: ")
    if (eingabe.upper() == "J"):
        functions.showStats(zuFaltendeDatei)
    else:
        pass

    #Ausgabe
    eingabe = (input("Möchtest Du die Datei speichern oder über dein Ausgabegerät abspielen? (S = Speichern / A = Ausgabe) \nBitte Wahl eintippen: "))

    if (eingabe.upper() == "S"):
        functions.ausgabe(gefalteteDatei,1)

    elif (eingabe.upper() == "A"):
        functions.ausgabe(gefalteteDatei,0)