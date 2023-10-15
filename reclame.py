from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):

    text = f"Vandag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    
    return text

print(aanbieding_1("aardbei", 4, 4-0.1*4))


def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    bedrag = (totaal * 0.09)
    text = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return text

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))


def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return hoogste, laagste

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))  

def gemiddelde(mijn_lijst):
    sum1 = sum(mijn_lijst)
    bedrag = sum1 // len(mijn_lijst)
    text = f"De gemiddelde inkomsten daze week zijn {bedrag} euro."
    return text

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    result = laag_en_hoog(invoer_lijst)
    return result

print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

input_list_2 = [1, 2, 3]
list = combinatie(input_list_2)

print(list)