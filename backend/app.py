from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
return jsonify({
"project": "SentinelHub",
"status": "online",
"message": "SentinelHub backend is running"
})


if __name__ == "__main__":
app.run(debug=True)
