città_con_escursione=[]
gradi_di_escursione=[]
valore_di_controllo=float(input("quanti gradi vale il valore prefissato per il controllo dell'escursione termica che si desidera monitorare?"))
print("(per interrompere l'elenco delle città prese a campione digitare 1)")
while True:
    nome=input("digitare il nome della città")
    if nome=="1":
        break
    print("a quanti gradi ammonta la temperatura massima registrata a ",nome,"?")
    temperatura_massima=float(input())
    print("a quanti gradi ammonta la temperatura minima registrata a ",nome,"?")
    temperatura_minima=float(input())
    escursione=temperatura_massima-temperatura_minima
    if escursione>=valore_di_controllo:
        città_con_escursione.append(nome)
        gradi_di_escursione.append(escursione)
print("hanno superato il valore prefissato le seguenti ",len(città_con_escursione)," città:")
index_città=0
for i in range(len(città_con_escursione)):
    print(città_con_escursione[index_città]," con un'escursione di", gradi_di_escursione[index_città]," gradi")
    index_città+=1