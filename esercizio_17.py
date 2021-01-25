geografia={}
list_nazioni=[]
list_capitali=[]
print("per interrompere il ciclo digitare 1 quando viene richiesta la nazione")
while True:
    nazione=input("inserire una nazione ")
    if nazione == "1":
        break
    list_nazioni.append(nazione)
    print("inserire la capitale della", nazione, end=" ")
    capitale=input()
    list_capitali.append(capitale)
for nazione in list_nazioni:
    key_index=list_nazioni.index(nazione)
    geografia[nazione]=list_capitali[key_index]
invert_geografia={}
list_keys=[]
list_valori=[]
for key in geografia:
    list_keys.append(key)
for elemento in geografia:
    list_valori.append(geografia[elemento])
counter=0
for i in range(len(list_keys)):
    invert_geografia[list_valori[counter]]=list_keys[counter]
    counter+=1
key_nazione=input("inserire il nome della capitale di cui si desidera conoscere la rispettiva nazione ")
if key_nazione in invert_geografia:
    print("la nazione di cui è capitale",key_nazione,"è la seguente:",invert_geografia[key_nazione])
else:
    print("questa capitale non risulta nell'elenco fornito il quale comprende:")
    for elemento in invert_geografia:
        print(elemento, end=", ")