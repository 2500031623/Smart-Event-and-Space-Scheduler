import pandas as pd
import matplotlib.pyplot as plt
from config import events

def show_stats():
    if not events:
        print("No data")
        return

    df = pd.DataFrame(events)

    print("\nEvent count by department:")
    print(df["dept"].value_counts())

    df["dept"].value_counts().plot(kind="bar")
    plt.title("Events per Department")
    plt.show()