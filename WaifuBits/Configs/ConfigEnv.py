from datetime import datetime
import os
from dotenv import load_dotenv

def get_config():
    load_dotenv()
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