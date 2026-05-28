
import sqlite3

# constants, so no magic numbers por repetitive code
DATABASE = "contact.db"
MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 10
LINE_WIDTH = 75
MENU_EXIT_OPTION = "6"

# resuable database connect fucntion, so conveneint
def connect_database():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    return db, cursor

# reusable heading function to avoid repeated code, so convenient
def print_heading():
    print("ID | Name                 | Phone Number | Address")
    print("-" * LINE_WIDTH)


# ================= VIEW CONTACTS =================
# function to print all contacts and addresses, adn join tables
def print_people_address():

    db, cursor = connect_database()

    sql = ("""
    SELECT person.id,
           person.first_name,
           person.last_name,
           person.phone_number,
           address.number,
           address.street,
           address.suburb
    FROM person
    JOIN address ON person.id = address.address_id
    ORDER BY person.last_name ASC;
    """)

    cursor.execute(sql)
    results = cursor.fetchall()

    print("\n--- ALL CONTACTS ---")

    print_heading()

    for person_id, first_name, last_name, phone_number, number, street, suburb in results:

# clear formatting
#colon(:) separates variable name from formatting rule
# < pushes data to left, with empty spaces on the right
# intger following < symbol is how many spaces the variable is allowed
        print(f"{person_id:<3} | "
              f"{first_name} {last_name:<18} | "
              f"{phone_number:<12} | "
              f"{number} {street}, {suburb}")

    db.close()



# ================= SEARCH FUNCTION =================
# function to search for a person
def search_for_person():

# .strip() removes accidental spaces
    name = input("Enter first or last name: ").strip()

# Invalid input handling
    if name == "":
        print("Error: You must enter a name.")
        return

#Uses constant instead of magic number
    elif len(name) < MIN_NAME_LENGTH:
        print(f"Error: Name must be at least {MIN_NAME_LENGTH} characters.")
        return

    db, cursor = connect_database()

    cursor.execute('''
    SELECT person.id,
           person.first_name,
           person.last_name,
           person.phone_number,
           address.number,
           address.street,
           address.suburb
    FROM person
    JOIN address ON person.id = address.address_id
    WHERE person.first_name LIKE ?
       OR person.last_name LIKE ?
    ''', (f"%{name}%", f"%{name}%"))

    results = cursor.fetchall()

    print("\n--- SEARCH RESULTS ---")

    if not results:
        print("That person was not found.")
        db.close()
        return

    print_heading()

    for row in results:

    # clean formatting
        print(f"{row[0]:<3} | "
              f"{row[1]} {row[2]:<18} | "
              f"{row[3]:<12} | "
              f"{row[4]} {row[5]}, {row[6]}")

    db.close()

# ================= UPDATE PHONE =================
# function to update a phone number
def update_phone():

# code accepts all input, handles invalid inputs and unexpected user inputs
    try:
        contact_id = int(input("Enter contact ID to update: "))

    except ValueError:
        print("Error: ID must be a number.")
        return

    new_phone = input("Enter a new phone number: ").strip()


    if new_phone == "":
        print("Error: Phone number cannot be blank.")
        return

    db, cursor = connect_database()

    cursor.execute('''
    UPDATE person
    SET phone_number = ?
    WHERE id = ?
    ''', (new_phone, contact_id))

# checks if ID exists
    if cursor.rowcount == 0:
        print("Error: Contact ID not found.")

    else:
        db.commit()
        print("Phone number updated.")

    db.close()

# ================= SORT CONTACTS =================
# function to sort contact information from A-Z
def sort_contact():

    db, cursor = connect_database()

    cursor.execute('''
    SELECT person.id,
           person.first_name,
           person.last_name,
           person.phone_number,
           address.number,
           address.street,
           address.suburb
    FROM person
    JOIN address ON person.id = address.address_id
    ORDER BY person.last_name ASC,
             person.first_name ASC
    ''')

    results = cursor.fetchall()

    print("\n--- SORTED CONTACTS (A-Z) ---")

# call function for headings
    print_heading()

    for row in results:

 # clear formatting
        print(f"{row[0]:<3} | "
              f"{row[1]} {row[2]:<18} | "
              f"{row[3]:<12} | "
              f"{row[4]} {row[5]}, {row[6]} {row[7]}")

    db.close()


# ================= FILTER BY SUBURB =================
# function to filter contacts by suburb
def filter_by_suburb():

    suburb = input("Enter suburb: ").strip()

# Invalid input handling
    if suburb == "":
        print("Error: Suburb cannot be blank.")
        return

    db, cursor = connect_database()

    cursor.execute('''
    SELECT person.id,
           person.first_name,
           person.last_name,
           person.phone_number,
           address.number,
           address.street,
           address.suburb
    FROM person
    JOIN address ON person.id = address.address_id
    WHERE address.suburb LIKE ?
    ORDER BY person.last_name ASC
    ''', (f"%{suburb}%",))

    results = cursor.fetchall()

    print("\n--- FILTER RESULTS ---")

    # checks if no results found
    if not results:
        print("No contacts found in that suburb.")
        db.close()
        return

    # reusable headings
    print_heading()

    for row in results:

        # cleaner formatting
        print(f"{row[0]:<3} | "
              f"{row[1]} {row[2]:<18} | "
              f"{row[3]:<12} | "
              f"{row[4]} {row[5]}, {row[6]}")

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
        elif choice == MENU_EXIT_OPTION:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

menu()
