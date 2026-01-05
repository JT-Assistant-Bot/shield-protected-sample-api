import requests
from flask import Flask, jsonify

app = Flask(__name__)

SHIELD_URL = "https://YOUR_DEPLOYED_API_DOMAIN/shield/check"
API_KEY = "PASTE_YOUR_API_KEY_HERE"

def shield_allows():
    r = requests.get(
        SHIELD_URL,
        headers={"X-API-Key": API_KEY},
        timeout=3
    )
    return r.status_code == 200

@app.route("/data")
def data():
    if not shield_allows():
        return jsonify({"error": "blocked by shield"}), 429

    return jsonify({
        "message": "This API works only because Shield is protecting it"
    })

if __name__ == "__main__":
    app.run()
