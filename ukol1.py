def ukol1(soubor):
    try:
        soubor = open(f"{soubor}.txt", encoding='utf-8')
        obsah = soubor.read()
        soubor.close()

        print(obsah)

    except FileNotFoundError:
        print(f"Soubor {soubor} nebyl nalezen")


ukol1("soubor")
ukol1("ukol")