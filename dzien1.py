#
# print('zadanie1:', end=' ')
# start_z1 = 0
# end_z1 = 100
# while start_z1 < end_z1 +1:
#     print(start_z1, end=' ')
#     start_z1 +=1
# print('\n')
#
#
# print('zadanie2:', end=' ')
# start_z2 = 50
# end_z2 = -50
# while start_z2 > end_z2 -1:
#     print(start_z2, end=' ')
#     start_z2 -=1
# print('\n')
#
#
# print('zadanie3:', end=' ')
# start_z3 = 50
# end_z3 = -50
# while start_z3 > end_z3 -1:
#     print(start_z3, end=' ')
#     start_z3 -=5
# print('\n')
#
#
# print('zadanie4:', end=' ')
# start_z4 = -30
# end_z4 = 30
# while start_z4 < end_z4 +1:
#     if start_z4 %2 == 0:
#         print(start_z4, end=' ')
#     start_z4 +=1
# print('\n')


N1 = 15
T = N1
print('Zadanie 1, Dzielniki liczby ',N1,' to :', end= ' ')
while T > 0:
    if N1 %T == 0:
        print(T,end=' ')
    T -=1
print('\n')

N2 = 15
T = N2
count = 0
print('Zadanie 2, ',N2,' ma dzielnikow :', end= ' ')
while T > 0:
    if N2 %T == 0:
        count +=1
    T -=1
print(count,'\n')

string = '548'
suma = 0
dl = len(string)
while dl != 0:
    suma += int(string[dl-1])
    dl -= 1
print('Zadanie 3, Suma cyfr liczby',string ,'to',suma)


liczba = 14
T2 = liczba
count = 0
while T2 > 0:
    if liczba %T2 == 0:
        count +=1
    T2 -=1
if count == 2:
    print('Zadanie 4 ',liczba,' jest liczba pierwsza')
else:
    print('Zadanie 4 ',liczba, ' nie jest liczba pierwsza')
    

liczbad = 496
sumad = 0
T3 = liczbad -1
while T3 > 0:
    if liczbad %T3 ==0:
        sumad +=T3
    T3 -=1
if liczbad == sumad:
    print('Zadanie 5 ',liczbad,' jest doskonala')
else:
    print('Zadanie 5 ',liczbad, ' nie doskonala')
