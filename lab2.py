# sarcina 1
#mai departe punctul b)
#---------------------------------------------------------------------------------------------

# lista = [1,2,3]
# lista1 = [1,2,3]
# prima_valoare = lista[0]
# doua_valoarea = lista[2]
# print(prima_valoare,doua_valoarea)

# lista[0] = 4
# print(lista)

# l = lista
# print(l)
# lista.append(5)
# print(lista)

# ex_cu_prima_functie = sum(lista)
# print("suma lor va fi ", ex_cu_prima_functie)

# ex_cu_doua_functie = len(lista)
# print("lungimea elementrelor va fi de ", ex_cu_doua_functie)


# lista_concatenata1 = [1,2,3]
# lista_concatenata2 = [4,5,6]
# lista_concatenata3 = lista_concatenata1 + lista_concatenata2
# print("folosind operatorul de concatenare primesc ", lista_concatenata3)
# lista_concatenata3[0] = -1

# lista_repetata = lista_concatenata3 * 2
# print("lista repetata de 2 ori va fi lista concatenata 3 de 2 ori la rand ", lista_concatenata3)

# if 1 in lista_concatenata1:
#     print("este")
# else :
#     print("nu este")

#mai departe punctul c)
#---------------------------------------------------------------------------------------------

# tuplu_definit = (1,2,3,4,5,6,7)
# print("arat ca este tuplu aici - ", type(tuplu_definit))



# prima_valoare = tuplu_definit[0]
# ultima_valoare = tuplu_definit[-1]
# print(prima_valoare,ultima_valoare)

# extractie_tuplu = tuplu_definit[0:2]
# print(extractie_tuplu)

# prima_functie_tuplu = len(tuplu_definit)
# doua_functie_tuplu = max(tuplu_definit)
# treia_functie_tuplu = min(tuplu_definit)
# print("cele 3 functii sunt aici ", prima_functie_tuplu,doua_functie_tuplu,treia_functie_tuplu)


#mai departe punctul d)
#---------------------------------------------------------------------------------------------


# setul_simplu = {1,2,3,4,5,6,7, 66776, 343, 989, 234, 456}

# print(setul_simplu)
# setul_cu_valori_repetate = {1,2,2,3,3,3,4,5,5,6}
# print("setul cu valori care se repeta" ,setul_cu_valori_repetate)

# setul_simplu.add(8)
# print("deja va arata si cifra 8 in acest set",setul_simplu)

# numarul_elementelor_al_setului = len(setul_simplu)
# print("numarul elementelor este dee", numarul_elementelor_al_setului)

#mai departe punctul e)
#---------------------------------------------------------------------------------------------





# dictionar_de_tip_text = {
#     "nume": "Victor",
#     "localitatea": "Orhei"
# }

# print("nume este", dictionar_de_tip_text["nume"])
# print("localiatea este", dictionar_de_tip_text["localitatea"])

# dictionar_de_tip_numeric = {
#     1: "fotbal",
#     2: "volei",
# }
# dictionar_de_tip_text["scoala"] = "nr1"

# print("primul sport este ", dictionar_de_tip_numeric[1])
# print("al doilea sport este", dictionar_de_tip_numeric[2])


# cheiele_dictionarului_de_tip_text = dictionar_de_tip_text.keys()
# print('cheile la ala de tip text sunt', cheiele_dictionarului_de_tip_text) 

# valorile_dictionarului_de_tip_text = dictionar_de_tip_text.values()
# a = list(valorile_dictionarului_de_tip_text)
# dictionar_de_tip_text['scoala'] = 'nr1'
# print('valorile la dictionarul de tip text sunt', a)

# for v in valorile_dictionarului_de_tip_text:
#     print(v)




# lungimea_dictionarului_de_tip_text = len(dictionar_de_tip_text)
# print('lungimea dictionarului de tip text este ', lungimea_dictionarului_de_tip_text)

# lungimea_dictionarului_de_tip_text = len(dictionar_de_tip_text)
# print('lungimea dictionarului de tip text este ', lungimea_dictionarului_de_tip_text)

# dictionar_cu_argumente_keyword = dict(nume="Mihai",localitatea="Orhei")
# print(dictionar_cu_argumente_keyword)


#mai departe punctul f)
#---------------------------------------------------------------------------------------------

# numar_float = 1.672919
# print("tipul de date este:", type(numar_float))  # va arata float

# numar_intreg = int(numar_float)
# print("tipul de date dupa modificare est:", type(numar_intreg))  # va arata deja integer
# print("valoarea numarului intreg este - :", numar_intreg)  


#sarcina 2
#mai departe punctul a)
#---------------------------------------------------------------------------------------------

# costuri = [10000, 200000, 300000]
# produse = ["masina", "casa", "apartament"]
# for i in range(len(produse)):
#     print("fiecare {} are un pret de {} euro.".format(produse[i], costuri[i]))


#mai departe punctul b)
#---------------------------------------------------------------------------------------------

# varsta_utilizatorului = input("scrie varsta ta: ")
# varsta_convertita_in_numar = int(varsta_utilizatorului)
# varsta_peste_5_ani = varsta_convertita_in_numar + 5
# print(" peste 5 ani o sa ai varsta de " + str(varsta_peste_5_ani) + " ani.")


#mai departe punctul c)
#---------------------------------------------------------------------------------------------
# lista_mea = [1,2,3,4,5,6,7]

# if 5 in lista_mea:
#     print("am 5 aici")

# if 10 not in lista_mea:
#     print("nu am 10 aici")


#-------------------------------------------FINAL--------------------------------------------------
