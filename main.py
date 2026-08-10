
import os

def main():

    version = 0.1
    exiting: bool = False

    while not exiting:

        clear_terminal()
        print(f"Expense Manager App v{version}")

        print("""
================================
      EXPENSE MANAGER
================================

1. Add expense
2. List expenses
3. Remove expense
4. Filter expenses
5. Show summary
6. Exit

Choose an option: """)

        option = input("> ")
        match option:
            case "1":
                select_add_expense()
            case "2":
                select_list_expenses()
            case "3":
                select_remove_expenses()
            case "4":
                select_filter_expenses()
            case "5":
                select_show_summary()
            case "6":
                exiting = select_exit()
            case _:
                print("> Invalid option")
                input("> Press any key to continue...")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def select_add_expense():
    pass

def select_list_expenses():
    pass

def select_remove_expenses():
    pass

def select_filter_expenses():
    pass

def select_show_summary():
    pass

def select_exit():
    print("Goodbye!")
    return True

if __name__ == "__main__":
    main()
