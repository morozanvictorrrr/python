# #sarcina nr 1
# #-----------------------------------------------------------------------------

# varsta = int(input("Scrie vrsta ta\n"))
# while varsta < 20 or varsta > 120:
#     print("Ai trecut limita privind varsta, scrie din nou varsta ta")
#     varsta = int(input("Scrie varsta ta\n"))

# inaltimea = int(input("Scrie inaltimea ta in cm\n"))
# while inaltimea < 150 or inaltimea > 220:
#     print("Ai trecut limita privind inaltimea, scrie din nou greutatea ta")
#     inaltimea = int(input("Scrie inaltimea ta in cm\n"))

# greutatea = float(input("Scrie greutatea ta in cm\n"))
# while greutatea < 45 or greutatea > 300:
#     print("Ai trecut limita privind greutatea, scrie din nou greutatea ta")
#     greutatea = float(input("Scrie greutatea ta in cm\n"))


# print("Daca esti barbat scrie 0, daca esti femeie scrie 1")

# gen = int(input("Ce gen esti?\n"))

# if gen == 0:
#     greautatea_ideala = inaltimea - 100 -(((inaltimea - 150)/4) + ((varsta - 20)/4))
#     print(f"Greutatea ideala pentru barbat este {greautatea_ideala} - kg ")
#     if greutatea - greautatea_ideala > 0:
#         greutatea_necesara = greutatea -greautatea_ideala
#         print(f"Trebuie sa slabesti {greutatea_necesara} - kilograme")
#     elif greutatea - greautatea_ideala < 0:
#         greutatea_necesara = greautatea_ideala - greutatea
#         print(f"Trebuie sa adaugi {greutatea_necesara} - kilograme")
#     else: 
#         print("Greutatea este ideala")
# elif gen == 1:
#     greautatea_ideala = inaltimea - 100 -(((inaltimea - 150)/2.5) + ((varsta - 20)/6))
#     print(f"Greutatea ideala pentru femeie este {greautatea_ideala} - kg")
# else :
#     print("Ai introdus ceva gresit")

#-----------------------------------------------------------------------------
#sarcina 2

def calculeaza_varsta_omeneasca():
  raspuns = input("este pisica mai mica de un an? daca da scrie - (da), daca nu scrie - (nu): ")

  if raspuns in ("da"):
    luni_omeneasca = {
        1: 6,
        2: 10,
        3: 2,
        4: 5,
        5: 8,
        6: 14,
        7: 15,
        8: 16,
        9: 16,
        10: 17,
        11: 17,
    }

    while True:
      try:
        luni_pisica = int(input("cate luni are pisica taa? introdu un numar de la 1 la 11: "))
        if 1 <= luni_pisica <= 11:
          break
        else:
          print("trebuie sa scrii o valoare de la 1 la 11.")
      except ValueError:
        print("eroare de valoare trebuie sa scrii o valoarea intreaha")

    print(f"pisica ta are {luni_omeneasca[luni_pisica]} luni omenesti.")

  elif raspuns in ("nu"):
    while True:
      try:
        ani_pisica = int(input("cati ani are pisica ta, scrie un numar de la 1 la 35 : "))
        if 1 <= ani_pisica <= 35:
          break
        else:
          print("trebuie sa scrii o valoare de la 1 la 11.")
      except ValueError:
        print("eroare de valoare trebuie sa scrii o valoarea intreaga")

    if ani_pisica == 1:
      ani_omenesti = 18
    elif ani_pisica == 2:
      ani_omenesti = 25
    elif 3 <= ani_pisica <= 15:
      ani_omenesti = 25 + (ani_pisica - 2) * 4
    else:
      ani_omenesti = 25 + (15 - 2) * 4 + (ani_pisica - 15) * 3

    print(f"daca ar fi in ani omenesti, pisica ta ar avea {ani_omenesti} ani.")

  else:
    print("Ai introdus ceva gresit, incearca din nou ")

if __name__ == "__main__":
  calculeaza_varsta_omeneasca()