The repository for the final exam of the Python crash course held by PhD Professor Del Coco Marco.

# Traccia 
## Esercitazione Finale
Realizzare un programma in Python per gestire una classe Studente. 
Ogni oggetto della classe dovrà rappresentare uno studente con alcune informazioni personali e alcune azioni che può compiere.

### Obiettivi 
La classe Studente deve avere almeno questi attributi:
- nome
- cognome
- eta
- matricola
- voti (una lista di numeri)

La classe deve contenere almeno questi metodi:
- presentati() → stampa o restituisce una breve presentazione dello studente
- aggiungi_voto(voto) → aggiunge un voto alla lista
- calcola_media() → restituisce la media dei voti
- studia(ore) → stampa un messaggio che descrive l’attività dello studente

Consegna un programma che:

- Definisca la classe Studente.
- Usi il metodo init per inizializzare tutti gli attributi principali.
- Crei almeno due oggetti della classe Studente.
- Chiami i metodi su ciascun oggetto per mostrare che ogni istanza mantiene il proprio stato, cioè i propri attributi e dati.
- Stampi i risultati in modo chiaro.

# Interpretazione del codice "main.py"

Il codice presente nel file "main.py" presenta una classe Studente inizializzata con il metodo __init__ che contiene le variabili richieste nella consegna.
Nella classe, inoltre, sono definite le funzioni obiettivo d'esame.

In particolare, ho incluso degli elementi decorativi per separare le schede Studenti stampate a video, qualora fossero presenti uno o più studenti.

La richiesta "aggiungi_voto(voto)" è stata eseguita tramite l'utilizzo della funzione ".append" per includere il nuovo valore nel vettore voti.

La funzione "media" dei voti è stata calcolata tramite la somma del vettore "voti", diviso per la lunghezza del vettore, come richiede la formula della media aritmetica (sommatoria "∑" da "i = 0" a "n" dei "x(i)" elementi, diviso per gli "n" elementi). Per facilità di lettura, il risultato della media viene arrotondato a 2 cifre decimali.

Infine, ho creato la sezione "ore di studio", con l'inserimento di commenti sulla preparazione ad un fittizio esame in base alle ore di studio svolte.

Ho dichiarato quindi due studenti con parametri inventati per una veloce verifica di funzionamento flawless del codice.

