termek_nevei = ["alma", "mosógép", "rabszolga"]
arak = [100, 1500000, 150]
raktar_keszlet = [5, 15, 0]


# szerkeszteni tudjuk a raktárunkat
def szerkesztes(termek_nevei, arak, raktar_keszlet):
    termek_nev = input("Adjon meg egy termék nevet!")
    ar = int(input("Adjon meg egy termék árát!"))
    darab = int(input("Adjon meg egy termék darabszámát!"))

    termek_nevei.append(termek_nev)
    arak.append(ar)
    raktar_keszlet.append(darab)


# vásárolni tudunk a raktárból
def vasarlas(termek_nevei, arak, raktar_keszlet):
    kosar = []
    vegosszeg = 0
    while True:
        for index, item in enumerate(termek_nevei):
            print(f"Termék neve: {item} - Ára: {arak[index]}Ft - Darabszám: {raktar_keszlet[index]}")
        termek = input("Adja meg mit szeretne vásárolni! Ha megszeretnél állni, akkor 'stop'!")
        if termek in termek_nevei:
            vegosszeg = vasarlas_manager(termek_nevei, arak, raktar_keszlet, kosar, vegosszeg, termek)
        elif termek == "stop":
            break
        else:
            print("Ilyen termék nem létezik!\n")
    print(f"Termékek: {kosar} \n Végösszeg: {vegosszeg} \n {raktar_keszlet}")
        

def vasarlas_manager(termek_nevei, arak, raktar_keszlet, kosar, vegosszeg, termek):
    termek_indexe = termek_nevei.index(termek)
    if raktar_keszlet[termek_indexe] > 0:
        vegosszeg += arak[termek_indexe]
        kosar.append(termek_nevei[termek_indexe])
        raktar_keszlet[termek_indexe] -= 1
        return vegosszeg
    else:
        print("Sajnos Misi ellopta! Ezért nincs több!")

def mennyiseg_valtoztatas(termek_nevei, raktar_keszlet):
    termek = input("Melyik termék raktárkészletét szeretnéd változtatni?")
    if termek in termek_nevei:
        termek_indexe = termek_nevei.index(termek)
        mennyiseg = int(input("Mennyivel változassuk a raktárkészletet? "))
        raktar_keszlet[termek_indexe] += mennyiseg
    else:
        print("Ilyen termék nincs!")



# user input
while True:
    print(termek_nevei,"\n ",arak,"\n ", raktar_keszlet)
    felhasznalo_input = input("Vásárolni vagy szerkeszteni szeretnél?")
    if felhasznalo_input == "vásárolni":
        vasarlas(termek_nevei, arak, raktar_keszlet)
    elif felhasznalo_input == "szerkeszteni":
        felhasznalo_input = input("Raktárkészletet szeretnél változtatni vagy új terméket hozzáadni? (mennyiseg, ujtermek)")
        if felhasznalo_input == "mennyiseg":
            mennyiseg_valtoztatas(termek_nevei, raktar_keszlet)
        elif felhasznalo_input == "ujtermek":
            szerkesztes(termek_nevei, arak, raktar_keszlet)
        else:
            print("Ilyen opció nincs!")
    else:
        print("Hibás értéket adtál meg! (vásárolni, szerkeszteni)")