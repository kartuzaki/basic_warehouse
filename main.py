
budzet = 25000.00
biblioteka = [
    {
        "tytul": "Call of Duty",
        "ilosc": 10,
        "cena": 149.99

    },
    {
        "tytul": "FC 24",
        "ilosc": 15,
        "cena": 269.99

    },
    {
        "tytul": "GTA V",
        "ilosc": 5,
        "cena": 59.99

    },
    {
        "tytul": "Super Mario World",
        "ilosc": 190,
        "cena": 19.99


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
    # elif opcje == "2":
    #     tytul_gry = input("Podaj tytuł gry którą sprzedajesz: ")
    #     ilosc_sztuk = int(input("Podaj ilość sztuk którą sprzedajesz: "))
    #     cena_gry = float(input("Podaj cenę jednostkową tytułu: "))
    #     gra_na_stanie = False
    #     sprzedaz_gry = False
    #     for gra in biblioteka:
    #         if gra.get("tytul") == tytul_gry:
    #             gra_na_stanie = True
    #             if gra.get("ilosc") > 0:
    #                 gra["ilosc"] -= 1
    #                 sprzedaz_gry = True
    #     if sprzedaz_gry:
    #         budzet
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
    elif opcje == "8":
        koniec_programu = True