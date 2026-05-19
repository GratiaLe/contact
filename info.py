
import sqlite3

DATABASE = 'contact.db'


# function to print all contacts, and join the person adn address tables
def print_people_address():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    sql = """
    SELECT person.id, person.first_name, person.last_name, phone_number,
    address.number, address.street, address.suburb
    FROM person
    JOIN address ON person.id = address.address_id;
    """

    cursor.execute(sql)
    results = cursor.fetchall()

    print(results)

    for first_name, last_name, phone_number, address_id, number, street, suburb in results:
        print(f"{first_name} {last_name}, {phone_number} {address_id}, {number} {street}, {suburb}")

    db.close()


print_people_address()

# function to print all contacts
def search_for_person():
    name = input("Enter first or last name: ")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
    SELECT person.first_name, person.last_name, person.phone_number,
           address.number, address.street, address.suburb
    FROM person
    JOIN address ON person.id = address.address_id
    WHERE person.first_name LIKE ? OR person.last_name LIKE ?
    ''', (f"%{name}%", f"%{name}%"))

search_for_person()
