d_fatturato={"nord":[],"centro":[],"sud":[],"isole":[]}
fatturato_tot=0
for elemento in d_fatturato:
    print("inserire il fatturato di:",elemento,end=" ")
    fatturato=int(input())
    d_fatturato[elemento].append(fatturato)
    fatturato_tot+=fatturato
for elemento in d_fatturato:
    fatturato_rel=d_fatturato[elemento[0]]/fatturato_tot*100
    d_fatturato[elemento].append(fatturato_rel)
print("il fatturato totale è stato di:",fatturato_tot,"$")
for elemento in d_fatturato:
    print("il fatturato relativo di: ",elemento,"è stato del",d_fatturato[elemento[1]],"%")