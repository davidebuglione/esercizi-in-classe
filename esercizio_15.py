geografia={}
while True:
    print("per interrompere il ciclo digitare 1 quando viene richiesta la nazione")
    while True:
        nazione=input("inserire una nazione ")
        if nazione == "1":
            break
        print("inserire la capitale della", nazione, end=" ")
        capitale=input()
        geografia[nazione]=capitale
    key_capitale=input("inserire il nome della nazione di cui si desidera conoscere la capitale")
    if key_capitale in geografia:
        print("la capitale della",key_capitale,"è",geografia[key_capitale])
    else:
        print("questa nazione non risulta nell'elenco fornito il quale comprende:")
        for elemento in geografia:
            print(elemento, end=", ")
        print()
        stop=input("se si desidera inserire nuove nazioni digitare 2")
        if stop!="2":
            break