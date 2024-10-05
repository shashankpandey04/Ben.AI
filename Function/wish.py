from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def wish():
    """
    This function will return the wish based on the time
    """
    NAME = os.getenv("NAME")
    hour = int(datetime.now().hour)
    if hour < 12:
        return f"Good Morning {NAME}"
    elif hour < 17:
        return f"Good Afternoon {NAME}"
    else:
        return f"Good Evening {NAME}"