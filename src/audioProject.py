#eigene Funktionen
import functions
#File Klasse
import file as file

#Dateien
zuFaltendeDatei = ""
impulsAntwort = ""
gefalteteDatei = ""

#Flags
eingabeIR = ""
eingabeHall = ""
eingabeShow = ""
eingabeAusgabe = ""


if __name__ == '__main__':
    eingabeDatei = ""

    while eingabeDatei.upper() != "E" and eingabeDatei.upper() != "P":
        eingabeDatei = input(
            "Möchtest Du eine eigene Datei mit Hall versehen oder das bereits vorhandene Preset nutzen? "
            "(P = Presets / E = Eigene)\nBitte Wahl eintippen: ")

        # Auswahl der Datei
        if eingabeDatei.upper() == "E":

            print("Wähle eine Datei aus, auf die Hall gelegt werden soll")
            try:
                zuFaltendeDatei = file.setUp(functions.select_file())

            except FileNotFoundError:
                print("Datei konnte nicht gefunden werden!")
                eingabeDatei = ""
            except ValueError:
                print("Datei Format ist nicht .wav!")
                eingabeDatei = ""
            except:
                print("Das lief schief! Versuch es noch mal, vielleicht mit einer anderen Datei!")
                eingabeDatei = ""



        # Preset für showcase, feste Datei & IR
        elif eingabeDatei.upper() == "P":
            zuFaltendeDatei = file.setUp('WiiShopChannel.wav')
            impulsAntwort = file.setUp('big_hall.wav')
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")

        if eingabeDatei.upper() == "E":
            # Auswahl ob Preset-Hall oder eigener
            while eingabeHall.upper() != "E" and eingabeHall.upper() != "P":

                eingabeHall = input(
                    "Möchtest du eine eigene Impulsantwort nutzen oder das bereits vorhandene Preset? "
                    "(P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

                # Eigene IR
                if eingabeHall.upper() == "E":
                    print("Wähle eine Datei für die Impulsantwort aus")
                    try:
                        impulsAntwort = file.setUp(functions.select_file())

                    except FileNotFoundError:
                        print("Datei konnte nicht gefunden werden!")
                        eingabeHall = ""
                    except ValueError:
                        print("Datei Format ist nicht .wav!")
                        eingabeHall = ""
                    except:
                        print("Das lief schief! Versuch es noch mal, vielleicht mit einer anderen Datei!")
                        eingabeHall = ""


                # Preset IR
                elif eingabeHall.upper() == "P":

                    # Auswahl zwischen Presets
                    while eingabeIR.upper() != "1" and eingabeIR.upper() != "2":
                        eingabeIR = input(
                            "Wähle ein Preset. Preset 1 (classroom.wav) = 1, Preset 2 (big_hall.wav) = 2 "
                            "\nBitte Wahl eintippen: ")

                        if eingabeIR == "1":
                            impulsAntwort = file.setUp('classroom.wav')
                        elif eingabeIR == "2":
                            impulsAntwort = file.setUp('big_hall.wav')
                        else:
                            print("Sie haben keine gültige Zahl eingegeben!")
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
    while eingabeShow.upper() != "J" and eingabeShow.upper() != "N":
        eingabeShow = input(
            "Möchtest du dir die Stats zu der zu faltenden Datei anzeigen lassen? "
            "(J = Ja / N = Nein) \nBitte Wahl eintippen: ")
        if eingabeShow.upper() == "J":
            zuFaltendeDatei.showStats()
        elif eingabeShow.upper() == "N":
            pass
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")

    # Ausgabe, entweder als .wav Datei oder über Soundkarte

    while eingabeAusgabe.upper() != "S" and eingabeAusgabe.upper() != "A":
        eingabeAusgabe = (input(
            "Möchtest Du die Datei speichern oder über dein Ausgabegerät abspielen? "
            "(S = Speichern / A = Ausgabe) \nBitte Wahl eintippen: "))

        # als .wav gespeichert
        if eingabeAusgabe.upper() == "S":
            try:
                functions.ausgabe(gefalteteDatei, 1)
            except:
                print("Datei konnte nicht gespeichert werden!")

        # über Soundkarte
        elif eingabeAusgabe.upper() == "A":
            try:
                functions.ausgabe(gefalteteDatei, 0)
            except:
                print("Datei konnte nicht abgespielt werden!")
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")