
print_all_contact()


import sqlite3

DATABASE = 'contact.db'

# function to print all contacts
def print_all_contact():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = 'SELECT * FROM contact;'
    cursor.execute(sql)
    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()

print_all_contact()
