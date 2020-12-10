print("per interrompere la lista di parole inserire 1")
lista_parole=[]
lista_numeri=[]
while True:
    parola=input("inserire una parola")
    if parola=="1":
        break
    lista_parole.append(parola)
counter=0
for i in range(len(lista_parole)):
    lista_numeri.append(len(lista_parole[counter]))
    counter+=1
print("la lunghezza complessiva delle parole è",sum(lista_numeri))
counter=0
for quantità in lista_numeri:
    print(lista_parole[counter],"ha",quantità,"lettere")
    counter+=1