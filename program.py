print("--- MINI KALKULAČKA ---")

# 1. Vypýtame si čísla
cislo1 = float(input("Napíš prvé číslo: "))
operacia = input("Vyber si operáciu (+, -, *, /): ")
cislo2 = float(input("Napíš druhé číslo: "))

# 2. Podmienky pre rôzne operácie
if operacia == "+":
    vysledok = cislo1 + cislo2
    print("Výsledok sčítania je: " + str(vysledok))

elif operacia == "-":
    vysledok = cislo1 - cislo2
    print("Výsledok odčítania je: " + str(vysledok))

elif operacia == "*":
    vysledok = cislo1 * cislo2
    print("Výsledok násobenia je: " + str(vysledok))

elif operacia == "/":
    # Ošetrenie, aby sme nedelili nulou (to počítače nemajú radi)
    if cislo2 == 0:
        print("Chyba: Nulou sa nedá deliť!")
    else:
        vysledok = cislo1 / cislo2
        print("Výsledok delenia je: " + str(vysledok))

else:
    print("Zvolil si neplatnú operáciu!")

# Brzda pre okno
input("\nStlač Enter pre ukončenie...")
