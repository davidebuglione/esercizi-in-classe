n_veicoli=0
giorno=0
ls_veicoli=[]
print("scrivere 0 per interrompere le domande")
while True:
    print("giorno",giorno)
    flusso_veicoli=int(input("quanti veicoli hanno attraversato il casello oggi?"))
    if flusso_veicoli==0:
        break
    giorno+=1
    ls_veicoli.append(flusso_veicoli)
start_counter_veicoli=int(input("a partire da quale giorno vuoi vedere quanti veicoli hanno attraversato il casello?"))
finish_counter_veicoli=int(input("fino a quale giorno?"))
somma_veicoli=sum(ls_veicoli[start_counter_veicoli:finish_counter_veicoli+1])
print("in totale hanno attraversato il casello",somma_veicoli,"veicoli")