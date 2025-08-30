#!/bin/bash
set -e
echo "🚀 Installing system packages and Python deps for Jarvis..."

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-venv python3-pip ffmpeg libatlas-base-dev portaudio19-dev

python3 -m venv jarvis_env
source jarvis_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Installation complete."
echo "Activate the environment with: source jarvis_env/bin/activate"
