print("PER INTERROMPERE LA REGISTRAZIONE DI PARTECIPANTI DIGITARE stop")
ls_partecipanti=[]
partecipanti_confermati=[]
counter=1
while True:
    print("inserire il nome del partecipante numero",counter, end=" ")
    partecipante=input()
    if partecipante=="stop":
        break
    ls_partecipanti.append(partecipante)
    counter+=1
counter=1
print("se desideri inviare una mail di conferma a tutti i partecipanti digitare ok",
"altrimenti per selezionare manualmentente i partecipanti a cui inviare la mail premere invio", end=" ")
conferma_all=input()
if conferma_all=="ok":
    for persona in ls_partecipanti:
        partecipanti_confermati.append(persona)
        ls_partecipanti.remove(persona)
else:
    for persona in ls_partecipanti:
        print("desideri inviare una mail di conferma al partecipante numero", counter, ":", persona,
        "?", " (rispondere ok oppure no)",end=" ")
        counter+=1
        risposta_conferma=input()
        if risposta_conferma=="ok":
            partecipanti_confermati.append(persona)
            ls_partecipanti.remove(persona)
print("ecco la lista dei partecipanti a cui vuoi inviare una mail di conferma:")
for partecipante in partecipanti_confermati:
    print(partecipante)
while True:
    cambia_mail=input("se desideri fare qualche modifica digitare ok ")
    verifica_anti_crash="ok"
    if cambia_mail=="ok":
        if conferma_all=="ok" and verifica_anti_crash=="ok":
            print("per interrompere le richieste di modifiche digitare stop")
            while True:
                elimina=input("inserire il nome del partecipante che si desidera eliminare dalla lista delle mail di conferma ")
                if elimina=="stop":
                    break
                eliminato=partecipanti_confermati.pop(partecipanti_confermati.index(elimina))
                ls_partecipanti.append(eliminato)
                verifica_anti_crash="no"
        else:
            print("per interrompere le richieste di modifiche digitare stop")
            while True:
                print("se si desidera eliminare un partecipante dalla lista delle mail di conferma",
                "digitare il nome, altrimenti digitare no", end=" ")
                eliminare=input()
                if eliminare=="stop":
                    break
                if eliminare != "no":
                    elimina=input("inserire il nome del partecipante che si desidera eliminare dalla lista delle mail di conferma ")
                    eliminato=partecipanti_confermati.pop(partecipanti_confermati.index(elimina))
                    ls_partecipanti.append(eliminato)
                aggiungere=input("se si desidera aggiungere un partecipante alla lista delle mail di conferma",
                "digitare il nome, altrimenti digitare no")
                if aggiungere!="no":
                    aggiungi=input("inserire il nome del partecipante che si desidera aggiungere alla lista delle mail di conferma ")
                    aggiunto=ls_partecipanti.pop(ls_partecipanti.index(aggiungi))
                    partecipanti_confermati.append(aggiunto)
    if conferma_all != "ok":
        print("ecco la lista dei partecipanti a cui vuoi inviare le mail di conferma:")
        for persona in partecipanti_confermati:
            print(persona)
    print("ecco la lista dei partecipanti a cui non viene inviata la mail:")
    for persona in ls_partecipanti:
        print(persona)
    check_finale=input("se desideri apportare ulteriori modifiche digitare ok")
    if check_finale != "ok":
        break