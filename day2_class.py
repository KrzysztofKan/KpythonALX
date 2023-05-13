print('Hello World', end=' ')
print('Hello World')

# Koemntarz, czyli cos nie widocznego dla komputera

liczba = 50
print(type(liczba))

liczba_zmiennoprzecinkowa = 4.56
print(type(liczba_zmiennoprzecinkowa))

wartosc_logiczna = False
print(type(wartosc_logiczna))

text = 'Ala ma kota'
print(type(text))

# operatory:

# operatory matematyczne: + - * / // % **
# operatory arytmetyczne: += -= *= /= //= %= **=

l1 = 50
l2 = 20
print(l1 + l2)

l1 += l2

# operatory porównania: < > <= >= != ==
# operator przypisania: =
# operatory logiczne: and or not
#* operatory bitowe/binarne

l1 = 40
l2 = 40

print(l1 != l2)

if 0 < l1 < 100:
    print('Liczba jest dodatnia')
elif l1 < 1000:
    print('jest mneijsza od 1000')
elif l1 < 10000:
    print('mniejsza od 10000')
else:
    print('dla pozostałych')


# zad 1 Sprawdz czy liczba jest w zakresie od -50 do 50
liczba = 30

if -50 < liczba < 50:
    print('zawiera sie w przedziale od -50 do 50')
else:
    print('nie zawiera sie')



# zad 2 Przedzial A = (3, 12), B = (15, 21>, odpowiedz na pytanie
# do ktorego zbioru nalezy zmienna N, lub wypisz komunikat ze nie nalezy do zadnego

N = 8

if 3 < N < 12:
    print('Nalezy do zbioru A')
elif 15 < N <= 21:
    print('Nalezy do zbioru B')
else:
    print('Nie nalezy nigdzie')


# zad 3 A = (-12, 2), B = <-5, 11>, C = (5, 24)
# zad 3* wypis przynaleznosci do przedzialu ma byc w jednej linii
# - nalezy do A i B

# N  = 11
#
# if -5 < N < 2:
#     print('Nalezy do A i B')
# elif 5 < N < 11:
#     print('Nalezy do B i C')
# elif -12 < N < -5:
#     print('Nalezy do A')
# elif 11 < N < 24:
#     print('Nalezy do C')
# elif 2 < N < 5:
#     print('Nalezy do B')
# else:
#     print('Nie nalezy do zadnego')

# start = 10
# while start < 20:
#     print(start)
#     start += 1

# zad 1 wypisz liczby od 0 do 100
# start = 0
# while start <= 100:
#     print(start)
#     start += 1

# zad 2 wypisz liczby od 50 do -50

# start = 50
#
# while start >= -50:
#     print(start)
#     start -= 1

# zad 3 Wypisz liczby od 50 do -50 co 5

# start = 50
# while start >= -50:
#     print(start)
#     start -= 5
# zad 4 wypisz tylko liczby nieparzyste od -30 do 30

# start = -30
# while start <= 30:
#     if start % 2 != 0:
#         print(start)
#     start += 1

# zad 1 Dla danej liczby N wypisz wszystkie jej dzielniki
#
# n = 28
# dzielnik = 1
# ile_dzielnikow = 0
# while dzielnik <= n:
#     if n % dzielnik == 0:
#         print(dzielnik)
#         ile_dzielnikow += 1
#     dzielnik += 1
#
# print(ile_dzielnikow)
# zad 2 Policz ile dana liczba ma dzielnikow
# zad 3* Wypisz sume cyfr danej liczby np. 548 -> 5 + 4 +8

# liczba = 7582
# suma = 0
#
# while liczba > 0:
#     suma += liczba % 10
#     liczba //= 10
#     print(f'Suma: {suma}, Liczba: {liczba}')
#
# print(suma)

# zad 4 sprawdz czy dana liczba jest liczba pierwsza

# n = 28
# dzielnik = 1
# ile_dzielnikow = 0
# while dzielnik <= n:
#     if n % dzielnik == 0:
#         # print(dzielnik)
#         ile_dzielnikow += 1
#     dzielnik += 1
#
# if ile_dzielnikow == 2:
#     print('Jest liczba pierwsza')
# else:
#     print('Nie jest liczba pierwsza')

# zad 5 sprawdz czy dana liczba jest liczba doskonala
# (ktorej suma dzielnikow mniejszych od niej jest rowna tej liczbie)
# np 28 -> 1, 2, 4, 7, 14

# n = 28
# dzielnik = 1
# suma_dzielnikow = 0
# while dzielnik < n:
#     if n % dzielnik == 0:
#         # print(dzielnik)
#         suma_dzielnikow += dzielnik
#     dzielnik += 1
#
# if suma_dzielnikow == n:
#     print('Jest liczba doskonala')
# else:
#     print('Nie jest liczba doskonala')

# zad 1 Wypisz 15 kolejnych wielokrotnosci liczby N

# N = 3
# ile = 1
#
# while ile < 15 :
#     print(ile * N)
#     ile += 1

# zad 2 Wypisz 10 kolejnych poteg liczby N

# N = 3
# ile = 0
#
# while ile < 10:
#     print(N ** ile)
#     ile += 1

# zad 3 Oblicz silnie z danej liczby N

# wynik = 1
# N = 5
# start = 1
# while start <= N:
#     wynik *= start
#     start += 1
#
# print(wynik)

# rok_ur = int(input('Podaj mi rok urodzenia:'))
#
# print(type(rok_ur))
# print(rok_ur)

# zad 1 pobierz dwie liczby od usera wypisz nwd z tych liczb
# 12 8 -> 4
# 88, 42 -> 2
#

# l1 = int(input('Liczba1:'))
# l2 = int(input('Liczba2:'))
#
# while l1 != l2:
#     if l1 > l2:
#         l1 -= l2
#     else:
#         l2 -= l1
#
# print(l1)

# zad 2 pobierz dwie liczby od usera wypisz nww z tych liczb

# l1 = int(input('Liczba1:'))
# l2 = int(input('Liczba2:'))
# tmp_l1 = l1
# tmp_l2 = l2
#
# while l1 != l2:
#     if l1 > l2:
#         l2 += tmp_l2
#     else:
#         l1 += tmp_l1
#
# print(l1)


#
# 3 4 -> 12
# 11, 6 -> 66

# zad 1 Jaka najwieksza potega liczby a, zmiesci sie w liczbie b ?
# a = 2
# b = 100
# ile = 1
#
# while a ** ile < b:
#     ile +=1
# ile -= 1
#
# print(a ** ile)
# print(ile)

# zakres = range(5) # range(2, 8), range(2, 12, 2)
#
# print(zakres)
# print(type(zakres))
#
# for idx in zakres:
#     print(idx)
#
#
# # zad 1 Wypisz 15 kolejnych wielokrotnosci liczby N
# N = 3
#
# for wielokrotnosc in range(1, 16):
#     print(N * wielokrotnosc)
#
# # zad 2 Wypisz 10 kolejnych poteg liczby N
# N = 3
#
# for potega in range(11):
#     print(N ** potega)
#
# # zad 3 Oblicz silnie z danej liczby N
# N = 5
# wynik = 1
# for i in range(1, N+1):
#     wynik *= i
#
# print(wynik)

# N = 5
#
# x x x x x
# x x x x x
# x x x x x
# x x x x x
# x x x x x

N = 5
# for w in range(N):
#     for k in range(N):
#         print('x', end=' ')
#     print()

# w = 0
#
# while w < N:
#     k = 0
#     while k < N:
#         print('x', end=' ')
#         k +=1
#     print()
#     w += 1


# bool -> True/False

# czy = True
# ile = 10
#
# while czy:
#     print(ile)
#     ile -= 1
#
#     if ile == 0:
#         czy = False

# niesławna instrukcja break i continue

# ile = 10
#
# for e in range(ile+1):
#     if e == 5:
#         continue
#     print(e)

ile = 10

# for e in range(ile+1):
#     if e == 5:
#         break
#     print(e)

# e = 0
# czy = True
# while czy:
#     if e == 5:
#         czy = False
#     print(e)
#     e+= 1


# zad 1
# n = 5
#
# o x x x o
# x o x o x
# x x o x x
# x o x o x
# o x x x o

# n = 10
#
# for w in range(n):
#     for k in range(n):
#         if w == k or (w + k + 1) == n:
#             print('o', end=' ')
#         else:
#             print('x', end=' ')
#     print()


# zad 2
# n = 5
#
# x o x o x
# o x o x o
# x o x o x
# o x o x o
# x o x o x
# N = 8
# w = 0
#
# while w < N:
#     k = 0
#     while k < N:
#         if (w + k) % 2 == 0:
#             print('o', end= ' ')
#         else:
#             print('x', end=' ')
#         k += 1
#     w += 1
#     print()

# n = 5
#
# x
# x x
# x x x
# x x x x
# x x x x x

# x x x x x
#   x x x x
#     x x x
#       x x
#         x

#         x
#       x x
#     x x x
#   x x x x
# x x x x x
czy = True

print(type(czy))

# x x x x x
# x x x x
# x x x
# x x
# x

# zad 1 wypisz liczby pierwsze z zakresu od 0 do 100

# for n in range(1, 100):
#
#     ile_dzielnikow = 0
#
#     for dzielnik in range(1, n+1):
#         if n % dzielnik == 0:
#             ile_dzielnikow += 1
#
#     if ile_dzielnikow == 2:
#         print(n)


# zad 2 Wypisz tabliczke mnozenia 10 x 10 (do 100)
# n = 10
# for e in range(1,n +1):
#     for e1 in range(1, n+1):
#         print(e * e1, end='\t')
#     print()

# zad 3 Znajdz 4 kolejne liczby doskonale

# ile = 4
# liczba = 1
# while ile:
#     suma_dzielnikow = 0
#     for dzielnik in range(1, liczba):
#         if liczba % dzielnik == 0:
#             suma_dzielnikow += dzielnik
#     if suma_dzielnikow == liczba:
#         print(liczba)
#         ile -= 1
#     liczba += 1
    # sprawdzanie kolejnej liczby naturalnej czy jest liczba doskonala
    # jesli znajdziemy, zmniejszamy zmienna ile


# zad 4* znajdz 5,6,7 kolejnych liczb doskonalych w czasie ponizej 2 sekundy

import random as r

print(int(r.random()*100) + 50)


# zad 1 wylosuj liczbe z zakresu od 50 do 100
# zad 2 wylosuj liczbe z zakresu od -50 do 20
print(int(r.random()*70)-50)
# zad 3 wylosuj liczbe parzysta z zakresu od 0 do 100
print(int(r.random()*50)*2)
# zad 4 wylosuj liczbe nieparzysta z zakresu od -50 do 50
print(int(r.random()*50)*2 -1 -50)

# zad 5 wylosuj 10 liczb bedacych podzielnymi przez 3 lub 7 z zakresu od -100 do 100
# ile = 10
#
# while ile:
#     liczba = int(r.random()*200 -100)
#     if liczba % 3 == 0 or liczba % 7 == 0:
#         print(liczba)
#         ile -= 1

# zad 6 losuj liczby z zakresu od 0 do 10 tak dlugo az nie zostana wylosowane 2 liczby pod rzad takie same
# starsza = int(r.random()*10)
# nowsza = int(r.random()*10)
# print(starsza)
# print(nowsza)
# while starsza != nowsza:
#     starsza = nowsza
#     nowsza = int(r.random()*10)

# zad 7 losuj liczby z zakresu od -10 do 10 az nie wylosujesz liczby 6
#
# liczba = -1
# while liczba != 6:
#     liczba = int(r.random() * 20 - 10)
#     print(liczba)

# zad 8 zagraj z userem w zgadnij liczbe, komputer losuje, my zgadujemy, wypisz za ktorym razem zgadlismy
# zad 9 dopisz do zad 8 komunikaty, mneijsza, wieksza, równa
# zad 10 odwrotna sytuacja niz zad 8, user wporwadza komputer zgaduje

# lista = list()
# lista = []
# lista = [4, 3, 2, 3, 4,5, 6]
#
# # print(lista[100])
# print(lista[-4]) # wyswietlenie elementu z lista
# print(len(lista))   # ilosc elementow na liscie
# lista.append(10)        # dodanie elemenot na koniec
# if 4 in lista:      # sprawdzenie czy istneije ewewnatrz listy
#     lista.remove(4)     # usuniecie po wartosci jesli wystepuje, jesli nie to blad
#
# lista.insert(3, 1000)       # wstawienie na okreslona pozycje z przesuniecie elementow w liscie
# lista[3] = -1000            # wstawienie na okrelsona pozycje z nadpisaniem
#
# print(lista)
#
#
#
# # ele = lista.pop(3)
# # lista.insert(3, ele)
# print(lista)
#
lista = [1,2,3,4,5]
# lista_tmp = lista.copy()
#
# print(lista)
# print(lista_tmp)
# lista[2] = 1000
# print(lista)
# print(lista_tmp)
#
# for e in lista:
#     print(e)

# zad 1 Wypisz sume elementow z tablicy
# zad 2 Wypisz wartosc najmniejsza z tablicy
# zad 3 Wypisz srednia arytmetyczna elementow z tablicy
# zad 4 Wypisz index miejsca gdzie wystepuje wartosc najwieksza

# suma = 0
#
# for e in lista:
#     suma += e
# print(round(suma/len(lista), 2))

# najmniejszy = lista[0]
#
# for e in lista:
#     if e < najmniejszy:
#         najmniejszy = e
#
# print(najmniejszy)

# idx_max = 0
#
# idx = 0
# while idx < len(lista):
#     # print(lista[idx])
#
#     if lista[idx_max] < lista[idx]:
#         idx_max = idx
#     idx+= 1
#
# print(idx_max)

# zad 5 Czy wiecej jest elementow parzystych dodatnich czy nieaprzystych ujemnych w liscie

# parzy_dod = 0
# nieparzy_uje = 0
#
# for e in lista:
#     if e % 2 == 0 and e > 0:
#         parzy_dod += 1
#     elif e % 2 != 0 and e < 0:
#         nieparzy_uje += 1
#
# if nieparzy_uje > parzy_dod:
#     print('Wiecej jest nieparzyystych ujemnych')
# elif nieparzy_uje < parzy_dod:
#     print('Wiecej jest parzystych dodatnich')
# else:
#     print('Po tyle samo')

# zad 6 znajdz w liscie wszytskie elementy ujemne i nadpisz je 0

# idx = 0
#
# while idx < len(lista):
#     if lista[idx] < 0:
#         lista[idx] = 0
#     idx += 1
#
# print(lista)
# zad 7 Wypisz z listy tylko liczby pierwsze


# for e in lista:
#     ilosc_dzielnikow = 0
#
#     for dzielnik in range(1, e + 1):
#         if e % dzielnik == 0:
#             ilosc_dzielnikow += 1
#
#     if ilosc_dzielnikow == 2:
#         print(e)

# zad 8 czy lista czytana od prawej do lewej ma taka sama kolejnosc elementow jak od lewej do prawej
# np. [1,3,8,2,2,8,3,1]

czy_kolejnosc_taka_sama = True

start = 0
koniec = len(lista)-1

while start < koniec:

    if lista[start] != lista[koniec]:
        czy_kolejnosc_taka_sama = False

    start += 1
    koniec -= 1

if czy_kolejnosc_taka_sama:
    print('Jest taka sama')
else:
    print('Jest rozna')

print(lista == lista[::-1])
print(sum(lista))
print(min(lista))
print(max(lista))


lista_1 = [2,4,22,1,3,9, -5, -2]
lista_2 = [5,7,1,3,9, -2, 9, 11]


# zad 9 usun wszytskie leemnty ktore koncza sie cyfra 1 lub 3

idx = 0

while idx < len(lista):
    if lista[idx] % 10 == 1 or lista[idx] % 10 == 3:
        print(lista.pop(idx))
        idx -= 1
    idx += 1

# zad 10 stworz 2 listy, wypisz elementy wspolne z obu list

for e in lista_1:
    if e in lista_2:
        print(e)

# zad 11 wypisz elementy niewpsolne

for e in lista_1:
    if not e in lista_2:
        print(e)

for e in lista_2:
    if not e in lista_1:
        print(e)

# zad 1 majac 2 listy bez tworzenia nowej, napisz rpogram ktory wszytskie dodatnie elementy zgrupuje na liscie 1, ujemne na liscie 2

idx_1 = 0

while idx_1 < len(lista_1):
    if lista_1[idx_1] < 0:
        lista_2.append(lista_1.pop(idx_1))
        idx_1 -= 1
    idx_1 += 1

idx_1 = 0

while idx_1 < len(lista_2):
    if lista_2[idx_1] > 0:
        lista_1.append(lista_2.pop(idx_1))
        idx_1 -= 1
    idx_1 += 1


# zad 2 dla jednej listy znajdz element wystepujacy najwieksza ilosc razy:
# a) jedna z tych liczb
# b) ile razy wystepuje maxymalny element ? np. 5 razy
# ponawiamy główny kod zeby sprawdzic ktore elementy wystepuja 5 razy

max_ele = lista[0]
max_wys = 0

# for e1 in lista:
#     suma = 0
#     for e2 in lista:
#         if e1 == e2:
#             suma += 1
#     if max_wys < suma:
#         max_wys = suma
#         max_ele = e1


# for e1 in lista:
#     suma = lista.count(e1)
#     if max_wys < suma:
#         max_wys = suma
#         max_ele = e1

# print(f'Element {max_ele} wystepuje {max_wys} razy.')

lista = [
[2,4,5,2,-2],
[12,2,6,22,12],
[9,-4,-5,12,-22],
[12,11,8,7,0],
[9,2,1,5,4]
]

print(lista)
print(len(lista))
print(lista[2][4])

for list_e in lista:
    for e in list_e:
        print(e, end=' ')
    print()

# zad 1 suma wszystkich elementow z 2 wymairowej listy
suma = 0

for list_e in lista:
    for e in list_e:
        suma += e

print(suma)

# zad 2 pozycja (w/k) najmneiojszego elementu

# zad 3 suma elementow w wierszach

suma = 0

for list_e in lista:
    suma = 0
    for e in list_e:
        suma += e

    print(suma)


# zad 4 suma elementow w kolumnach

numer_kolumny = 3

nr_wiersza = 0
suma = 0
while nr_wiersza < len(lista):
    suma += lista[nr_wiersza][numer_kolumny]
    nr_wiersza += 1
    
print(suma)
    
