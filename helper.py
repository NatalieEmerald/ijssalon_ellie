def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(inkomsten):
    totaal = sum(inkomsten.values())
    return totaal