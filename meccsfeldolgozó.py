class Meccs():
    def __init__(self,csapat1nev,csapat2nev,meccsdatum,bajnoksag,fordulo,csapat1gol,csapat2gol,tamadasok,helyszín,nezoszam,jatekvezeto):
        self.csapat1nev = csapat1nev
        self.csapat2nev = csapat2nev
        self.meccsdatum = meccsdatum
        self.bajnoksag = bajnoksag
        self.fordulo = fordulo
        self.csapat1gol = int(csapat1gol)
        self.csapat2gol = int(csapat2gol)
        self.tamadasok = tamadasok
        self.helyszín = helyszín
        self.nezoszam = nezoszam
        self.jatekvezeto = jatekvezeto

    def nyertes(self):
        if self.csapat1gol > self.csapat2gol:
            return self.csapat1nev
        elif self.csapat1gol < self.csapat2gol:
            return self.csapat2nev
        else:
            return "Döntetlen"
    
    def osszgol(self):
        return self.csapat1gol+self.csapat2gol

    def __repr__(self):
        return f"{self.csapat1nev} {self.csapat2nev} {self.meccsdatum} {self.bajnoksag} {self.fordulo} {self.csapat1gol} {self.csapat2gol} {self.tamadasok} {self.helyszín} {self.nezoszam} {self.jatekvezeto}"


def kiemeléshatár():
    print("=" * 40)
def kiemelés(szoveg):
    kiemeléshatár()
    print(f"{szoveg.center(40)}")
    kiemeléshatár()
Meccsek = []
with open("meccsek.txt", "r", encoding="utf-8") as bemenet:
    for sor in bemenet:
        bontas = sor.split(";")
        csapat1nev = bontas[0]
        csapat2nev = bontas[1]
        meccsdatum = bontas[2]
        bajnoksag = bontas[3]
        fordulo = bontas[4]
        csapat1gol = bontas[5]
        csapat2gol = bontas[6]
        tamadasok = bontas[7]
        helyszín = bontas[8]
        nezoszam = bontas[9]
        jatekvezeto = bontas[10]
        Meccsek.append(Meccs(csapat1nev,csapat2nev,meccsdatum,bajnoksag,fordulo,csapat1gol,csapat2gol,tamadasok,helyszín,nezoszam,jatekvezeto))
print("Melyik meccs statisztikáit szeretnéd megnézni?")
szamlalo = 1
for meccsek in Meccsek:
    print(f"{szamlalo}. {meccsek.csapat1nev} vs {meccsek.csapat2nev}")
    szamlalo += 1
választó = int(input("Meccs száma: "))
valasztott = Meccsek[választó -1]
kiemelés(f"{valasztott.csapat1nev} vs {valasztott.csapat2nev}")
print(f"-Csapat 1: {valasztott.csapat1nev}")
print(f"-Csapat 2: {valasztott.csapat2nev}")
print(f"-Dátum: {valasztott.meccsdatum}")
print(f"-Bajnokság: {valasztott.bajnoksag}")
print(f"-Bajnoksági forduló: {valasztott.fordulo}.")
print(f"-{valasztott.csapat1nev} gólok: {valasztott.csapat1gol}")
print(f"-{valasztott.csapat2nev} gólok: {valasztott.csapat2gol}")
print(f"-Összes gól: {valasztott.osszgol()}")
print(f"-Összes támadás: {valasztott.tamadasok}")
print(f"-Nyertes: {valasztott.nyertes()}")
print(f"-Helyszín: {valasztott.helyszín}")
print(f"-Nézőszám: {valasztott.nezoszam}")
print(f"-Játékvezető: {valasztott.jatekvezeto}")