import copy
import utils as u


lista_multi = [
    [3, -5, -4, 3, 2, 9], 
    [9, 2, 3, 4], 
    [9, 19, 82, 43, -9, -2, 0],
    [3, 5, 55, 555, 2, 9],
    [-4, 7]
]

lista_multi_2 = [
    [13, 2, 23, 24, -5,-7],
    [2, 7, 6, 4, 11, 19, 45],
    [123, 5, 7]
]

slownik = {
    'aaa' : ['aaa']
}

uczen_ocena = {
    'Tomek Kowalski' : [4,3,5,4],
    'Darek Niewidomski':[3.5,4,5,5],
    'Milosz Kolski': [2,5,4,2],
    'Aleksandra Salata' : [4.5,5,4,5,3]
}

lista_przedmiotow = ['Matematyka','Programowanie Python','Jezyk Angielski','Logika']


def zad1(list=[]):
    tmp = 1000
    min = []
    for wiersz in list:
        for ele in wiersz:
            if ele < tmp:
                tmp = ele
        min.append(tmp)
        tmp = 1000
    return min
        
def zad2():
    pass

def zad3():
    pass

def zad4():
    pass

def zad5():
    pass

def zad6():
    slownik = {
        'war1' : [23,4,3,233,4,6],
        'war2' : [7,5,3,4,22,-100],
        'war3' : [11,4,3,2,9],
        'war4' : [9,8,17,72,500]
    }
    idx = 1
    for key in slownik:
        print(key,sum(slownik['war'+ str(idx)]))
        idx+=1
    
    idx=1
    tmp = 0
    max = ''
    for key in slownik:
        if sum(slownik['war'+ str(idx)]) >= tmp:
            tmp = sum(slownik['war'+ str(idx)])
            max = 'war'+ str(idx)
        idx+=1
    print('Najwieksza:',max,tmp)
            





    pass

def zad7():
    flag = True
    while flag:
        inp = input('Podaj slowo:')
        fg2 =False
        if inp == 'koniec':
            flag = False
            break
        for key in slownik.keys():
            if u.is_anagram(inp,key):
                slownik[key].append(inp)
                fg2 = False
            else: fg2 =True
        if fg2: slownik[inp] = []
        print(slownik)

def zad8():
    idx = 0
    for pr in lista_przedmiotow:
        print('\t',pr)
        for key in uczen_ocena:
            print(key,uczen_ocena[key][idx])
        idx +=1

def zad9():
    idx = 0
    key = ''
    tmp2 = 0
    for ucz in uczen_ocena:
        tmp = (sum(uczen_ocena[ucz])/len(uczen_ocena[ucz]))
        if tmp > tmp2:
            tmp2 = tmp
            key = ucz
        idx +=1
    print(key,tmp2)
    

def zad10():
    niezaliczone = {'':['']}
    idx = 0
    for przedmiot in lista_przedmiotow:
        for uczen in uczen_ocena:
            for ocena in uczen:
                if uczen[ocena[idx]] >=2:
                    niezaliczone[uczen].append[przedmiot]
    
    print(niezaliczone)


    pass






def main():
    #print(zad1(lista_multi))
    #zad6()
    #zad7()
    #zad8()
    #zad9()
    #zad10()
    pass
    


main()


# idx = 0
# for ele in lista_m2:
#     for x in ele:
#         if x <=0:
#             ele.pop(idx)

#         else:
#             idx+=1
#     idx = 0

# print(lista_m2)
# listwynik2 = [0,0,0,0,0]

# idx1 = 0
# for ele in lista_multi:
#     for el in ele:
#         listwynik2[idx1] += el
#     idx1+=1
# idx1 = 0

# print(listwynik2)