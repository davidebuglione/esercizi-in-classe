numero_decimale=int(input("inserire il numero decimale che si desidera trasformare in binario"))
funzione_python=bin(numero_decimale)
numeri_binari=[]
numeri_binari.append(numero_decimale%2)
while numero_decimale!=1:
    numero_decimale//=2
    resto=numero_decimale%2
    numeri_binari.append(resto)
numeri_binari.reverse()
print("Il numero trasformato in binario è:")
for number in numeri_binari:
    print(number,end="")
print(" per dimostrarti che il mio risultato è corretto ecco ciò che dice la funzione bin di python:")
print(funzione_python)