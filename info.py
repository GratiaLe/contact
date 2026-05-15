
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


def menu():
    while True:
        print("\n===== CONTACT DATABASE MENU =====")
        print("1. View all contacts")
        print("2. Search contact")
        print("3. Update phone number")
        print("4. Sort contacts A-Z")
        print("5. Filter by suburb")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_contacts()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_phone()
        elif choice == "4":
            sort_contacts()
        elif choice == "5":
            filter_by_suburb()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")