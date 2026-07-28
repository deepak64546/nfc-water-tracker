import json
from datetime import datetime, date
from pathlib import Path 

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

LOG_FILE = Path(__file__).parent / "water_log.json"
DAILY_GOAL = 120


def load_entries () -> list[dict]:
    if not LOG_FILE.exists():
        return []
    with open(LOG_FILE) as f:
        return json .load(f)
    
def save_entries (entries: list[dict]) -> None:
    with open(LOG_FILE, "w") as f:
        json.dump(entries, f, indent=2)

def add_entry(amount_oz: float) -> None:
    entries = load_entries()
    entries.append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "amount_oz": amount_oz
    })
    save_entries(entries)

def get_today_total() -> float:
    today_str = date.today().isoformat()
    entries = load_entries()
    total = sum(
        e["amount_oz"] for e in entries
        if e ["timestamp"].startswith(today_str)
    )
    return total

def undo_last_entry() -> bool:
    today_str = date.today().isoformat()
    entries = load_entries()

    last_today_index = None
    for i, e in enumerate(entries):
        if e["timestamp"].startswith(today_str):
            last_today_index = i

    if last_today_index is None:
        return False
    
    entries.pop(last_today_index)
    save_entries(entries)
    return True

def reset_today() -> None:
    today_str = date.today().isoformat()
    entries = load_entries()
    entries = [e for e in entries if not e["timestamp"].startswith(today_str)]
    save_entries(entries)

@app.route("/")
def index():
    today_total = get_today_total()
    progress_pct = min(int((today_total / DAILY_GOAL) * 100), 100)
    return render_template(
        "index.html",
        today_total=today_total,
        goal=DAILY_GOAL,
        progress_pct=progress_pct,
    )

@app.route("/log", methods=["POST"])
def log_water():
    data = request.get_json()
    amount = data.get("amount_oz")

    if amount is None or amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400
    
    add_entry(float(amount))
    today_total = get_today_total()

    return jsonify({
        "success": True,
        "today_total": today_total,
        "goal": DAILY_GOAL,
        "progress_pct": min(int((today_total / DAILY_GOAL) * 100), 100),
    })

@app.route("/status")
def status():
    today_total = get_today_total()
    return jsonify({
        "today_total": today_total,
        "goal": DAILY_GOAL,
        "progress_pct": min(int((today_total / DAILY_GOAL) * 100), 100),
    })


@app.route("/undo", methods=["POST"])
def undo():
    removed = undo_last_entry()
    today_total = get_today_total()
    return jsonify({
        "success": removed,
        "today_total": today_total,
        "goal": DAILY_GOAL,
        "progress_pct": min(int((today_total / DAILY_GOAL) *100), 100),
    })

@app.route("/reset", methods=["POST"])
def reset():
    reset_today()
    return jsonify({
        "success": True,
        "today_total": 0,
        "goal": DAILY_GOAL,
        "progress_pct": 0,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)