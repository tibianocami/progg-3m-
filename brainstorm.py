import tkinter as tk
from tkinter import messagebox


# -----------------------------
# TEMA
# -----------------------------

theme = {
    "bg": "white",
    "fg": "black",
    "btn": "#e0e0e0"
}


def apply_theme(widget):
    try:
        widget.configure(bg=theme["bg"], fg=theme["fg"])
    except:
        pass


def set_dark():
    theme["bg"] = "#1e1e1e"
    theme["fg"] = "white"
    theme["btn"] = "#333333"
    refresh()


def set_light():
    theme["bg"] = "white"
    theme["fg"] = "black"
    theme["btn"] = "#e0e0e0"
    refresh()


# -----------------------------
# PULIZIA SCHERMO
# -----------------------------

def clear():
    for w in root.winfo_children():
        if w not in (menu_btn, output):
            w.destroy()


# -----------------------------
# HOME
# -----------------------------

def home():
    clear()

    tk.Label(root, text="GESTIONE GANTT & PREVENTIVI",
             bg=theme["bg"], fg=theme["fg"],
             font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="GANTT",
              bg=theme["btn"], fg=theme["fg"],
              width=20, command=gantt_page).pack(pady=10)

    tk.Button(root, text="PREVENTIVI",
              bg=theme["btn"], fg=theme["fg"],
              width=20, command=preventivi_page).pack(pady=10)


# -----------------------------
# GANTT
# -----------------------------

def gantt_page():
    clear()

    tk.Label(root, text="GANTT",
             bg=theme["bg"], fg=theme["fg"],
             font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Numero attività:",
             bg=theme["bg"], fg=theme["fg"]).pack()

    entry = tk.Entry(root)
    entry.pack()

    def genera():
        try:
            n = int(entry.get())
            output.delete("1.0", tk.END)

            output.insert(tk.END, "=== GANTT ===\n\n")

            for i in range(n):
                bar = "█" * (i + 2)
                output.insert(tk.END, f"Task {i+1}: {bar}\n")

        except:
            messagebox.showerror("Errore", "Numero non valido")

    tk.Button(root, text="Genera",
              bg=theme["btn"], fg=theme["fg"],
              command=genera).pack(pady=5)

    tk.Button(root, text="Indietro",
              command=home).pack(pady=5)


# -----------------------------
# PREVENTIVI
# -----------------------------

def preventivi_page():
    clear()

    tk.Label(root, text="PREVENTIVI",
             bg=theme["bg"], fg=theme["fg"],
             font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Cliente:",
             bg=theme["bg"], fg=theme["fg"]).pack()

    cliente = tk.Entry(root)
    cliente.pack()

    tk.Label(root, text="Numero servizi:",
             bg=theme["bg"], fg=theme["fg"]).pack()

    nserv = tk.Entry(root)
    nserv.pack()

    def genera():
        try:
            n = int(nserv.get())
            output.delete("1.0", tk.END)

            totale = 0

            output.insert(tk.END, f"Cliente: {cliente.get()}\n\n")

            for i in range(n):
                prezzo = 10 * (i + 1)
                totale += prezzo
                output.insert(tk.END, f"Servizio {i+1} - €{prezzo}\n")

            output.insert(tk.END, f"\nTOTALE: €{totale}\n")

        except:
            messagebox.showerror("Errore", "Input non valido")

    tk.Button(root, text="Genera",
              bg=theme["btn"], fg=theme["fg"],
              command=genera).pack(pady=5)

    tk.Button(root, text="Indietro",
              command=home).pack(pady=5)


# -----------------------------
# INFO
# -----------------------------

def info_page():
    clear()

    text = """
APP GANTT & PREVENTIVI

Descrizione:
App per creare Gantt e preventivi in modo semplice.

Come si usa:
- scegli una funzione dalla home
- inserisci i dati
- genera il risultato

Contatti:
GitHub: github.com/tuoprogetto
Email: esempio@email.com
"""

    tk.Label(root, text="INFO",
             bg=theme["bg"], fg=theme["fg"],
             font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text=text,
             bg=theme["bg"], fg=theme["fg"],
             justify="left").pack()

    tk.Button(root, text="Indietro",
              command=home).pack(pady=10)


# -----------------------------
# MENU ☰
# -----------------------------

def open_menu():
    m = tk.Menu(root, tearoff=0)
    m.add_command(label="Dark Mode", command=set_dark)
    m.add_command(label="Light Mode", command=set_light)
    m.add_command(label="Info", command=info_page)

    try:
        m.tk_popup(550, 40)
    finally:
        m.grab_release()


# -----------------------------
# REFRESH
# -----------------------------

def refresh():
    home()


# -----------------------------
# GUI PRINCIPALE
# -----------------------------

root = tk.Tk()
root.title("Gantt & Preventivi")
root.geometry("600x500")


# MENU ☰
menu_btn = tk.Button(root, text="☰", command=open_menu)
menu_btn.place(x=560, y=10)


# OUTPUT
output = tk.Text(root, height=10)
output.pack(side="bottom", fill="x")


# START
home()
root.mainloop()