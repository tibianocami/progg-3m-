import tkinter as tk
from tkinter import messagebox


# -------------------------
# FUNZIONI LOGICHE
# -------------------------

def crea_gantt():
    try:
        n = int(entry_n_gantt.get())

        if n <= 0:
            messagebox.showerror("Errore", "Numero attività non valido")
            return

        output.delete("1.0", tk.END)
        output.insert(tk.END, "=== GANTT ===\n\n")

        for i in range(n):
            nome = f"Attività {i+1}"
            start = i * 2
            durata = 3

            barra = "█" * durata
            output.insert(tk.END, f"{nome:12} | {barra} ({start}-{start+durata})\n")

    except:
        messagebox.showerror("Errore", "Inserisci un numero valido")


def crea_preventivo():
    try:
        cliente = entry_cliente.get()
        n = int(entry_n_servizi.get())

        if cliente.strip() == "":
            messagebox.showerror("Errore", "Cliente vuoto")
            return

        totale = 0

        output.delete("1.0", tk.END)
        output.insert(tk.END, f"=== PREVENTIVO ===\nCliente: {cliente}\n\n")

        for i in range(n):
            nome = f"Servizio {i+1}"
            prezzo = 10 * (i + 1)

            totale += prezzo

            output.insert(tk.END, f"{nome} - €{prezzo}\n")

        output.insert(tk.END, f"\nTOTALE: €{totale}\n")

    except:
        messagebox.showerror("Errore", "Input non valido")


def pulisci():
    output.delete("1.0", tk.END)


# -------------------------
# GUI
# -------------------------

root = tk.Tk()
root.title("Gantt & Preventivi")
root.geometry("600x500")


# TITOLO
title = tk.Label(root, text="GESTIONE PROGETTO", font=("Arial", 16))
title.pack(pady=10)


# -------------------------
# GANTT
# -------------------------

frame_gantt = tk.Frame(root)
frame_gantt.pack(pady=5)

tk.Label(frame_gantt, text="Numero attività Gantt:").grid(row=0, column=0)
entry_n_gantt = tk.Entry(frame_gantt)
entry_n_gantt.grid(row=0, column=1)

tk.Button(frame_gantt, text="Crea Gantt", command=crea_gantt).grid(row=0, column=2)


# -------------------------
# PREVENTIVO
# -------------------------

frame_prev = tk.Frame(root)
frame_prev.pack(pady=10)

tk.Label(frame_prev, text="Cliente:").grid(row=0, column=0)
entry_cliente = tk.Entry(frame_prev)
entry_cliente.grid(row=0, column=1)

tk.Label(frame_prev, text="N° servizi:").grid(row=1, column=0)
entry_n_servizi = tk.Entry(frame_prev)
entry_n_servizi.grid(row=1, column=1)

tk.Button(frame_prev, text="Crea Preventivo", command=crea_preventivo).grid(row=2, column=1)


# -------------------------
# OUTPUT
# -------------------------

output = tk.Text(root, height=15, width=70)
output.pack(pady=10)


# -------------------------
# BOTTONI EXTRA
# -------------------------

tk.Button(root, text="Pulisci", command=pulisci).pack()
tk.Button(root, text="Esci", command=root.destroy).pack(pady=5)


# AVVIO
root.mainloop()