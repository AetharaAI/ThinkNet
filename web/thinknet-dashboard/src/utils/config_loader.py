import yaml
from pathlib import Path

class ConfigLoader:
    """
    Loads YAML configuration files safely.
    """

    @staticmethod
    def load_config(filepath: str) -> dict:
        try:
            path = Path(filepath)
            with open(path, 'r') as file:
                config = yaml.safe_load(file)
            return config
        except Exception as e:
            raise RuntimeError(f"Failed to load config file {filepath}: {e}")
