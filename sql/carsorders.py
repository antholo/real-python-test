import sqlite3

car_orders = [
        ('Ford', '500', '2014-10-31'),
        ('Ford', '500', '2014-05-01'),
        ('Ford', '500', '2013-12-24'),
        ('Ford', 'Focus', '2014-10-31'),
        ('Ford', 'Focus', '2014-06-01'),
        ('Ford', 'Focus', '2013-02-14'),
        ('Ford', 'Taurus', '2014-10-31'),
        ('Ford', 'Taurus', '2014-04-01'),
        ('Ford', 'Taurus', '2013-11-24'),
        ('Honda', 'Civic', '2014-10-31'),
        ('Honda', 'Civic', '2014-05-05'),
        ('Honda', 'Civic', '2013-12-01'),
        ('Honda', 'Accord', '2014-06-16'),
        ('Honda', 'Accord', '2014-04-17'),
        ('Honda', 'Accord', '2013-05-24'),
        ]

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    #c.execute("""CREATE TABLE orders
    #            (make TEXT, model TEXT, order_date DATE)
    #            """)

    #c.executemany("INSERT INTO orders VALUES(?, ?, ?)", car_orders)

    c.execute("""SELECT Inventory.make, Inventory.model, Inventory.quantity, orders.order_date
                FROM Inventory, orders
                WHERE Inventory.make = orders.make
                AND Inventory.model = orders.model
                ORDER by Inventory.make""")
    rows = c.fetchall()

    print "Make: ", rows[0][0], "Model: ", rows[0][1], "Quantity: ", rows[0][2]
    make = rows[0][0]
    model = rows[0][1]
    for r in rows:
        if r[0] == make and r[1] == model:
            print "    Ordered: ",  r[3]
        else:
            make = r[0]
            model = r[1]
            print "Make: ", r[0], "Model: ", r[1], "Quantity: ", r[2]
            print "    Ordered: ",  r[3]