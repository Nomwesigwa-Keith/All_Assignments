import os
import shutil
import time
from datetime import datetime

# Define the source folder to monitor
source_folder = 'C:\\Users\\USER\\Downloads'

# Define the backup folder
backup_folder = os.path.join(source_folder, 'backup')

# Create the backup folder if it doesn't exist
os.makedirs(backup_folder, exist_ok=True)

# Get current time
now = time.time()

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file's last modified time
    last_modified = os.path.getmtime(file_path)

    # If modified in the last 3 minutes (180 seconds)
    if now - last_modified <= 180:
        target_path = os.path.join(backup_folder, filename)
        shutil.copy2(file_path, target_path)  # copy2 preserves metadata
        print(f'Backed up: {filename} -> backup/')
