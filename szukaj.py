import random
import matplotlib.pyplot as plt
import copy
import math


class Stan:  # klasa przetrzymująca stan
    miasto_teraz = -1
    sciezka = []
    koszt = 0.0

    def ustawMiasto(self, miasto):
        self.miasto_teraz = miasto

    def dodajDoSciezki(self, miasto):
        self.sciezka.append(miasto)

    def dodajKoszt(self, k):
        self.koszt = self.koszt + k

    def __lt__(self, do_porownania):
        return self.koszt < do_porownania.koszt


def obliczOdleglosc(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def potomstwo(stan, miasta):
    ile_miast = len(miasta)

    listaStanow = []

    for i in range(ile_miast):
        temp = Stan()
        temp.sciezka = copy.deepcopy(stan.sciezka)
        temp.miasto_teraz = stan.miasto_teraz
        temp.koszt = stan.koszt
        if i not in temp.sciezka:
            temp.dodajKoszt(
                obliczOdleglosc(miasta[stan.miasto_teraz][1], miasta[stan.miasto_teraz][2], miasta[i][1], miasta[i][2]))
            temp.dodajDoSciezki(i)
            temp.ustawMiasto(i)
            listaStanow.append(temp)

    return listaStanow


algorytm = int(input("Wybierz algorytym do liczenia:\n1 - BRUTEF ORCE\n2 - NAJBLIŻSZY SĄSIAD\n"))
ile_miast = int(input("Podaj liczbę miast, dla których chcesz licztyć: "))
tabela_maist = []

for i in range(ile_miast):
    tabela_maist.insert(i, [i, random.randint(1, 40), random.randint(1, 40)])

stan_teraz = Stan()
miasto_startowe = random.randrange(0, ile_miast)
stan_teraz.ustawMiasto(miasto_startowe)
stan_teraz.dodajDoSciezki(miasto_startowe)
if algorytm == 1:
    wyniki = potomstwo(stan_teraz, tabela_maist)
    while len(wyniki[0].sciezka) != ile_miast:
        temp = []
        for i in wyniki:
            temp.extend(potomstwo(i, tabela_maist))
        wyniki = temp

    for i in wyniki:
        i.dodajDoSciezki(i.sciezka[0])
        i.dodajKoszt(
            obliczOdleglosc(tabela_maist[i.miasto_teraz][1], tabela_maist[i.miasto_teraz][2],
                            tabela_maist[i.sciezka[0]][1],
                            tabela_maist[i.sciezka[0]][2]))

    wyniki.sort()
    print('Najmniejszy koszt: ', wyniki[0].koszt)
    print('Najlepsza sciezka ', wyniki[0].sciezka)
    x = []
    y = []

    for i in wyniki[0].sciezka:
        x.append(tabela_maist[i][1])
        y.append(tabela_maist[i][2])

    x.append(tabela_maist[wyniki[0].sciezka[0]][1])
    y.append(tabela_maist[wyniki[0].sciezka[0]][2])

    plt.plot(x, y)

    for i in range(len(x) - 1):
        plt.annotate(wyniki[0].sciezka[i], (x[i], y[i]), textcoords="offset points", xytext=(5, 5), ha='center')

    plt.show()
elif algorytm == 2:
    for i in range(ile_miast - 1):
        temp = potomstwo(stan_teraz, tabela_maist)
        temp.sort()
        stan_teraz = temp[0]
    print('Najmniejszy koszt: ', stan_teraz.koszt)
    print('Najlepsza sciezka ', stan_teraz.sciezka)

    x = []
    y = []

    for i in stan_teraz.sciezka:
        x.append(tabela_maist[i][1])
        y.append(tabela_maist[i][2])

    x.append(tabela_maist[stan_teraz.sciezka[0]][1])
    y.append(tabela_maist[stan_teraz.sciezka[0]][2])

    plt.plot(x, y)

    for i in range(len(x) - 1):
        plt.annotate(stan_teraz.sciezka[i], (x[i], y[i]), textcoords="offset points", xytext=(5, 5), ha='center')

    plt.show()
