class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return "{jmeno}\t{prijmeni}\t{vek}\t{telefon}".format(jmeno=self.jmeno, prijmeni = self.prijmeni, vek = self.vek, telefon = self.telefon)


pojistenci = {}
while 1 == 1:
    print("""Vyberte si akci:
1 - Pridat nového pojisteného
2 - Vypsat vsechny pojistene
3 - vyhledat pojisteneho
4 - Konec""")
    odpoved = input("Vyberte akci:")
    if odpoved == "1":
        jmeno = input("Zadejte jmeno pojistence:")
        prijmeni = input("Zadejte prijmeni pojistence:")
        vek = input("Zadejte vek pojistence:")
        telefon = input("Zadejte telefon pojistence:")
        data = Pojistenec(jmeno, prijmeni, vek, telefon)
        klic = jmeno+prijmeni
        pojistenci.update({klic:data})
        print(f"Pojistenec {jmeno} {prijmeni} pridan")
    elif odpoved == "2":
        for values in pojistenci.values():
            print(values)
    elif odpoved == "3":
        hledat_jmeno = input ("Zadejte jmeno pojistence:")
        hledat_prijmeni = input("Zadejte prijmeni pojistence:")
        hledat = hledat_jmeno+hledat_prijmeni
        try:
            print(pojistenci[hledat])
        except KeyError:
            print("Pojistenec nenalezen")
    elif odpoved == "4":
        quit()
    else:
        print("Chybny prikaz")

        