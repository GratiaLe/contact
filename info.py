
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

# create variable for lowest amount of chararacters in first and last names in database/person table
lowest_name_character = 3

# function to print all contacts
def search_for_person():
# ask user for person's foirst or last name
    name = input("Enter first or last name: ").strip()
# accepts error values
    if name == "":
        print("Error: You must enter a name.")
        return
# Amy is the shortest name in the person table (3 letters)
    elif len(name) < lowest_name_character:
        print("Error: Name must be at least 3 characters.")
        return

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
    SELECT  person.id,
            person.first_name,
            person.last_name,
            person.phone_number,
            address.number,
            address.street,
            address.suburb
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

    # column headings
    print("ID  |      Name     | Phone Number | Address")  
    print("-" * 70)


    for row in results:
        print(f"{row[0]}   |   {row[1]} {row[2]}   |   {row[3]}    | {row[4]} {row[5]} {row[6]}")

    db.close()


# function to update phone number
def update_phone():
    contact_id = input("Enter contact ID to update. ").strip
    new_phone = input("Enter a new phone number. ").strip

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
    UPDATE person
    SET phone_number = ?
    WHERE id = ?
    ''', (new_phone, contact_id))

    db.commit
    db.close()

    print("Phone number updated.")

    update_phone()

# function to sort contact information from A-Z
def sort_contact():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
        SELECT  person.id,
            person.first_name,
            person.last_name,
            person.phone_number,
            address.address_id,
            address.number,
            address.street,
            address.suburb
        FROM person
        JOIN address ON person.id = address.address_id''')

    results = cursor.fetchall()

    print("\n ---SORTED CONTACTS (A-Z)---")

    # column headings
    print("ID  |      Name     | Phone Number | Address")  
    print("-" * 70)

    for row in results:
        print(f"{row[0]}   |   {row[1]} {row[2]}   |   {row[3]}    | {row[4]} {row[5]} {row[6]}")

    db.close()

# function to filter by suburb
def filter_by_suburb():
    suburb = input("Enter suburb: ")

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()

    cursor.execute('''
    SELECT  person.id,
            person.first_name,
            person.last_name,
            person.phone_number,
            address.number,
            address.street,
            address.suburb
    FROM person
    JOIN address ON person.id = address.address_id
    WHERE address.suburb LIKE ?''', (f"%{suburb}%",))

    results = cursor.fetchall()

    print("\n---FILTER RESULTS---")

    # column headings
    print("ID  |      Name     | Phone Number | Address")  
    print("-" * 70)

    for row in results:
        print(f"{row[0]}   |   {row[1]} {row[2]}   |   {row[3]}    | {row[4]} {row[5]} {row[6]}")

    db.close()


# function to define/create menu
def menu():
    while True:
        print("\n---CONTACT DATABASE MENU---")
        print("1. View all contacts")
        print("2. Search for person")
        print("3. Update phone number")
        print("4. Sort contacts A-Z")
        print("5. Filter by suburb")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_people_address()
        elif choice == "2":
            search_for_person()
        elif choice == "3":
            update_phone()
        elif choice == "4":
            sort_contact()
        elif choice == "5":
            filter_by_suburb()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

menu()