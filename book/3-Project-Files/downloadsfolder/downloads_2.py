"""downloads_2

Clean up on aisle 'Downloads'
"""

import random
from pathlib import Path

# Make fake downloads folder
downloads_folder = Path("./downloads")
downloads_folder.mkdir(parents=True, exist_ok=True)

# Add fake files
filetypes = ["mp4", "docx", "txt", "wav", "xlsx", "pdf"]
num_files = 10
for i in range(num_files):
    file = downloads_folder/f"fake_{i}.{random.choice(filetypes)}"
    file.touch()

# List files
for file in downloads_folder.iterdir():
    print(file)
