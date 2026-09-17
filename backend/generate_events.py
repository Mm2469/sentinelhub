import json
import random
from datetime import datetime, timezone
from pathlib import Path


EVENT_TYPES = [
"login_success",
"login_failure",
"password_reset",
"suspicious_login",
]

SEVERITIES = [
"low",
"medium",
"high",
]


def generate_event(event_id):
return {
"id": event_id,
"timestamp": datetime.now(timezone.utc).isoformat(),
"event_type": random.choice(EVENT_TYPES),
"severity": random.choice(SEVERITIES),
"source": "synthetic",
}


def main():
events = [generate_event(index) for index in range(1, 11)]

output_path = Path(__file__).resolve().parents[1] / "data" / "events.json"

with output_path.open("w", encoding="utf-8") as file:
json.dump({"events": events}, file, indent=2)

print(f"Generated {len(events)} synthetic security events.")


if __name__ == "__main__":
main()
