
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

    for first_name, last_name, phone_number, address_id, number, street, suburb in results:
        print(f"{first_name} {last_name}, {phone_number} {address_id}, {number} {street}, {suburb}")

    db.close()


print_people_address()

# function to print all contacts
def search_for_person():
# ask user for person's foirst or last name
    name = input("Enter first or last name: ").strip()
# accepts error values
    if name == "":
        print("Error: You must enter a name.")
        return
# Amy is the shortest name in the person table (3 letters)
    elif len(name) < 3:
        print("Error: Name must be at least 2 characters.")
        return
    
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
    SELECT person.first_name, person.last_name, person.phone_number,
           address.number, address.street, address.suburb
    FROM person
    JOIN address ON person.id = address.address_id
    WHERE person.first_name LIKE ? OR person.last_name LIKE ?
    ''', (f"%{name}%", f"%{name}%"))

    results = cursor.fetchall()
    print("\n---SEARCH RESULTS---")

    if not results:
        print("That person was not found.")
        db.close()
        return

    for row in results:
        print(f"{row[0]}{row[1]}       {row[2]} {row[3]}, {row[4]} {row[5]}")

    db.close()

search_for_person()
