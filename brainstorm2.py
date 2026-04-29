import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class PreventivoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generatore Preventivi PRO")
        self.root.geometry("1100x700")

        self.items = []

        self.build_ui()

    # ================= UI =================
    def build_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Preventivo")

        # ===== CLIENTE =====
        box = ttk.LabelFrame(frame, text="Cliente")
        box.pack(fill="x", padx=10, pady=5)

        self.nome = tk.StringVar()
        self.indirizzo = tk.StringVar()

        ttk.Label(box, text="Nome").grid(row=0, column=0)
        ttk.Entry(box, textvariable=self.nome, width=40).grid(row=0, column=1)

        ttk.Label(box, text="Indirizzo").grid(row=1, column=0)
        ttk.Entry(box, textvariable=self.indirizzo, width=40).grid(row=1, column=1)

        # ===== INPUT =====
        input_box = ttk.LabelFrame(frame, text="Servizi")
        input_box.pack(fill="x", padx=10, pady=5)

        self.desc = tk.StringVar()
        self.qta = tk.DoubleVar(value=1)
        self.prezzo = tk.DoubleVar(value=0)

        ttk.Entry(input_box, textvariable=self.desc, width=40).grid(row=0, column=0)
        ttk.Entry(input_box, textvariable=self.qta, width=10).grid(row=0, column=1)
        ttk.Entry(input_box, textvariable=self.prezzo, width=10).grid(row=0, column=2)

        ttk.Button(input_box, text="Aggiungi", command=self.add_item).grid(row=0, column=3)
        ttk.Button(input_box, text="Modifica selezionato", command=self.edit_item).grid(row=0, column=4)
        ttk.Button(input_box, text="Elimina selezionato", command=self.delete_item).grid(row=0, column=5)

        # ===== TABELLA =====
        table = ttk.LabelFrame(frame, text="Lista lavori")
        table.pack(fill="both", expand=True, padx=10, pady=5)

        cols = ("Desc", "Qta", "Prezzo", "Totale")
        self.tree = ttk.Treeview(table, columns=cols, show="headings")

        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="center")

        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        # ===== TOTALI =====
        bottom = ttk.Frame(frame)
        bottom.pack(fill="x", padx=10, pady=10)

        self.subtotale = tk.StringVar(value="0.00 €")
        self.iva = tk.StringVar(value="22")
        self.totale = tk.StringVar(value="0.00 €")

        ttk.Label(bottom, text="Subtotale").grid(row=0, column=0)
        ttk.Label(bottom, textvariable=self.subtotale).grid(row=0, column=1)

        ttk.Label(bottom, text="IVA %").grid(row=1, column=0)
        ttk.Entry(bottom, textvariable=self.iva, width=5).grid(row=1, column=1)

        ttk.Label(bottom, text="Totale").grid(row=2, column=0)
        ttk.Label(bottom, textvariable=self.totale).grid(row=2, column=1)

        ttk.Button(bottom, text="Calcola", command=self.calcola).grid(row=3, column=0)
        ttk.Button(bottom, text="Esporta PDF", command=self.export_pdf).grid(row=3, column=1)

        self.selected_index = None

    # ================= SELEZIONE =================
    def on_select(self, event):
        selected = self.tree.focus()
        if not selected:
            return

        values = self.tree.item(selected, "values")

        self.desc.set(values[0])
        self.qta.set(values[1])
        self.prezzo.set(values[2])

        self.selected_index = self.tree.index(selected)

    # ================= ADD =================
    def add_item(self):
        d = self.desc.get()
        q = float(self.qta.get())
        p = float(self.prezzo.get())

        tot = q * p

        self.items.append([d, q, p, tot])
        self.tree.insert("", "end", values=(d, q, p, tot))

        self.calcola()

    # ================= EDIT =================
    def edit_item(self):
        if self.selected_index is None:
            messagebox.showwarning("Attenzione", "Seleziona una riga")
            return

        d = self.desc.get()
        q = float(self.qta.get())
        p = float(self.prezzo.get())

        tot = q * p

        self.items[self.selected_index] = [d, q, p, tot]

        self.refresh_tree()
        self.calcola()

    # ================= DELETE =================
    def delete_item(self):
        selected = self.tree.focus()
        if not selected:
            return

        index = self.tree.index(selected)

        del self.items[index]
        self.tree.delete(selected)

        self.selected_index = None
        self.calcola()

    # ================= REFRESH =================
    def refresh_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for item in self.items:
            self.tree.insert("", "end", values=item)

    # ================= CALCOLA =================
    def calcola(self):
        subtotal = sum(i[3] for i in self.items)
        iva = float(self.iva.get())

        tot = subtotal + (subtotal * iva / 100)

        self.subtotale.set(f"{subtotal:.2f} €")
        self.totale.set(f"{tot:.2f} €")

    # ================= PDF =================
    def export_pdf(self):
        file = filedialog.asksaveasfilename(defaultextension=".pdf")
        if not file:
            return

        c = canvas.Canvas(file, pagesize=A4)
        w, h = A4

        c.setFont("Helvetica-Bold", 20)
        c.drawString(50, h - 60, "PREVENTIVO")

        c.setFont("Helvetica", 10)
        c.drawString(50, h - 120, f"Cliente: {self.nome.get()}")
        c.drawString(50, h - 135, f"Indirizzo: {self.indirizzo.get()}")

        y = h - 180

        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "Descrizione")
        c.drawString(300, y, "Qta")
        c.drawString(350, y, "Prezzo")
        c.drawString(450, y, "Totale")

        y -= 20
        c.setFont("Helvetica", 10)

        subtotal = 0

        for i in self.items:
            d, q, p, t = i
            subtotal += t

            c.drawString(50, y, str(d))
            c.drawString(300, y, str(q))
            c.drawString(350, y, f"{p:.2f}")
            c.drawString(450, y, f"{t:.2f}")

            y -= 15

        iva = float(self.iva.get())
        iva_val = subtotal * iva / 100
        totale = subtotal + iva_val

        y -= 20
        c.setFont("Helvetica-Bold", 11)
        c.drawString(350, y, f"Totale: {totale:.2f} €")

        c.save()

        messagebox.showinfo("OK", "PDF creato!")


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = PreventivoApp(root)
    root.mainloop()