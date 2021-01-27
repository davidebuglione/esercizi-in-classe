conto={}
print("per interrompere le richieste digitare stop quando viene richiesto il numero di conto")
while True:
    n_conto=input("inserire il numero di conto bancario ")
    if n_conto=="stop":
        break
    print("inserire il saldo del conto numero", n_conto,": $", end="")
    saldo=input()
    conto[n_conto]=saldo
while True:
    trova_conto=input("digitare il numero di conto di cui si desidera conoscere il saldo ")
    if trova_conto not in conto:
        print("numero di conto non valido")
    else:
        break
print()
print("il saldo del conto numero", trova_conto,"è di", conto[trova_conto],"$")