import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("SELECT * FROM Inventory WHERE make='Ford'")

    rows = c.fetchall()

    for r in rows:
        print "Make: ", r[0], "Model: ", r[1], "Quantity: ", r[2] 