from models import (
    Book, Magazine, ReferenceBook,
    StudentMember, ResearchStudent,
    FacultyMember, NotifiedMember
)

from library_service import LibraryManager
from storage import save_data, load_data


library = LibraryManager()
load_data(library)


def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Register Item")
        print("2. Register Member")
        print("3. Borrow Item")
        print("4. Return Item")
        print("5. View Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                item_id = input("Enter Item ID: ")
                title = input("Enter Title: ")

                print("1. Book")
                print("2. Magazine")
                print("3. Reference Book")

                item_type = input("Select type: ")

                classes = {
                    "1": Book,
                    "2": Magazine,
                    "3": ReferenceBook
                }

                if item_type not in classes:
                    print("Invalid item type.")
                    continue

                item = classes[item_type](item_id, title)
                library.register_item(item)
                print("Item registered successfully!")

            elif choice == "2":
                member_id = input("Enter Member ID: ")
                name = input("Enter Name: ")

                print("1. Student")
                print("2. Research Student")
                print("3. Faculty")
                print("4. Notified Member")

                member_type = input("Select type: ")

                classes = {
                    "1": StudentMember,
                    "2": ResearchStudent,
                    "3": FacultyMember,
                    "4": NotifiedMember
                }

                if member_type not in classes:
                    print("Invalid member type.")
                    continue

                member = classes[member_type](member_id, name)
                library.register_member(member)
                print("Member registered successfully!")

            elif choice == "3":
                member_id = input("Enter Member ID: ")
                item_id = input("Enter Item ID: ")
                library.borrow_item(member_id, item_id)

            elif choice == "4":
                item_id = input("Enter Item ID: ")
                library.return_item(item_id)

            elif choice == "5":
                library.show_reports()

            elif choice == "6":
                save_data(library)
                print("Thank you for using the library!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as error:
            print("Error:", error)

        except (KeyError, TypeError) as error:
            print("Invalid input:", error)