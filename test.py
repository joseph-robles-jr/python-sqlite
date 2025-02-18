import sqlite3

'''How to create and update a table in SQLite'''

# Connect to an SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()


sqliteConnection = sqlite3.connect('sql.db')
cursor = sqliteConnection.cursor()

query = "SQL query;"
cursor.execute(query)
result = cursor.fetchall()
print('SQLite Version is {}'.format(result))



