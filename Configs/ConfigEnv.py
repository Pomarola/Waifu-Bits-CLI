import datetime
import os
from dotenv import load_dotenv

def get_config():
    load_dotenv()
    return {
        "DATE": datetime.date.today().isoformat() if os.getenv('DATE') is None else os.getenv('DATE'),
        "HABITS_FILEPATH": os.getenv('HABITS_FILEPATH'),
        "HABIT_STATUS_FILEPATH": os.getenv('HABIT_STATUS_FILEPATH')
    }

def get_palette():
    return [
        # Default fallback style
        ('reversed', 'standout', ''),

        # Input and focused box (border/title + field)
        ('input_focus', 'white', 'dark gray'),

        # Selected item in habit list
        ('black', 'black', 'light gray'),

        # Default background
        ('bg', 'light gray', 'black'),

        # LineBox titles
        ('title', 'white', 'black'),

        # Logs
        ('log_focus', 'light gray', 'dark gray'),

        # Command box
        ('command', 'light gray', 'black'),

        # Header or dimmed/placeholder text
        ('header', 'white', 'black'),
        ('dim', 'dark gray', 'black'),

        ('selected', 'black', 'light gray'),
        ('unselected', 'light gray', ''),
        ('unfocused', 'light gray', '')
    ]