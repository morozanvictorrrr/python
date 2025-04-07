#problema 1

# greet_user = lambda name: print("Hello my dear",name)
# user_name = input("What is your name")
# greet_user(user_name)

#problema 2

# prima_lista_tuplu = [(3,11),(1,7),(7,8),(16,88),(23,15)]
# rezultatul_sortarii = sorted(prima_lista_tuplu,key=lambda tuplu:tuplu[1])
# print(rezultatul_sortarii)

#problema 3 

# cuvinte = ["mere","banane","pere","cirese","portocale","cartofi"]
# cuvinte_sortate = sorted(cuvinte,key=lambda cuvant: len(cuvant))
# print(cuvinte_sortate)

#problema 4 a)

#functie fara parametri 
# def functie_fara_parametri():
#     print("functia fara parametri")
# functie_fara_parametri()

#functie cu parametri 
# def functie_cu_parametri(x,y):
#     print(f"Adunam a cu b, a fiind a - {x},si b fiind b - {y}, iar rezultatul este {x+y}")
# functie_cu_parametri(10,20)

#functia cu valori predefinite pentru parametri, voi scrie doar una,e la fel pentru fiecare
# def functia_cu_valori_predefinita(varsta = 20):
#     print(f"Ai varsta de {varsta} de ani")
# functia_cu_valori_predefinita() #aici va folosi valoare implicita
# functia_cu_valori_predefinita(60) #iar aici va folosi argumentul 60 

#problema 4 b)

#functie care returneaza un rezultat 
# def functia_care_returneaza_un_rezultat(x,y):
#     return x*y
# rezultat = functia_care_returneaza_un_rezultat(10,20)
# print(rezultat)

#functia care returneaza un rezultat si nu foloseste return, implicit returneaza None

# def mesaj(text):
#     print(f"Mesajul este {text}")
# mesaj("ca nu returneaza nimic")
    

#functia cu argumente cheie
# def date_personale_persoana(nume,varsta,oras):
#     print(f"Ma numesc {nume}, am {varsta} de ani si locuiesc in {oras}")
# date_personale_persoana(nume="Victor",varsta=20,oras="Orhei")