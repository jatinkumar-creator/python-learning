import json
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stdout)
log = logging.getLogger("config")

SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)

DEFAULTS = {"host": "localhost", "port": 8080, "debug": False}

class ConfigError(Exception):
    pass

def load_config(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        log.warning("%s not found, using defaults", path.name)
        return dict(DEFAULTS)
    except json.JSONDecodeError as e:
        raise ConfigError(f"{path.name} is not valid JSON (line {e.lineno})") from e
    except PermissionError as e:
        raise ConfigError(f"cannot read {path.name}") from e

    if not isinstance(data, dict):
        raise ConfigError("top level of the config must be an object")
    config = {**DEFAULTS, **data}
    if not isinstance(config["port"], int) or not 1 <= config["port"] <= 65535:
        raise ConfigError(f"invalid port: {config['port']!r}")
    return config

cases = {
    "missing.json": None,
    "good.json": '{"port": 9000, "debug": true}',
    "broken.json": '{"port": 9000,',
    "list.json": "[1, 2, 3]",
    "badport.json": '{"port": "high"}',
}
for name, content in cases.items():
    path = SCRATCH / name
    if content is None:
        path.unlink(missing_ok=True)
    else:
        path.write_text(content, encoding="utf-8")
    try:
        print(name, "->", load_config(path))
    except ConfigError as e:
        print(name, "-> ConfigError:", e, "| cause:", type(e.__cause__).__name__ if e.__cause__ else None)