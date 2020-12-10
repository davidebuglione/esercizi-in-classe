parola=input("inserire una parola per verificare se si tratta di un palindromo")
lista_lettere=list(parola)
lista_lettere_inverse=[]
for lettera in parola:
    lista_lettere_inverse.append(lettera)
lista_lettere_inverse.reverse()
if lista_lettere==lista_lettere_inverse:
    print("sì, la parola è un palindromo")
else:
    print("no,la parola non è un palindromo")