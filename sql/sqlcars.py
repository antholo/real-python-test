import sqlite3

connection = sqlite3.connect("cars.db")

c = connection.cursor()

c.execute("""CREATE TABLE Inventory
            (Make TEXT, Model TEXT, Quantity INT)
            """)

connection.close()