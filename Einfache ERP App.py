import tkinter as tk
import sqlite3

class ERPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Einfache ERP App")

        # Verbindung zur Datenbank herstellen
        self.conn = sqlite3.connect('erp_app.db')
        self.cursor = self.conn.cursor()

        # Tabelle erstellen, falls nicht vorhanden
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                date TEXT,
                description TEXT,
                amount REAL
            )
        ''')
        self.conn.commit()

        # GUI-Elemente erstellen
        self.label = tk.Label(root, text="Beschreibung:")
        self.label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.amount_label = tk.Label(root, text="Betrag:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.add_transaction_button = tk.Button(root, text="Transaktion hinzufügen", command=self.add_transaction)
        self.add_transaction_button.pack()

    def add_transaction(self):
        description = self.description_entry.get()
        amount = float(self.amount_entry.get())

        # Hier fügen Sie die Transaktion in die Datenbank ein
        self.cursor.execute("INSERT INTO transactions (description, amount) VALUES (?, ?)", (description, amount))
        self.conn.commit()
        
        self.description_entry.delete(0, tk.END)  # Felder leeren nach dem Hinzufügen
        self.amount_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ERPApp(root)
    root.mainloop()
