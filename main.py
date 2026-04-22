from event_manager import add_event, view_events, delete_event
from search import search_events
from file_handler import save_csv, load_csv, save_json, load_json
from analytics import show_stats

def menu():
    while True:
        print("\n==== SESS MENU ====")
        print("1. Add Event")
        print("2. View Events")
        print("3. Search")
        print("4. Delete")
        print("5. Save CSV")
        print("6. Load CSV")
        print("7. Save JSON")
        print("8. Load JSON")
        print("9. Analytics")
        print("0. Exit")

        ch = input("Choice: ")

        if ch == "1": add_event()
        elif ch == "2": view_events()
        elif ch == "3": search_events()
        elif ch == "4": delete_event()
        elif ch == "5": save_csv()
        elif ch == "6": load_csv()
        elif ch == "7": save_json()
        elif ch == "8": load_json()
        elif ch == "9": show_stats()
        elif ch == "0": break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()