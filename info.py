
import sqlite3

DATABASE = 'contact.db'


# function to print all contacts
def print_people_address():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = """
    SELECT person.id, person.first_name, person.last_name,
    address.number, address.street, address.suburb
    FROM person
    JOIN address ON person.id = address.address_id;
    """

    cursor.execute(sql)
    results = cursor.fetchall()

    for id, first_name, last_name, address_id, number, street, suburb in results:
        print(f"{id} {first_name}, {last_name}, {address_id}, {number}, {street}, {suburb}")

    db.close()


print_people_address()
