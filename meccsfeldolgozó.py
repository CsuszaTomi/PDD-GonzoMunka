class Meccs():
    def __init__(self,csapat1nev,csapat2nev,meccsdatum,bajnoksag,fordulo,tamadasok,nyertes,helyszín,nezoszam,jatekvezeto):
        self.csapat1nev = csapat1nev
        self.csapat2nev = csapat2nev
        self.meccsdatum = meccsdatum
        self.bajnoksag = bajnoksag
        self.fordulo = fordulo
        self.tamadasok = tamadasok
        self.nyertes = nyertes
        self.helyszín = helyszín
        self.nezoszam = nezoszam
        self.jatekvezeto = jatekvezeto
    def __repr__(self):
        return f"{self.csapat1nev} {self.csapat2nev} {self.meccsdatum} {self.bajnoksag} {self.fordulo} {self.tamadasok} {self.nyertes} {self.helyszín} {self.nezoszam} {self.jatekvezeto}"
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
        tamadasok = bontas[5]
        nyertes = bontas[6]
        helyszín = bontas[7]
        nezoszam = bontas[8]
        jatekvezeto = bontas[9]
        Meccsek.append(Meccs(csapat1nev,csapat2nev,meccsdatum,bajnoksag,fordulo,tamadasok,nyertes,helyszín,nezoszam,jatekvezeto))
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
print(f"-Összes támadás: {valasztott.tamadasok}")
print(f"-Nyertes: {valasztott.nyertes}")
print(f"-Helyszín: {valasztott.helyszín}")
print(f"-Nézőszám: {valasztott.nezoszam}")
print(f"-Játékvezető: {valasztott.jatekvezeto}")