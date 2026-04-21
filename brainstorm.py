#main ------------------------------------------------------
#from gantt import crea_gantt
#from preventivo import crea_preventivo

def menu():
    while True:
        print("\n=== Gantt & Preventivi Generator ===")
        print("1. Crea Gantt")
        print("2. Crea Preventivo")
        print("3. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            crea_gantt()
        elif scelta == "2":
            crea_preventivo()
        elif scelta == "3":
            print("Uscita...")
            break
        else:
            print("Scelta non valida!")

if __name__ == "__main__":
    menu()


#gantt ------------------------------------------------------

#import matplotlib.pyplot as plt

def crea_gantt():
    attivita = []
    start = []
    durata = []

    print("\n--- Creazione Gantt ---")

    n = int(input("Quante attività vuoi inserire? "))

    for i in range(n):
        nome = input(f"Nome attività {i+1}: ")
        s = int(input("Giorno inizio (numero): "))
        d = int(input("Durata (giorni): "))

        attivita.append(nome)
        start.append(s)
        durata.append(d)

    fig, ax = plt.subplots()

    ax.barh(attivita, durata, left=start)

    ax.set_xlabel("Giorni")
    ax.set_title("Diagramma di Gantt")

    plt.tight_layout()
    plt.savefig("gantt.png")

    print("✅ Gantt salvato come gantt.png")

#preventivo ------------------------------------------------------

#from PIL import Image, ImageDraw, ImageFont

def crea_preventivo():
    print("\n--- Creazione Preventivo ---")

    cliente = input("Nome cliente: ")
    n = int(input("Quanti servizi vuoi inserire? "))

    servizi = []
    totale = 0

    for i in range(n):
        nome = input(f"Servizio {i+1}: ")
        prezzo = float(input("Prezzo: "))
        servizi.append((nome, prezzo))
        totale += prezzo

    # crea immagine
    img = Image.new('RGB', (600, 400), color='white')
    draw = ImageDraw.Draw(img)

    y = 20
    draw.text((20, y), f"Preventivo per: {cliente}", fill='black')
    y += 40

    for nome, prezzo in servizi:
        draw.text((20, y), f"{nome} - €{prezzo}", fill='black')
        y += 30

    y += 20
    draw.text((20, y), f"Totale: €{totale}", fill='black')

    img.save("preventivo.png")

    print("✅ Preventivo salvato come preventivo.png")


    # tools.py ------------------------------------------------------

    def input_intero(messaggio):
     while True:
        try:
            return int(input(messaggio))
        except:
            print("Inserisci un numero valido!")