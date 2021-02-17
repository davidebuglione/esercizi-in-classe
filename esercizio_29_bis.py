reddito=int(input("inserire il reddito "))
if reddito<=15000:
    imposta=reddito/100*23
    print("L'imposta ammonta a:",imposta,"$")
elif reddito>15000 and reddito<=28000:
    imposta=3450+((reddito-15000)/100*27)
    print("L'imposta ammonta a:",imposta,"$")
elif reddito>28000 and reddito<=55000:
    imposta=3450+3510+((reddito-28000)/100*38)
    print("L'imposta ammonta a:",imposta,"$")
elif reddito>55000 and reddito<=75000:
    imposta=3450+3510+10259.62+((reddito-55000)/100*41)
    print("L'imposta ammonta a:",imposta,"$")
else:
    imposta=3450+3510+10259.62+8199.59+((reddito-75000)/100*43)
    print("L'imposta ammonta a:",imposta,"$")