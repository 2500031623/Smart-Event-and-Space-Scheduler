from config import events

def search_events():
    key = input("Enter keyword: ").lower()

    results = [
        ev for ev in events
        if key in ev["name"].lower() or key in ev["dept"].lower()
    ]

    if not results:
        print("No results found.")
        return

    for ev in results:
        print(ev)