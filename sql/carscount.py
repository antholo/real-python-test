import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute(""" SELECT Inventory.make, Inventory.model, Inventory.quantity, 
                    (SELECT count(*)
                        FROM orders
                        WHERE make=Inventory.make AND model=Inventory.model)
                    FROM Inventory
                    GROUP BY make, model
                """)
    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print r[2]
        print r[3]