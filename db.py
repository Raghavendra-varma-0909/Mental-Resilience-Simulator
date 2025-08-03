import json
from datetime import datetime

DB_FILE = "journal_entries.json"

def save_entry(entries, score, topic):
    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append({
        "timestamp": str(datetime.now()),
        "topic": topic,
        "entries": entries,
        "score": score
    })

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)