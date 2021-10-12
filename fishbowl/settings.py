import json
import os
from fishbowl import program_dir, logger

host = "localhost"
schema_name = "qes"
username = "gone"
password = "fishing"
port = 3305


def read_settings(file_path: str):
    """Reads a settings file."""
    with open(file_path, "r") as f:
        settings = json.load(f)
    return settings

def load_settings(settings: dict):
    """Loads settings from a file."""
    logger.info(f"Loading settings.\n\tSettings: {settings}")

    global host
    global schema_name
    global username
    global password
    global port

    try:
        host = settings["host"]
        schema_name = settings["schema_name"]
        username = settings["username"]
        password = settings["password"]
        port = settings["port"]
    except KeyError as error:
        logger.error(f"Settings file is missing key {error}")
        exit()

def save_settings(settings: dict, file_path: str):
    """Saves a settings file."""
    logger.info(f"Saving settings.\n\tSettings: {settings}\n\tFile: {file_path}")
    with open(file_path, "w") as f:
        json.dump(settings, f, indent=4)


def main():
    # Check if settings file exists
    settings = {
        "host": host,
        "schema_name": schema_name,
        "username": username,
        "password": password,
        "port": port
    }

    settings_file = os.path.join(program_dir, "settings.json")
    if not os.path.exists(settings_file):
        logger.info("Settings file not found. Creating new one.")
        save_settings(settings, settings_file)
    
    # Load settings
    load_settings(read_settings(settings_file))
    logger.info("Settings loaded.")

main()