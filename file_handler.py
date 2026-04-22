import csv
import json
from config import events

def save_csv():
    with open("events.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=events[0].keys())
        writer.writeheader()
        writer.writerows(events)
    print("Saved to CSV")

def load_csv():
    try:
        with open("events.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                events.append(dict(row))
        print("Loaded CSV")
    except:
        print("No CSV file found")

def save_json():
    with open("events.json", "w") as f:
        json.dump(events, f, indent=4)
    print("Saved to JSON")

def load_json():
    try:
        with open("events.json", "r") as f:
            data = json.load(f)
            events.extend(data)
        print("Loaded JSON")
    except:
        print("No JSON file found")