# =========================================================
# POLYMARKET STYLE APP - PYTHON + TKINTER
# =========================================================
# FEATURES:
# - Login/Register
# - Virtual balance
# - Prediction markets
# - Buy YES / NO shares
# - Market prices
# - Portfolio
# - Transaction history
# - SQLite database
# - Modern GUI with ttkbootstrap
#
# INSTALL:
# pip install ttkbootstrap
# =========================================================

import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import sqlite3
from datetime import datetime
import random

# =========================================================
# DATABASE
# =========================================================

conn = sqlite3.connect("polymarket.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT,
    balance REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS markets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    yes_price REAL,
    no_price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolio(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    market_id INTEGER,
    side TEXT,
    shares INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    action TEXT,
    amount REAL,
    date TEXT
)
""")

conn.commit()

# =========================================================
# CREATE SAMPLE MARKETS
# =========================================================

cursor.execute("SELECT COUNT(*) FROM markets")
count = cursor.fetchone()[0]

if count == 0:

    sample_markets = [
        ("Bitcoin above $100k in 2026?", 0.65, 0.35),
        ("Italy wins World Cup 2026?", 0.20, 0.80),
        ("GTA 6 delayed again?", 0.55, 0.45),
        ("AI replaces programmers before 2035?", 0.70, 0.30),
        ("Tesla stock doubles this year?", 0.25, 0.75)
    ]

    for market in sample_markets:
        cursor.execute("""
        INSERT INTO markets(question, yes_price, no_price)
        VALUES (?, ?, ?)
        """, market)

conn.commit()

# =========================================================
# APP
# =========================================================

class PolyMarketApp:

    def __init__(self, root):

        self.root = root
        self.root.title("PolyMarket Clone")
        self.root.geometry("1200x700")

        self.current_user = None

        self.login_screen()

    # =====================================================
    # CLEAR
    # =====================================================

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # =====================================================
    # LOGIN SCREEN
    # =====================================================

    def login_screen(self):

        self.clear()

        frame = tb.Frame(self.root, padding=50)
        frame.pack(expand=True)

        tb.Label(
            frame,
            text="📈 POLYMARKET",
            font=("Arial", 34, "bold")
        ).pack(pady=20)

        tb.Label(frame, text="Username").pack(anchor="w")

        self.username_entry = tb.Entry(frame, width=30)
        self.username_entry.pack(pady=10)

        tb.Label(frame, text="Password").pack(anchor="w")

        self.password_entry = tb.Entry(frame, width=30, show="*")
        self.password_entry.pack(pady=10)

        tb.Button(
            frame,
            text="Login",
            bootstyle="success",
            width=20,
            command=self.login
        ).pack(pady=10)

        tb.Button(
            frame,
            text="Register",
            bootstyle="info",
            width=20,
            command=self.register
        ).pack()

    # =====================================================
    # REGISTER
    # =====================================================

    def register(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Fill all fields")
            return

        try:

            cursor.execute("""
            INSERT INTO users VALUES (?, ?, ?)
            """, (username, password, 1000))

            conn.commit()

            messagebox.showinfo(
                "Success",
                "Account created with $1000 virtual balance"
            )

        except:
            messagebox.showerror(
                "Error",
                "Username already exists"
            )

    # =====================================================
    # LOGIN
    # =====================================================

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute("""
        SELECT * FROM users
        WHERE username=? AND password=?
        """, (username, password))

        user = cursor.fetchone()

        if user:
            self.current_user = username
            self.dashboard()

        else:
            messagebox.showerror(
                "Error",
                "Invalid credentials"
            )

    # =====================================================
    # DASHBOARD
    # =====================================================

    def dashboard(self):

        self.clear()

        # TOP BAR
        top = tb.Frame(self.root)
        top.pack(fill="x", pady=10)

        tb.Label(
            top,
            text=f"👤 {self.current_user}",
            font=("Arial", 22, "bold")
        ).pack(side="left", padx=20)

        cursor.execute("""
        SELECT balance FROM users
        WHERE username=?
        """, (self.current_user,))

        balance = cursor.fetchone()[0]

        tb.Label(
            top,
            text=f"💰 ${balance:.2f}",
            font=("Arial", 22)
        ).pack(side="right", padx=20)

        # TITLE
        tb.Label(
            self.root,
            text="Prediction Markets",
            font=("Arial", 28, "bold")
        ).pack(pady=20)

        # MARKET FRAME
        market_frame = tb.Frame(self.root)
        market_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(market_frame, bg="#222222")
        scrollbar = tb.Scrollbar(
            market_frame,
            orient="vertical",
            command=canvas.yview
        )

        scroll_frame = tb.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # LOAD MARKETS
        cursor.execute("SELECT * FROM markets")
        markets = cursor.fetchall()

        for market in markets:

            market_id = market[0]
            question = market[1]
            yes_price = market[2]
            no_price = market[3]

            card = tb.Frame(
                scroll_frame,
                bootstyle="dark",
                padding=20
            )

            card.pack(fill="x", padx=20, pady=10)

            tb.Label(
                card,
                text=question,
                font=("Arial", 18, "bold")
            ).pack(anchor="w", pady=10)

            prices = tb.Frame(card)
            prices.pack(fill="x")

            tb.Label(
                prices,
                text=f"YES: ${yes_price:.2f}",
                foreground="lime",
                font=("Arial", 14)
            ).pack(side="left", padx=10)

            tb.Label(
                prices,
                text=f"NO: ${no_price:.2f}",
                foreground="red",
                font=("Arial", 14)
            ).pack(side="left", padx=10)

            buttons = tb.Frame(card)
            buttons.pack(pady=10)

            tb.Button(
                buttons,
                text="Buy YES",
                bootstyle="success",
                command=lambda m=market_id: self.buy_popup(m, "YES")
            ).pack(side="left", padx=10)

            tb.Button(
                buttons,
                text="Buy NO",
                bootstyle="danger",
                command=lambda m=market_id: self.buy_popup(m, "NO")
            ).pack(side="left", padx=10)

        # PORTFOLIO BUTTON
        tb.Button(
            self.root,
            text="📊 Portfolio",
            bootstyle="info",
            command=self.portfolio_screen
        ).pack(pady=20)

    # =====================================================
    # BUY POPUP
    # =====================================================

    def buy_popup(self, market_id, side):

        popup = tb.Toplevel(self.root)
        popup.title("Buy Shares")
        popup.geometry("350x250")

        tb.Label(
            popup,
            text=f"Buy {side} Shares",
            font=("Arial", 20)
        ).pack(pady=20)

        tb.Label(
            popup,
            text="Number of shares"
        ).pack()

        shares_entry = tb.Entry(popup)
        shares_entry.pack(pady=10)

        def confirm():

            try:

                shares = int(shares_entry.get())

                if shares <= 0:
                    raise ValueError

                cursor.execute("""
                SELECT yes_price, no_price
                FROM markets
                WHERE id=?
                """, (market_id,))

                prices = cursor.fetchone()

                price = prices[0] if side == "YES" else prices[1]

                total = price * shares

                cursor.execute("""
                SELECT balance FROM users
                WHERE username=?
                """, (self.current_user,))

                balance = cursor.fetchone()[0]

                if total > balance:
                    messagebox.showerror(
                        "Error",
                        "Not enough balance"
                    )
                    return

                # UPDATE BALANCE
                cursor.execute("""
                UPDATE users
                SET balance = balance - ?
                WHERE username=?
                """, (total, self.current_user))

                # SAVE PORTFOLIO
                cursor.execute("""
                INSERT INTO portfolio(
                    username,
                    market_id,
                    side,
                    shares
                )
                VALUES (?, ?, ?, ?)
                """, (
                    self.current_user,
                    market_id,
                    side,
                    shares
                ))

                # TRANSACTION
                date = datetime.now().strftime("%d/%m/%Y %H:%M")

                cursor.execute("""
                INSERT INTO transactions(
                    username,
                    action,
                    amount,
                    date
                )
                VALUES (?, ?, ?, ?)
                """, (
                    self.current_user,
                    f"Buy {side}",
                    total,
                    date
                ))

                conn.commit()

                popup.destroy()

                self.randomize_prices()

                self.dashboard()

                messagebox.showinfo(
                    "Success",
                    f"Bought {shares} shares"
                )

            except:
                messagebox.showerror(
                    "Error",
                    "Invalid value"
                )

        tb.Button(
            popup,
            text="Confirm",
            bootstyle="success",
            command=confirm
        ).pack(pady=20)

    # =====================================================
    # RANDOM MARKET MOVEMENT
    # =====================================================

    def randomize_prices(self):

        cursor.execute("SELECT * FROM markets")
        markets = cursor.fetchall()

        for market in markets:

            market_id = market[0]

            new_yes = round(random.uniform(0.05, 0.95), 2)
            new_no = round(1 - new_yes, 2)

            cursor.execute("""
            UPDATE markets
            SET yes_price=?, no_price=?
            WHERE id=?
            """, (new_yes, new_no, market_id))

        conn.commit()

    # =====================================================
    # PORTFOLIO
    # =====================================================

    def portfolio_screen(self):

        portfolio = tb.Toplevel(self.root)
        portfolio.title("Portfolio")
        portfolio.geometry("800x500")

        tb.Label(
            portfolio,
            text="📊 Your Portfolio",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        columns = (
            "Question",
            "Side",
            "Shares"
        )

        tree = tb.Treeview(
            portfolio,
            columns=columns,
            show="headings",
            height=15
        )

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=220)

        tree.pack(fill="both", expand=True, padx=20, pady=20)

        cursor.execute("""
        SELECT
            markets.question,
            portfolio.side,
            portfolio.shares
        FROM portfolio
        JOIN markets
        ON portfolio.market_id = markets.id
        WHERE portfolio.username=?
        """, (self.current_user,))

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("", "end", values=row)


# =========================================================
# START
# =========================================================

root = tb.Window(themename="cyborg")
app = PolyMarketApp(root)
root.mainloop()