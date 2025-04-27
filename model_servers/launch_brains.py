import yaml
import subprocess
import time
import os

# Load YAML config
config_path = os.path.join(os.path.dirname(__file__), "models_config.yaml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

# Map brain names to ports
ports = {
    "emotionalmodel": 5001,
    "technicalmodel": 5002,
    "langaugemodel": 5003,
    "logicmodel": 5004,
    "creativemodel": 5005
}

# Absolute path to project root (one level up from model_servers)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Spin up brain servers
for brain_name in config.keys():
    if brain_name not in ports:
        continue  # skip mood_controller or any other non-brain sections

    print(f"🧠 Spinning up {brain_name} on port {ports[brain_name]}...")

    subprocess.Popen(
        ["python", "model_servers/serve_brain.py", brain_name],
        cwd=project_root,  # IMPORTANT: set working directory to project root
        env={**os.environ, "PYTHONPATH": project_root}  # IMPORTANT: ensure modules can be found
    )

    time.sleep(2)  # slight delay between launching each brain
