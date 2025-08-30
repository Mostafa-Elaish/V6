from flask import Flask, send_from_directory, jsonify, request
import os, json
from config.settings_manager import SettingsManager
app = Flask(__name__)
BASE = os.path.join(os.path.dirname(__file__), '..')
@app.route('/')
def index():
    return send_from_directory(os.path.join(BASE, 'web', 'templates'), 'index.html')
@app.route('/api/settings', methods=['GET', 'POST'])
def api_settings():
    sm = SettingsManager()
    if request.method == 'GET':
        return jsonify(sm._data)
    data = request.json or {}
    for k,v in data.items():
        sm.set(k, v)
    return jsonify({'status':'ok','settings':sm._data})
@app.route('/api/move', methods=['POST'])
def api_move():
    body = request.json or {}
    return jsonify({'ok': True, 'received': body})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
