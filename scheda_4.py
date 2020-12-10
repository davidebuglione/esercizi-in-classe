while True:
    print("quale area vuoi calcolare?")
    print()
    print("1) Area del quadrato")
    print("2) Area del rettangolo")
    print("3) Area del triangolo")
    print("4) Area del cerchio")
    scelta=input()
    unità_misura=input("inserire l'unità di misura in simboli")
    if scelta=="1" or scelta=="1)":
        lato_q=int(input("inserire la lunghezza del lato "))
        print("l'area del quadrato è",lato_q*lato_q,unità_misura)
        break
    elif scelta=="2" or scelta=="2)":
        lato_r_lungo=int(input("inserire la lunghezza del lato lungo"))
        lato_r_corto=int(input("inserire la lunghezza del lato corto"))
        print("l'area del rettangolo è",lato_r_lungo*lato_r_corto,unità_misura)
        break
    elif scelta=="3" or scelta=="3)":
        base_t=int(input("inserire la lunghezza dela base"))
        altezza_t=int(input("inserire la lunghezza dell'altezza"))
        print("l'area del tringolo è",base_t*altezza_t/2,unità_misura)
        break
    elif scelta=="4" or scelta=="4)":
        diametro=int(input("inserire la lungheza del diametro"))
        print("l'area del cerchio è", diametro*3.14,unità_misura)
        break
    else:
        print("scelta non accettata, ritentare")
        print()