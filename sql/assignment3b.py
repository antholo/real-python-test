import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    choice = int(raw_imput("""Please select a function:
        1. Average
        2. Maximum
        3. Minimum
        4. Sum
        5. Quit"""))

    while choice < 1 OR choice > 5:
        choice = int(raw_imput("Invalid selection. Please select 1-5"))

    while choice < 5:
        action = {1: "avg", 2: "max", 3: "min", 4: "sum"}[choice]

        result = c.execute("SELECT " + action + "(num) FROM numbers")
        print(action + " = " + result)
        choice = int(raw_input("Please select another action")
        