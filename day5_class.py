uczen_ocena = {
    'Tomek Kowalski' : [4,3,5,4],
    'Darek Niewidomski':[3.5,4,5,5],
    'Milosz Kolski': [2,5,4,2],
    'Aleksandra Salata' : [4.5,5,4,5,3]
}

lista_przedmiotow = ['Matematyka','Programowanie Python','Jezyk Angielski','Logika']


id_studenta_oceny = {
    's0001' : [4, 2, 5, 4, -1],
    's0003' : [3.5, 4, None, 5, 7],
    's3212' : [2, 5, 4, 2, 5],
    's7621' : [5,4,3,3,2]
}

id_studenta_info = {
    's0003' : ['Maria', 'Jackowska', 'informatyka'],
    's0001' : ['Ela', 'Jabłońska', 'politologia'],
    's7621' : ['Jakub', 'Niewiadomski', 'informatyka'],
    's3212' : ['Tomasz', 'Dziedzic', 'politologia']
}

def zad1():
    for uczen in uczen_ocena.keys():
        idx = 0
        while idx < 5:
            try:
                print(uczen,uczen_ocena[uczen][idx])
                idx+=1
            except:
                tmp = input(uczen)
                uczen_ocena[uczen] += tmp
                idx+=1
            # if uczen_ocena[uczen][idx] > 0:
            #     print(uczen_ocena[uczen][idx])
            #     idx+=1
    print(uczen_ocena)

# zad 5 Wypisz kazdego studenta Imie, nazwisko, oraz srednia z wystawionych ocen pod warunkiem ze wszystkie 
# oceny sa wystawione i sa wystawione poprawnie w innej sytuacji wypisz komunikat o błędnie wystawionych ocenach
def zad2():
    flag = True
    for student in id_studenta_info:
        print(id_studenta_info[student][0],id_studenta_info[student][1],end=": ")
        for ocena in id_studenta_oceny[student]:
            if ocena > 0:
                flag = False
        if flag == True:
            try:
                print(sum(id_studenta_oceny[student])/len(id_studenta_oceny[student]))
            except:
                print("zle wystawiona oceny")
        else:
            print("zle wystawiona oceny")
    flag = True



    pass


def main():
    #zad1()
    zad2()


main()