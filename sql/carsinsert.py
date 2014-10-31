import sqlite3

vehicles = [
            ('Ford', 'Taurus', 5),
            ('Ford', 'Focus', 3),
            ('Honda', 'Civic', 12),
            ('Honda', 'Accord', 8),
            ('Ford', '500', 7)
            ]

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.executemany("INSERT INTO Inventory VALUES(?, ?, ?)", vehicles)