from config import events
from validator import validate_date, validate_time

def add_event():
    print("\n=== ADD NEW EVENT ===")
    
    name = input("Enter event name: ").strip()
    if not name:
        print("Event name cannot be empty.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    if not validate_date(date):
        print("Invalid date format.")
        return

    start = input("Start time (HH:MM): ").strip()
    if not validate_time(start):
        print("Invalid start time.")
        return

    end = input("End time (HH:MM): ").strip()
    if not validate_time(end):
        print("Invalid end time.")
        return

    venue = input("Venue: ").strip()
    dept = input("Department: ").strip()
    etype = input("Event type: ").strip()

    event = {
        "name": name,
        "date": date,
        "start": start,
        "end": end,
        "venue": venue,
        "dept": dept,
        "type": etype
    }

    events.append(event)
    print("Event added successfully!")


def view_events():
    print("\n=== ALL EVENTS ===")

    if not events:
        print("No events found.")
        return

    for i, ev in enumerate(events, 1):
        print(i, ev)


def delete_event():
    view_events()
    try:
        idx = int(input("Enter event ID to delete: ")) - 1
        events.pop(idx)
        print("Deleted successfully!")
    except:
        print("Invalid ID")