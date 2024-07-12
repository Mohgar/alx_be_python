def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item to shopping_list
            added_item = input("Enter the item to add: ")  # This line meets the requirement
            shopping_list.append(added_item)
            print(f"{added_item} added to the shopping list")


        elif choice == '2':
            removed_item = input("inter the item to remove: ")  # Prompt for and remove an item
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"{removed_item} removed from the shopping list")
            else:
                print(f"{removed_item} is not found in shopping list")


        elif choice == '3':
            for item in shopping_list:
                print(item)
                # Display the shopping list

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
