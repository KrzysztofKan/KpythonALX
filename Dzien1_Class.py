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
 
w = 0
 
while w < N:
    k = 0
    while k < N:
        print('x', end=' ')
        k +=1
    print()
    w += 1
