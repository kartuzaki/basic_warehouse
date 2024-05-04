
budzet = 25000.00
biblioteka = [
    {
        "tytul": "Call of Duty",
        "ilosc": 10,
        "cena": 145

    },
    {
        "tytul": "FC 24",
        "ilosc": 15,
        "cena": 269

    },
    {
        "tytul": "GTA V",
        "ilosc": 5,
        "cena": 59

    },
    {
        "tytul": "Super Mario World",
        "ilosc": 190,
        "cena": 190


    },
]
operacje = []
koniec_programu = False
print("Witaj w programie księgowo-magazynowym")
while not koniec_programu:
    opcje = input("\nWybierz jedną z poniższych opcji:\n\n1.Saldo\n2.Sprzedaż\n3.Zakup\n4.Konto\n5.Lista\n6.Magazyn\n7.Przegląd"
              "\n8.Koniec\n")

    if opcje == "1":
        zmiana_saldo = input("Podaj kwotę którą chcesz dodać lub odjąć od salda:")
        budzet += float(zmiana_saldo)
    elif opcje == "2":
        tytul_gry = input("Podaj tytuł gry którą sprzedajesz: ")
        ilosc_sztuk = int(input("Podaj ilość sztuk którą sprzedajesz: "))
        cena_gry = float(input("Podaj cenę jednostkową tytułu: "))
        gra_na_stanie = False
        sprzedaz_gry = False
        for gra in biblioteka:
            if gra.get("tytul") == tytul_gry:
                gra_na_stanie = True
                if gra.get("ilosc") >= ilosc_sztuk:
                    gra["ilosc"] -= ilosc_sztuk
                    sprzedaz_gry = True
                    break
        if sprzedaz_gry:
            print(f"Sprzedano {ilosc_sztuk} szt. gry {tytul_gry} za łączną kwotę {ilosc_sztuk * cena_gry} zł.")
            operacje.append({"operacja": "sprzedaż", "tytuł": tytul_gry, "ilość": ilosc_sztuk, "cena": cena_gry})
            budzet += ilosc_sztuk * cena_gry
        else:
            if not gra_na_stanie:
                print("Nie ma takiej gry na stanie.")
            else:
                print("Brak wystarczającej ilości gier na stanie.")
    elif opcje == "3":
        tytul = input("Podaj tytuł gry którą chcesz kupić: ")
        ilosc = int(input("Podaj ilość sztuk którą chcesz zakupić: "))
        cena = float(input("Podaj cenę jednostkową tytułu: "))
        if budzet >= ilosc * cena:
            biblioteka.append({
                "tytul": tytul,
                "ilosc": ilosc,
                "cena": cena
            })
            budzet = budzet - (ilosc * cena)
        else:
            print(f"Ten zakup przekracza wartość dostępnego salda.\nSaldo wynosi obecnie: {budzet}")
    elif opcje == "4":\
        print(f"Stan konta wynosi obecnie: {budzet}")
    elif opcje == "5":
        print(biblioteka)
    elif opcje == "6":
        nazwa_produktu = input("Podaj nazwę produktu: ")
        produkt_znaleziony = False
        for produkt in biblioteka:
            if produkt["tytul"] == nazwa_produktu:
                print(f"Stan magazynu dla produktu '{nazwa_produktu}': {produkt['ilosc']} sztuk")
                produkt_znaleziony = True
                break
        if not produkt_znaleziony:
            print("Nie znaleziono produktu o podanej nazwie.")
    elif opcje == "7":
        od = input("Podaj mi początkowy zakres: ")
        do = input("Podaj mi końcowy zakres: ")
        if od != "" and do != "":
            print(operacje[int(od):int(do)])
        elif od != "" and do == "":
            print(operacje[int(od):])
    elif opcje == "8":
        koniec_programu = True