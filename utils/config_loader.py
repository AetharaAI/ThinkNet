import os
import yaml

# Get the absolute path dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(BASE_DIR, 'model_servers', 'models_config.yaml')

def load_yaml_config(path: str) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)

# Load config using the dynamic path
config = load_yaml_config(CONFIG_PATH)
