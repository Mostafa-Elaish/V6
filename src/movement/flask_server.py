from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)
WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'web_dashboard')
GUARD_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'demo', 'guard_state.txt')

@app.route('/')
def root():
    return send_from_directory(WEB_DIR, 'index.html')

@app.route('/move', methods=['POST'])
def move():
    d = request.get_json(force=True)
    print('Move', d)
    return jsonify({'ok': True})

@app.route('/guard')
def guard():
    toggle = request.args.get('toggle')
    cur = 'off'
    if os.path.exists(GUARD_FILE):
        with open(GUARD_FILE) as fh:
            cur = fh.read().strip()
    if toggle:
        new = 'on' if cur=='off' else 'off'
        os.makedirs(os.path.dirname(GUARD_FILE), exist_ok=True)
        with open(GUARD_FILE,'w') as fh: fh.write(new)
        return jsonify({'enabled': new})
    return jsonify({'enabled': cur})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
