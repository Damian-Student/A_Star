import math

start_x = 19
start_y = 0
koniec_x = 0
koniec_y = 19
tab = []
lista_otw = []
lista_zam = []
rodzice = [['0'] * 20 for _x in range(20)]


class Punkt:
    poz_x = start_x
    poz_y = start_y
    poz_kon_x = koniec_x
    poz_kon_y = koniec_y
    koszt = 0
    heurystyka = 0.00

    def __init__(self, x, y, koszt):
        self.poz_x = x
        self.poz_y = y
        self.koszt = koszt


def wczytajPlik(nazwaPliku):
    try:
        plik = open(nazwaPliku, 'r')
        for line in plik:
            tab.append(line.split())
        plik.close()
        return tab
    except FileNotFoundError as e:
        print("Plik nie istnieje")
        print(e)


def heurystykaPoz(x, y):
    return math.sqrt((x - Punkt.poz_kon_x)**2 + (y - Punkt.poz_kon_y)**2)


def wyliczKoszt(x, y):
    heurystyka = heurystykaPoz(x, y)
    wart = True
    koszt = 0
    while wart:
        if start_x == x and start_y == y:
            wart = False
        else:
            if rodzice[x][y] == 'down':
                x += 1
            elif rodzice[x][y] == 'up':
                x -= 1
            elif rodzice[x][y] == 'left':
                y -= 1
            elif rodzice[x][y] == 'right':
                y += 1
            koszt += 1
    return koszt + heurystyka


def czy_na_liscie(lista, Punkt):
    for x in range(len(lista)):
        if (lista[x].poz_x == Punkt.poz_x and lista[x].poz_y == Punkt.poz_y):
            return True
    return False


def dodaj(x, y, koszt):
    if (x < 19 and tab[x + 1][y] != '5' and czy_na_liscie(lista_zam, Punkt(x + 1, y, koszt)) == 0):  # Dół
        if rodzice[x + 1][y] == '0':
            rodzice[x + 1][y] = 'up'            # Jest rodzicem tego z góry
        Punkt.koszt = wyliczKoszt(x + 1, y)
        lista_otw.append(Punkt(x + 1, y, koszt))
    if (y > 0 and tab[x][y - 1] != '5' and czy_na_liscie(lista_zam, Punkt(x, y - 1, koszt)) == 0):  # Lewa
        if rodzice[x][y - 1] == '0':
            rodzice[x][y - 1] = 'right'
        Punkt.koszt = wyliczKoszt(x, y - 1)
        lista_otw.append(Punkt(x, y - 1, koszt))
    if (x > 0 and tab[x - 1][y] != '5' and czy_na_liscie(lista_zam, Punkt(x - 1, y, koszt)) == 0):  # Góra
        if rodzice[x - 1][y] == '0':
            rodzice[x - 1][y] = 'down'
        Punkt.koszt = wyliczKoszt(x - 1, y)
        lista_otw.append(Punkt(x - 1, y, koszt))
    if (y < 19 and tab[x][y + 1] != '5' and czy_na_liscie(lista_zam, Punkt(x, y + 1, koszt)) == 0):  # Prawa
        if rodzice[x][y + 1] == '0':
            rodzice[x][y + 1] = 'left'
        Punkt.koszt = wyliczKoszt(x, y + 1)
        lista_otw.append(Punkt(x, y + 1, koszt))
    if len(lista_otw) == 0:
        print("Nie ma drogi do celu")
        exit(0)


def najmnijeszy_na_liscie(lista):
    minimum = lista[len(lista) - 1].koszt
    for x in range(len(lista)):
        if minimum > lista[x].koszt:
            minimum = lista[x].koszt
    return minimum


def Algorytm():
    lista_zam.append(Punkt)
    tab[Punkt.poz_x][Punkt.poz_y] = '3'
    dodaj(Punkt.poz_x, Punkt.poz_y, Punkt.koszt)
    while ((Punkt.poz_x != Punkt.poz_kon_x and Punkt.poz_y != Punkt.poz_kon_y) or Punkt.poz_x != Punkt.poz_kon_x or Punkt.poz_y != Punkt.poz_kon_y):
        lista_zam.append(Punkt(Punkt.poz_x, Punkt.poz_y, Punkt.koszt))
        dodaj(Punkt.poz_x, Punkt.poz_y, Punkt.koszt)
        for x in range(lista_otw.__len__() - 1, -1, -1):
            if najmnijeszy_na_liscie(lista_otw) == lista_otw[x].koszt:
                Punkt.poz_x = lista_otw[x].poz_x
                Punkt.poz_y = lista_otw[x].poz_y
                if czy_na_liscie(lista_zam, Punkt) == 0:
                    lista_zam.append(Punkt(Punkt.poz_x, Punkt.poz_y, Punkt.koszt))
                del lista_otw[x]
                break

def wypisz():
    wart = True
    ilosc = 1
    x = Punkt.poz_kon_x
    y = Punkt.poz_kon_y
    while wart:
        if start_x == x and start_y == y:
            wart = False
            for x in tab:
                print(x)
        else:
            if rodzice[x][y] == 'down':
                tab[x][y] = '3'
                x += 1
                ilosc += 1
            elif rodzice[x][y] == 'up':
                tab[x][y] = '3'
                x -= 1
                ilosc += 1
            elif rodzice[x][y] == 'left':
                tab[x][y] = '3'
                y -= 1
                ilosc += 1
            elif rodzice[x][y] == 'right':
                tab[x][y] = '3'
                y += 1
                ilosc += 1
    print(ilosc)

wczytajPlik("grid.txt")
Algorytm()
wypisz()

