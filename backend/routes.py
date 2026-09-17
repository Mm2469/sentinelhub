import json
from pathlib import Path

from flask import jsonify


DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "events.json"


def health_check():
return jsonify({
"status": "healthy",
"service": "SentinelHub API"
})


def get_events():
with DATA_FILE.open("r", encoding="utf-8") as file:
data = json.load(file)

return jsonify(data)
