# INSERT Command

import sqlite3

# create the connection object
connection = sqlite3.connect("new.db")

#cursor for executing SQL commands
cursor = connection.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8200000)")
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)")

    # commit the changes
    connection.commit()
except sqlite3.OperationalError as e:
    print "Oops! Let's see what the error says: ", e
# close the database connection
connection.close()