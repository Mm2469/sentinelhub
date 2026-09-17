from flask import Flask, jsonify
from routes import health_check

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


if __name__ == "__main__":
app.run(debug=True)
