#eigene Funktionen
import functions
#File Klasse
import file as file

#Dateien
zuFaltendeDatei = ""
impulsAntwort = ""
gefalteteDatei = ""

#Flags
eingabeFlag = ""



if __name__ == '__main__':

    while eingabeFlag.upper() != "E" and eingabeFlag.upper() != "P":
        eingabeFlag = input(
            "Möchtest Du eine eigene Datei mit Hall versehen oder das bereits vorhandene Preset nutzen? "
            "(P = Presets / E = Eigene)\nBitte Wahl eintippen: ")

        # Auswahl der Datei
        if eingabeFlag.upper() == "E":

            print("Wähle eine Datei aus, auf die Hall gelegt werden soll")
            try:
                zuFaltendeDatei = file.setUp(functions.select_file())
                eingabeFlag = ""
            except FileNotFoundError:
                print("Datei konnte nicht gefunden werden!")
            except ValueError:
                print("Datei Format ist nicht .wav!")
            except:
                print("Das lief schief! Versuch es noch mal, vielleicht mit einer anderen Datei!")

            # Auswahl ob Preset-Hall oder eigener
            while eingabeFlag.upper() != "E" and eingabeFlag.upper() != "P":
                eingabeFlag = input(
                    "Möchtest du eine eigene Impulsantwort nutzen oder das bereits vorhandene Preset? "
                    "(P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

                # Eigene IR
                if eingabeFlag.upper() == "E":
                    print("Wähle eine Datei für die Impulsantwort aus")
                    try:
                        impulsAntwort = file.setUp(functions.select_file())
                        eingabeFlag = ""
                    except FileNotFoundError:
                        print("Datei konnte nicht gefunden werden!")
                    except ValueError:
                        print("Datei Format ist nicht .wav!")
                    except:
                        print("Das lief schief! Versuch es noch mal, vielleicht mit einer anderen Datei!")

                # Preset IR
                elif eingabeFlag.upper() == "P":

                    # Auswahl zwischen Presets
                    while eingabeFlag != "1" and eingabeFlag != "2":
                        eingabeFlag = input(
                            "Wähle ein Preset. Preset 1 (classroom.wav) = 1, Preset 2 (big_hall.wav) = 2 "
                            "\nBitte Wahl eintippen: ")

                        if eingabeFlag == "1":
                            impulsAntwort = file.setUp('classroom.wav')
                            eingabeFlag = ""
                        elif eingabeFlag == "2":
                            impulsAntwort = file.setUp('big_hall.wav')
                            eingabeFlag = ""
                        else:
                            print("Sie haben keine gültige Zahl eingegeben!")
                else:
                    print("Sie haben keinen gültigen Buchstaben eingegeben!")

        # Preset für showcase, feste Datei & IR
        elif eingabeFlag.upper() == "P":
            zuFaltendeDatei = file.setUp('WiiShopChannel.wav')
            impulsAntwort = file.setUp('big_hall.wav')
            eingabeFlag = ""
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")

    # Faltung soll mit 2 Mono Dateien geschehen
    zuFaltendeDatei.makeMono()
    impulsAntwort.makeMono()

    # Faltung
    gefalteteDatei = functions.convolve(zuFaltendeDatei, impulsAntwort)

    # Normalisierung für Ausgabe, ansonsten verzerrt es
    gefalteteDatei.normalize()

    # Stats
    while eingabeFlag.upper() != "J" and eingabeFlag.upper() != "N":
        eingabeFlag = input(
            "Möchtest du dir die Stats zu der zu faltenden Datei anzeigen lassen? "
            "(J = Ja / N = Nein) \nBitte Wahl eintippen: ")
        if eingabeFlag.upper() == "J":
            zuFaltendeDatei.showStats()
            eingabeFlag = ""
        elif eingabeFlag.upper() == "N":
            eingabeFlag = ""
            pass
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")

    # Ausgabe, entweder als .wav Datei oder über Soundkarte

    while eingabeFlag.upper() != "S" and eingabeFlag.upper() != "A":
        eingabeFlag = (input(
            "Möchtest Du die Datei speichern oder über dein Ausgabegerät abspielen? "
            "(S = Speichern / A = Ausgabe) \nBitte Wahl eintippen: "))

        # als .wav gespeichert
        if eingabeFlag.upper() == "S":
            try:
                functions.ausgabe(gefalteteDatei, 1)
                eingabeFlag = ""
            except:
                print("Datei konnte nicht gespeichert werden!")

        # über Soundkarte
        elif eingabeFlag.upper() == "A":
            try:
                functions.ausgabe(gefalteteDatei, 0)
                eingabeFlag = ""
            except:
                print("Datei konnte nicht abgespielt werden!")
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")