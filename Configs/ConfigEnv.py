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
    ]