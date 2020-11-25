totale_stipendi=0
numero_stipendi=0
while True:
    stipendio=input("inserire il valore di uno stipendio")
    if stipendio=="-1":
        break
    else:
        stipendio=int(stipendio)
        totale_stipendi+=stipendio
        numero_stipendi+=1
media=int(totale_stipendi/numero_stipendi)
print("la media degli stipendi è",media,"$")