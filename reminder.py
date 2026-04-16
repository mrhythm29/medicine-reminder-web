import json
import time
from datetime import datetime
from plyer import notification

file = "medicines.json"

def load_data():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

print("🔔 Reminder system started...")

while True:
    medicines = load_data()
    now = datetime.now().strftime("%H:%M")

    for med in medicines:
        if med["time"] == now:
            notification.notify(
                title="💊 Medicine Reminder",
                message=f"Time to take {med['name']}",
                timeout=10
            )
            time.sleep(60)  # avoid repeat

    time.sleep(30)