from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

def get_config():
    # This resolves to the installed WaifuBits/Configs directory
    current_dir = Path(__file__).resolve().parent

    # Go up to WaifuBits root and load .env from there
    env_path = current_dir.parent / ".env"

    if env_path.exists():
        load_dotenv(env_path)
    else:
        print(f"⚠️ .env file not found at {env_path}")

    raw_date = os.getenv("DATE")
    return {
        "DATE": datetime.today().date() if raw_date is None else datetime.fromisoformat(raw_date),
        "HABITS_FILEPATH": os.getenv('HABITS_FILEPATH'),
        "HABIT_STATUS_FILEPATH": os.getenv('HABIT_STATUS_FILEPATH')
    }

def get_palette():
    return [
        ('reversed', 'standout', ''),
        ('input_focus', 'bold,italics,white', 'dark gray'),
        ('black', 'bold,black', 'light gray'),
        ('bg', 'bold,light gray', 'black'),
        ('title', 'bold,white', 'black'),
        ('log_focus', 'italics,light gray', 'dark gray'),
        ('log_unfocus', 'light gray', 'black'),
        ('command', 'light gray', 'black'),
        ('header', 'bold,white', 'black'),
        ('dim', 'bold,dark gray', 'black'),
        ('selected', 'bold,black', 'light gray'),
        ('unselected', 'bold,light gray', ''),
        ('unfocused', 'bold,light gray', 'dark gray'),
        ('box_done', 'dark gray', ''),   # black text on white box
        ('box_empty', '', ''),
    ]