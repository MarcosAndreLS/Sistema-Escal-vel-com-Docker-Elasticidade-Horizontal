from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import socket

app = Flask(__name__)

# Adicionando o PrometheusMetrics ao Flask para coletar métricas
metrics = PrometheusMetrics(app)

# Definindo uma rota simples
@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    return f'Hello from {hostname}!'

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json  # Processa os dados recebidos
    if data:
        return jsonify({"message": "Data received", "data": data}), 200
    return jsonify({"error": "No data received"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
