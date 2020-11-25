voti1=int(input("inserire i voti del candidato1"))
voti2=int(input("inserire i voti del candidato2"))
voti_totali=voti1+voti2
percentuale1=int(voti1/voti_totali*100)
percentuale2=int(voti2/voti_totali*100)
print("il candidato 1 ha ricevuto", voti1,"voti su",voti_totali,"con una percentuale del",percentuale1,"%")
print("il candidato 2 ha ricevuto",voti2,"voti su",voti_totali,"con una percentuale del",percentuale2,"%")
if voti1>voti2:
    print("ha vinto il candidato 1, complimenti!")
elif voti1==voti2:
    print("pareggio!")
elif voti2>voti1:
    print("ha viinto il candidato 2, complimenti!")