import sqlite3

DATABASE = 'contact.db'


def(print_all_contact)
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'select * from contact;'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close
