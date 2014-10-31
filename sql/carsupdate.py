import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("UPDATE Inventory SET quantity=2 WHERE model='civic'")
    c.execute("UPDATE Inventory SET quantity=5 WHERE model='500'")

    c.execute("SELECT * FROM Inventory")

    rows = c.fetchall()

    for r in rows:
        print "Make: ", r[0], "Model: ", r[1], "Quantity: ", r[2]