candidato1=input("inserire il nome del primo candidato").upper()
candidato2=input("inserire il nome del secopndo candidato").upper()
voticandidato1=int(input("quanti voti ha ricevuto il candidato 1?"))
voticandidato2=int(input("quanti voti ha ricevuto il candidato 2?"))
if candidato1>candidato2:
    print("L'ordine alfabetico dei candidati è",candidato1,candidato2)
elif candidato2>candidato1:
    print("L'ordine alfabetico dei candidati è",candidato2,candidato1)
if voticandidato1>voticandidato2:
    print("l'ordine in base ai voti è:",candidato1,candidato2,": ha vinto",candidato1)
elif voticandidato2>voticandidato1:
    print("l'ordine in base ai voti è:",candidato2,candidato1,": ha vinto",candidato2)
elif voticandidato2==voticandidato1:
    print("i candidati hanno concluso in pareggio")