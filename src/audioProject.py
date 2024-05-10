#eigene Funktionen
import functions

sampleRate = 44100
zuFaltendeDatei = ""
impulsAntwort = ""
gefalteteDatei = ""

if __name__ == '__main__':

    eingabe_datei1 = ""

    while eingabe_datei1.upper() != "E" and eingabe_datei1.upper() != "P":
        eingabe_datei1 = input(
            "Möchtest Du eine eigene Datei mit Hall versehen oder das bereits vorhandene Preset nutzen? "
            "(P = Presets / E = Eigene)\nBitte Wahl eintippen: ")

        if eingabe_datei1.upper() == "E":
            while zuFaltendeDatei == "":

                print("Wähle eine Datei aus, auf die Hall gelegt werden soll")
                try:
                    zuFaltendeDatei = functions.select_file()
                except FileNotFoundError:
                    print("Datei konnte nicht gefunden werden!")
                except ValueError:
                    print("Datei ist nicht .wav!")
                except:
                    print("Da ist was schiefgelaufen, versuch es nochmal!")

            eingabe_hall = ""
            while eingabe_hall.upper()!= "E" and eingabe_hall.upper()!= "P":
                eingabe_hall = input(
                    "Möchtest du eine eigene Impulsantwort nutzen oder das bereits vorhandene Preset? "
                    "(P = Presets / E = Eigene) \nBitte Wahl eintippen: ")

                if eingabe_hall.upper() == "E":
                    print("Wähle eine Datei für die Impulsantwort aus")
                    try:
                        impulsAntwort = functions.select_file()
                    except FileNotFoundError:
                        print("Datei konnte nicht gefunden werden!")
                    except ValueError:
                        print("Datei ist nicht .wav!")
                    except:
                        print("Da ist was schiefgelaufen, versuch es nochmal!")

                elif eingabe_hall.upper() == "P":
                    eingabe_preset = 0
                    while eingabe_preset != "1" and eingabe_preset != "2":
                        eingabe_preset = input(
                            "Wähle ein Preset. Preset 1 (classroom.wav) = 1, Preset 2 (big_hall.wav) = 2 "
                            "\nBitte Wahl eintippen: ")

                        if eingabe_preset == "1":
                            impulsAntwort = 'classroom.wav'
                        elif eingabe_preset == "2":
                            impulsAntwort = 'big_hall.wav'
                        else:
                            print("Sie haben keine gültige Zahl eingegeben!")

                else:
                    print("Sie haben keinen gültigen Buchstaben eingegeben!")

        elif eingabe_datei1.upper() == "P":
            zuFaltendeDatei = 'WiiShopChannel.wav'
            impulsAntwort = 'big_hall.wav'
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")

    #Faltung
    gefalteteDatei, sampleRate = functions.convolve(zuFaltendeDatei, impulsAntwort)

    #Stats
    eingabe_stats = ""
    while eingabe_stats.upper() != "J" and eingabe_stats.upper() != "N":
        eingabe_stats = input(
            "Möchtest du dir die Stats zu der zu faltenden Datei anzeigen lassen? "
            "(J = Ja / N = Nein) \nBitte Wahl eintippen: ")
        if eingabe_stats.upper() == "J":
            functions.show_stats(zuFaltendeDatei)
        elif eingabe_stats.upper() == "N":
            pass
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")

    #Ausgabe
    eingabe_ausgabe = ""
    while eingabe_ausgabe.upper() != "S" and eingabe_ausgabe.upper() != "A":
        eingabe_ausgabe = (input(
            "Möchtest Du die Datei speichern oder über dein Ausgabegerät abspielen? "
            "(S = Speichern / A = Ausgabe) \nBitte Wahl eintippen: "))

        if eingabe_ausgabe.upper() == "S":
            try:
                functions.ausgabe(gefalteteDatei, sampleRate, 1)
            except:
                print("Datei konnte nicht gespeichert werden!")

        elif eingabe_ausgabe.upper() == "A":
            try:
                functions.ausgabe(gefalteteDatei, sampleRate, 0)
            except:
                print("Datei konnte nicht abgespielt werden!")
        else:
            print("Sie haben keinen gültigen Buchstaben eingegeben!")
