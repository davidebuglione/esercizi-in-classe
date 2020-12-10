linguaggio_svizzero=input("inserire una parola o una frase in rovarspraket da tradurre")
lista_linguaggio_svizzero=[]
for lettera in linguaggio_svizzero:
    lista_linguaggio_svizzero.append(lettera)
vocali=["a","e","i","o","u"]
for lettera2 in lista_linguaggio_svizzero:
    index_consonante=lista_linguaggio_svizzero.index(lettera2)
    if lettera2 not in vocali and lista_linguaggio_svizzero[index_consonante+1]=="o":
        lista_linguaggio_svizzero.remove(lista_linguaggio_svizzero[index_consonante+1])
        lista_linguaggio_svizzero.remove(lista_linguaggio_svizzero[index_consonante])
print("la parola o frase tradotta è:")
for lettera3 in lista_linguaggio_svizzero:
    print(lettera3,end="")
print()