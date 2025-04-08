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
        ('unfocused', 'bold,light gray', 'dark gray')
    ]