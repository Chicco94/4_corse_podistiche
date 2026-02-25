# Corse Podistiche - Piattaforma di Valutazione Gare

**Versione Online:** https://chicco94.pythonanywhere.com/

## Descrizione

Corse Podistiche è un'applicazione web che permette ai runner di valutare e condividere le loro esperienze su gare podistiche. Gli utenti possono registrare nuove gare, lasciare recensioni dettagliate basate su molteplici criteri e consultare le valutazioni di altri partecipanti.

## Funzionalità Principali

### Per gli Utenti
- **Registrazione e Autenticazione:** Crea un account per accedere alle funzionalità della piattaforma
- **Creazione Gare:** I runner possono registrare nuove gare podistiche con nome e luogo
- **Valutazione Dettagliata:** Lasciare recensioni complete su tre categorie principali:
  - **Percorso:** Segnaletica, qualità del fondo, correttezza della distanza dichiarata
  - **Ristori:** Numero, varietà, disponibilità di ristori abusivi, qualità del ristoro finale
  - **Organizzazione:** Valutazione generale dell'organizzazione della gara
- **Note Personali:** Aggiungi commenti e osservazioni dettagliate sulla tua esperienza
- **Filtro Dinamico:** Filtra le gare per nome, luogo o autore in tempo reale
- **Visualizzazione Voti:** Vedi la valutazione media e il numero di recensioni per ogni gara

### Sistema di Valutazione
- Scala 1-5 per ogni criterio di valutazione
- Calcolo automatico della media globale
- Indicatori visivi con emoji per facilità di lettura

## Come Iniziare

### Requisiti
- Python 3.8+
- pip (gestore pacchetti Python)

### Installazione Locale

1. **Clona il repository**
   ```bash
   git clone <repository-url>
   cd 4_corse_podistiche
   ```

2. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

3. **Avvia l'applicazione**
   ```bash
   python run.py
   ```

4. **Accedi all'applicazione**
   Apri il browser e vai a `http://localhost:5000`

## Struttura del Progetto

```
4_corse_podistiche/
├── app/
│   ├── models/           # Modelli del database (User, Race, Review)
│   ├── routes/           # Rotte principali dell'applicazione
│   ├── static/           # File statici (CSS, JavaScript)
│   │   ├── css/
│   │   └── js/
│   ├── templates/        # Template HTML
│   └── config.py         # Configurazione dell'app
├── database/             # Schema del database
├── tests/                # Test automatizzati
├── run.py                # Punto di ingresso dell'applicazione
└── requirements.txt      # Dipendenze Python
```

## Tecnologie Utilizzate

- **Backend:** Flask (Python)
- **Database:** SQLite / SQL
- **Frontend:** HTML5, CSS3, JavaScript
- **Hosting:** PythonAnywhere

## Note di Utilizzo

- Crea un account per poter lasciare recensioni
- Ogni gara calcolerà automaticamente la valutazione media basata su tutte le recensioni ricevute
- I tooltips info accanto a ogni campo ti aiuteranno a capire cosa valutare
- Puoi sempre modificare il tuo profilo e consultare le tue recensioni passate

---

© 2026 Corse Podistiche
