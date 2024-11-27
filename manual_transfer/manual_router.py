from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

CONTAINER_URLS = [
    "http://flask1:5000",
    "http://flask2:5000",
    "http://flask3:5000"
]

current_container = 0


@app.route("/", methods=["GET", "POST"])
def route_request():
    global current_container

    target_url = CONTAINER_URLS[current_container]

    current_container = (current_container + 1) % len(CONTAINER_URLS)

    try:
        if request.method == "GET":
            response = requests.get(target_url)
        elif request.method == "POST":
            response = requests.post(target_url, json=request.json)
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
