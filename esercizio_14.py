while True:
    stop=input("per interrompere digitare 1 altrimenti premere INVIO")
    if stop=="1":
        break
    a=int(input("inserire il valore di a"))
    b=int(input("inserire il valore di b"))
    if a*b>10:
        print(a-b)
    elif a*b<=10:
        print(a+b)