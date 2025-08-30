#!/usr/bin/env bash
set -e
echo "[Jarvis] Installing system packages..."
sudo apt-get update
sudo apt-get install -y python3-pip python3-venv ffmpeg libatlas-base-dev
python3 -m venv jarvis_env
source jarvis_env/bin/activate
pip install --upgrade pip
pip install -r install/requirements.txt
echo "[Jarvis] Done. Activate with: source jarvis_env/bin/activate"
