from flask import Flask, jsonify
from routes import health_check, get_events

app = Flask(__name__)


@app.route("/")
def home():
return jsonify({
"project": "SentinelHub",
"status": "online",
"message": "SentinelHub backend is running"
})


@app.route("/health")
def health():
return health_check()

@app.route("/events")
def events():
return get_events()


if __name__ == "__main__":
app.run(debug=True)
