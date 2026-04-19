"""
utils/config_loader.py
Loads project configuration from config.yaml.
"""
import yaml
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent

def load_config(path: str = None) -> dict:
    cfg_path = path or (_ROOT / "config.yaml")
    with open(cfg_path, "r") as f:
        return yaml.safe_load(f)

def get_path(key_path: str, config: dict = None) -> Path:
    """
    Resolve a nested config path key (dot-separated) to an absolute Path.
    Example: get_path("paths.data.raw.structured")
    """
    cfg = config or load_config()
    keys = key_path.split(".")
    val = cfg
    for k in keys:
        val = val[k]
    return (_ROOT / val).resolve()
