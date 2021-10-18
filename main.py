from math import sqrt


def prim(n):
    '''
    Determina daca un numar este prim sau nu
    :param n: numar intreg
    :return: returneaza true daca n e prim, si daca nu, returneaza false
    '''
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def citire_lista():
    '''
    Citeste o lista de numere intregi
    :return: lista de numere intregi
    '''
    lst = []
    lst = list(input("Scrieti elementele despartite de spatiu").split())
    lista = [int(x) for x in lst]
    return lista


def eliminare_prime(lst:list[int]):
    '''
    Modifica lista de numere intregi, prin eliminarea celor prime
    :param lst: lista de numere intregi
    :return: returneaza lista, neavand numere prime
    '''
    i = 0
    while i < len(lst):
        if prim(lst[i]) is True:
            lst.remove(lst[i])
            i = i - 1
        i = i + 1
    return lst


def calculare_medie_aritmetica(lst:list[int]):
    '''
    Calculeaza si returneaza media aritmetica a elementelor din lista
    :param lst: lista de numere intregi
    :return: returneaza media aritmetica
    '''
    medie_aritmetica = sum(lst)
    lungime = len(lst)
    return medie_aritmetica / lungime


def comparare_medie(lst:list[int], n):
    '''
    Compara media aritmetica a listei cu numarul n
    :param lst: lista de numere intregi
    :param n: numar intreg
    :return: returneaza True daca media e mai mare ca n, False in caz contrar
    '''
    if calculare_medie_aritmetica(lst) > n:
        return True
    return False


def inserare_divizori_proprii(lst:list[int]):
    '''
    Insereaza in lista data, dupa fiecare element, divizorii sai proprii
    :param lst: lista de numere intregi
    :return: returneaza lista careia s-au adaugat divizorii proprii
    '''
    count = 0
    i = 0
    lungime = len(lst)
    while i < lungime:
        count = 0
        for j in range(2, lst[i] // 2 + 1):
            if lst[i] % j == 0:
                count += 1
                lst.insert(i + count, j)
        i = i + 1 + count
        lungime = len(lst)
    return lst


def modificare_lista_tuple(lst:list[int]):
    '''
    Realizeaza o lista de tuple-uri, in care pe prima pozitie se afla pozitia
    elementului, pe a doua se afla valoarea sa, si in a treia se afla numarul de aparitii
    :param lst: lista de numere intregi
    :return: returneaza lista de tuple-uri
    '''
    lista_tuple = []
    for i in range(len(lst)):
        lista_tuple.append((lst[i], i, lst.count(lst[i])))
    return lista_tuple


def test_prim():
    assert prim(3) is True
    assert prim(1) is False
    assert prim(61) is True


def test_eliminare_prime():
    assert eliminare_prime([1, 3, 8, 10]) == [1, 8, 10]
    assert eliminare_prime([10, 20, 30]) == [10, 20, 30]
    assert eliminare_prime([2, 2, 2]) == []


def test_comparare_medie():
    assert comparare_medie([10, -3, 25, -1, 3, 25, 18], 10) is True
    assert comparare_medie([20, 30, 10], 40) is False
    assert comparare_medie([1, 1, 1], 1) is False


def test_inserare_divizori_proprii():
    assert inserare_divizori_proprii([1, 5, 10, 3]) == [1, 5, 10, 2, 5, 3]
    assert inserare_divizori_proprii([1, 3, 7]) == [1, 3, 7]
    assert inserare_divizori_proprii([10, 8, 3]) == [10, 2, 5, 8, 2, 4, 3]


def test_modificare_lista_tuple():
    assert modificare_lista_tuple([25, 13, 26, 13]) == [(25, 0, 1), (13, 1, 2), (26, 2, 1), (13, 3, 2)]
    assert modificare_lista_tuple([10, 3, 4]) == [(10, 0, 1), (3, 1, 1), (4, 2, 1)]
    assert modificare_lista_tuple([1, 1, 1, 1]) == [(1, 0, 4), (1, 1, 4), (1, 2, 4), (1, 3, 4)]


def test_all():
    test_comparare_medie()
    test_prim()
    test_inserare_divizori_proprii()
    test_eliminare_prime()
    test_modificare_lista_tuple()


test_all()


def main():
    optiune = """
    Daca doresti sa citesti lista, scrie '1'.
    Daca doresti sa elimini numerele prime din lista, si sa afisezi lista, scrie '2'.
    Daca doresti sa afli daca media aritmetica a elementelor listei e mai mare ca un numar, scrie '3'.
    Daca doresti sa afisezi lista modificata prin inserarea divizorilor proprii dupa fiecare numar, scrie '4'.
    Daca doresti sa formezi un o lista de tuple-uri de forma (valoare, index, numar de aparitie) a fiecarui element, scrie '5'.
    Daca doresti sa opresti programul, scrie '6'.
    """
    while True:
        alegere = input(optiune)
        if alegere == '1':
            lista = citire_lista()
        elif alegere == '2':
            print(eliminare_prime(lista))
        elif alegere == '3':
            comparator = int(input("Scrieti numarul pe care doriti sa-l comparati cu media. Daca e mai mare decat media, va scrie 'Da', altfel, 'Nu': "))
            if comparare_medie(lista, comparator) is True:
                print("DA")
            else:
                print("NU")
        elif alegere == '4':
            print(inserare_divizori_proprii(lista))
        elif alegere == '5':
            print(modificare_lista_tuple(lista))
        elif alegere == '6':
            print("Programul s-a oprit!")
            break
        else: print("Comanda inexistenta")

if __name__== main():
    main()





