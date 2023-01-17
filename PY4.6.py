#kuupäev
def kuu_nimi(o):
    kuud = ["", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[o]
def kuupaev(p,l,a):
    print(f"{p}. {l} {a}. a")
vastus = input("Sisesta kuupäev kujul DD.MM.YYYY: ")
p,k,a = vastus.split(".")
kuupaev(p,kuu_nimi(int(k)),a)