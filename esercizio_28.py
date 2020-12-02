studenti=[]
valori_lanci=[]
print("per interrompere l'elenco digitare 1")
while True:
    nome=input("inserire il nome dello studente: ")
    if nome=="1":
        break
    lancio=float(input("inserire la distanza raggiunta in metri"))
    studenti.append(nome)
    valori_lanci.append(lancio)
indice_vincitore=valori_lanci.index(max(valori_lanci))
valore_vincitore=max(valori_lanci)
vincitore=studenti[indice_vincitore]
print("ha vinto",vincitore,"raggiungerndo la distanza di",valore_vincitore,"metri")