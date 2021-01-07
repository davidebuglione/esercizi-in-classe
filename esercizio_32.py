print("questo programma risolve un'equazione di primo grado di tipo ax+b=0")
a=int(input("inserire il valore di a "))
b=int(input("inserire il valore di b "))
if a==0 and b==0:
    print("l'equazione è indeterminata")
elif a!=0 and b==0:
    print("il risultato è x=0")
elif a==0 and b!=0:
    print("l'equazione è impossibile")
elif a!=0 and b!=0:
    x=-(b/a)
    print("x=",round(x,3))