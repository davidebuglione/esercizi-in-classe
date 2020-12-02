numero_cifre=int(input("da quante cifre è composto il numero binario che si desidera convertire in decimale?"))
print("scrivere le cifre binarie una alla volta a partire da destra")
elevatore_potenze=0
numero_decimale=0
for i in range(numero_cifre):
    cifra=int(input())
    numero_da_sommare=cifra*(2**elevatore_potenze)
    numero_decimale+=numero_da_sommare
    elevatore_potenze+=1
numero_binario=input("non sono sicuro di aver fatto giusto, potresti riscrivere il numero da sinistra verso destra?")
numero_certo=int(numero_binario,2)
if numero_decimale==numero_certo:
    print("ok ora sono sicuro, il numero decimale è ",numero_decimale)
else:
    print("prenderò 2 in informatica")