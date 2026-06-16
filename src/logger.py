from pathlib import Path
from datetime import datetime


def write_log(message):

    # Create logs folder if it doesn't exist
    Path("logs").mkdir(exist_ok=True)

    # Current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create log entry
    log_entry = f"[{timestamp}] {message}\n"

    # Append to app.log
    with open("logs/app.log", "a") as log_file:
        log_file.write(log_entry)