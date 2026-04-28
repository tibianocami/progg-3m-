# FUNZIONE BASE: controllo input vuoto
def input_non_vuoto(valore):
    return valore.strip() != ""


# INPUT INTERO CON RANGE
def input_intero_range(messaggio, minimo, massimo):
    while True:
        try:
            valore = input(messaggio)

            if not input_non_vuoto(valore):
                print("Errore: input vuoto!")
                continue

            valore = int(valore)

            if minimo <= valore <= massimo:
                return valore

            print(f"Inserisci un numero tra {minimo} e {massimo}")

        except ValueError:
            print("Errore: inserisci un numero intero valido!")


# INPUT INTERO MINIMO
def input_intero_min(messaggio, minimo):
    while True:
        try:
            valore = input(messaggio)

            if not input_non_vuoto(valore):
                print("Errore: input vuoto!")
                continue

            valore = int(valore)

            if valore >= minimo:
                return valore

            print(f"Inserisci un numero maggiore o uguale a {minimo}")

        except ValueError:
            print("Errore: inserisci un numero intero valido!")


# INPUT NUMERO (FLOAT)
def input_numero(messaggio):
    while True:
        try:
            valore = input(messaggio)

            if not input_non_vuoto(valore):
                print("Errore: input vuoto!")
                continue

            return float(valore)

        except ValueError:
            print("Errore: inserisci un numero valido!")


# INPUT TESTO (SOLO LETTERE)
def input_testo(messaggio):
    while True:
        valore = input(messaggio)

        if not input_non_vuoto(valore):
            print("Errore: input vuoto!")
            continue

        valore = valore.strip()

        if valore.isalpha():
            return valore

        print("Errore: inserisci solo lettere (no numeri o simboli)!")


# INPUT SOLO LETTERE (più generico)
def input_solo_lettere(messaggio):
    while True:
        valore = input(messaggio)

        if not input_non_vuoto(valore):
            print("Errore: input vuoto!")
            continue

        valore = valore.strip()

        if valore.isalpha():
            return valore

        print("Errore: inserisci solo lettere!")


# INPUT IN LISTA
def input_in_lista(messaggio, lista_valori):
    while True:
        valore = input(messaggio)

        if not input_non_vuoto(valore):
            print("Errore: input vuoto!")
            continue

        valore = valore.strip()

        if valore in lista_valori:
            return valore

        print(f"Errore: scegli tra {', '.join(lista_valori)}")