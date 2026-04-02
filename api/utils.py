import json
import re
from typing import Any, Dict, Optional
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    """
    Checks if a given string is a valid URL.
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def is_valid_email(email: str) -> bool:
    """
    Checks if a given string is a valid email address.
    """
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Loads a JSON configuration file from the given path.
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in configuration file: {e}")


def get_value_from_dict(data: Dict[str, Any], key_path: str, default: Optional[Any] = None) -> Any:
    """
    Retrieves a value from a nested dictionary using a key path.
    Key path is a string where keys are separated by dots (e.g., "a.b.c").
    Returns the default value if the key path is not found.
    """
    keys = key_path.split('.')
    current = data

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default

    return current


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncates a string to a maximum length, adding a suffix if necessary.
    """
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length - len(suffix)] + suffix