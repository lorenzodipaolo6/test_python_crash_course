# Creazione della classe "Studente", con i parametri "Nome, Cognome, Età, Matricola e Voti".
class Studente:
    def __init__(self, nome, cognome, eta, matricola, voti):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = voti

    # Creazione del metodo "presentati", che presenta lo studente con il suo nome, cognome e i voti ottenuti.
    def presentati(self):
        print(
            f"Ciao! Sono lo studente {self.nome} {self.cognome}\nIl mio libretto è composto dai seguenti voti: {self.voti}\n"
        )

    # Creazione del metodo "aggiungi_voto", che aggiunge un nuovo voto al libretto dello studente
    # e stampa il nuovo voto e il libretto aggiornato.
    def aggiungi_voto(self, nuovo_voto):
        self.voti.append(nuovo_voto)
        print(
            f"Ho ottenuto un nuovo voto: {nuovo_voto}\nIl mio libretto studente, aggiornato all'ultimo esame, è composto da: {self.voti}\n"
        )

    # Creazione del metodo "calcola_media", che calcola la media del vettore voti e ne stampa il risultato,
    # arrotondato a 2 cifre decimali.
    def calcola_media(self):
        media = sum(self.voti) / len(self.voti)
        print(f"La media dei miei voti è: {media:.2f}\n")

    # Creazione del metodo "studia", che prende in input il numero di ore di studio e
    # stampa un messaggio in base al numero di ore studiate.
    def studia(self, ore):
        self.ore = ore
        if self.ore > 10:
            print(f"Ho studiato per {self.ore} ore, sono pronto per l'esame.\n")
        elif self.ore > 5:
            print(f"Ho studiato per {self.ore} ore, devo prepararmi meglio.\n")
        else:
            print(f"Ho studiato per {self.ore} ore, non sono pronto per l'esame.\n")


# Creazione di due soggetti Studente ("Lorenzo" e "Piero") e call dei metodi.
Lorenzo = Studente("Lorenzo", "Di Paolo", 25, 20112651, [28, 28, 27])
Lorenzo.presentati()
Lorenzo.aggiungi_voto(20)
Lorenzo.calcola_media(Lorenzo.voti)
Lorenzo.studia(3)

Piero = Studente("Piero", "Rossi", 22, 20112652, [30, 29, 25, 27])
Piero.presentati()
Piero.aggiungi_voto(28)
Piero.calcola_media(Piero.voti)
Piero.studia(12)
