Documento dei Requisiti – Progetto 3M
1. Titolo del progetto
Gantt & Preventivi Generator

2. Obiettivo
Il programma ci deve far creare automaticamente:
diagrammi di Gantt esportati in PNG
preventivi professionali esportati in PNG
3. Attori
Utente / Operatore  inserisce dati per Gantt o preventivo


4. Requisiti funzionali
Il programma deve:
Avviare con un menu principale
Permettere di scegliere tra:
Creazione Gantt
Creazione Preventivo
Gestire input dell’utente (date, costi, attività)
Generare:
Gantt come immagine PNG
Preventivo come immagine PNG
Salvare i file su disco
Mostrare anteprima testuale o riepilogo
Usare almeno un package Python esterno
(Extra) salvare dati in file JSON

5. Requisiti non funzionali
1)Interfaccia a console chiara e semplice
2)Gestione errori (date sbagliate, input numerici)
3)Codice diviso in più file (moduli)
4)Commenti e documentazione base
5)Struttura leggibile e modulare

6. Scelta del package Python
Package principali consigliati:
matplotlib
Per creare i diagrammi di Gantt
Pillow
Per generare immagini PNG dei preventivi
pandas (opzionale)
Per gestire dati in modo ordinato
Esempio compilato:
Package scelto: matplotlib, Pillow
 Perché lo abbiamo scelto:
1)matplotlib permette di creare grafici tipo Gantt
2)Pillow permette di creare immagini personalizzate
Come lo usiamo nel progetto:
matplotlib  disegna le barre del Gantt
Pillow  crea il layout del preventivo (testo + tabelle)

7. Suddivisione del lavoro
Essendo in :
Nichita Moraru: gestione menu + input utente
Zampini Diego: Gantt (date, attività)
Cami Tibiano: preventivi + generazione PNG (Pillow)generazione immagini Gantt (matplotlib)

8. Flusso del programma
Menu iniziale
1 → Crea Gantt
2 → Crea Preventivo
3 → Esci
Se Gantt:
Inserimento attività
Inserimento date
Generazione immagine
Se Preventivo:
Inserimento cliente
Inserimento servizi + costi
Calcolo totale
Generazione immagine
Output finale
File PNG salvato

9. Cronoprogramma (Gantt semplificato)
Settimana 1: idea, scelta package, requisiti
Settimana 2: progettazione + struttura codice
Settimana 3: sviluppo Gantt + preventivi
Settimana 4: test, miglioramenti, consegna

10. Note aggiuntive
 Idee extra per migliorare il progetto
Template grafici diversi (stile moderno, aziendale)
Esportazione anche in PDF
Salvataggio progetti
Modifica di un Gantt già creato
Aggiunta colori personalizzati
Calcolo automatico durata attività
Logo aziendale nei preventivi
Sconti e IVA automatici
Timeline con milestone
Interfaccia grafica (bonus avanzato con tkinter)
Generare Gantt da file CSV
Import/export dati
Mini dashboard riepilogo
Versione web futura (con Flask)

brain storm nuove idee —-----------------------------------------------------------------------

A.A.C: gambling (se va bene prendiamo soldi extra, se va male facciamo pagare di meno)




per nuove ideee
