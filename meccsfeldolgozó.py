class Meccs():
    def __init__(self,csapat1nev,csapat2nev,meccsdatum,bajnoksag,fordulo,tamadasok,helyszín,nezoszam,jatekvezeto):
        self.csapat1nev = csapat1nev
        self.csapat2nev = csapat2nev
        self.meccsdatum = meccsdatum
        self.bajnoksag = bajnoksag
        self.fordulo = fordulo
        self.tamadasok = tamadasok
        self.helyszín = helyszín
        self.nezoszam = nezoszam
        self.jatekvezeto = jatekvezeto
    def __repr__(self):
        return f"{self.csapat1nev} {self.csapat2nev} {self.meccsdatum} {self.bajnoksag} {self.fordulo} {self.tamadasok} {self.helyszín} {self.nezoszam} {self.jatekvezeto}"
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
        helyszín = bontas[6]
        nezoszam = bontas[7]
        jatekvezeto = bontas[8]
        Meccsek.append(Meccs(csapat1nev,csapat2nev,meccsdatum,bajnoksag,fordulo,tamadasok,helyszín,nezoszam,jatekvezeto))
print(Meccsek)