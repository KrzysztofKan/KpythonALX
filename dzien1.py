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
dl = len(str(string))
it = dl
while it != 0:
    suma += int(string[it-1])
    it -= 1
print('Suma cyfr liczby',string ,'to',suma)
