import datetime

print('Salutare, acesta este laboratorul numarul 1')
print('Introdu numele tau')
numele_tau = input()
print('Salut' + ' '+ numele_tau)

variabila_de_tip_numerica = 5
variabila_de_tip_text_scurta = "Python"
variabila_de_tip_reala = 6.0
variabila_cu_multe_randuri = """ primul rand 
al doilea rand
al treilea rand 
"""

print(type(variabila_cu_multe_randuri))
print(type(variabila_de_tip_numerica))

print(len(variabila_cu_multe_randuri))

transformarea_textului_in_litere_mari = variabila_de_tip_text_scurta.upper()
print(transformarea_textului_in_litere_mari)

variabila_care_va_fi_taiata = 'Acesta este acest text'
variabila_taiata = variabila_care_va_fi_taiata[0:9]
print(variabila_taiata)

# variabilele atribuite in metoda fstring
varsta = 20
inaltimea = 180
numele = 'Victor'
variabilele_atribuite_in_metoda_1 = f'Ma numesc {numele} am {varsta} de ani si inaltimea de {inaltimea} de cm'
print(variabilele_atribuite_in_metoda_1)

#variabilele atribuite in metoda string
variabilele_atribuite_in_metoda_2 = " Temperatura in {orasul} este de {temperatura}, iar ora este {ora} !"
print(variabilele_atribuite_in_metoda_2.format(orasul = 'New York', temperatura = '80F', ora = datetime.datetime.now()))

variabilele_atribuite_in_metoda_2 = " Temperatura in {} este de {}, iar ora este {} !"
print(variabilele_atribuite_in_metoda_2.format('New York', '80F', datetime.datetime.now()))


#sarcina 2 - punctul a
txt = 'More results from text...'
substr = txt[4:12]
print(substr)
print(substr.strip())

#sarcina 2 - punctul b
txt = 'More results from text...'
print(txt.split())

#sarcina - punctul c
age = 36
txt = 'My name is Mary, and i am {}'
print(txt.format(age))