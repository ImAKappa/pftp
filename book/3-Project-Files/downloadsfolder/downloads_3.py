"""downloads_3

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

# Sort files
for file in downloads_folder.iterdir():

    # Assign the file to a group
    group = ""
    match file.suffix:
        case ".txt"|".pdf"|".doc"|".docx"|".xls"|".xlsx"|".ppt"|".pptx":
            group = "docs"
        case ".mov"|".mp4"|".avi":
            group = "videos"
        case ".png"|".jpeg"|".jpg"|".gif"|".bmp"|".webp":
            group = "images"
        case ".wav"|".mp3"|".m4a"|".aac"|".flac":
            group = "audio"
        case ".exe"|".msi"|".dmg"|".app":
            group = "apps"

    # Move the file to the new group
    destination = Path(f"{file.parent}/{group}")
    destination.mkdir(parents=True, exist_ok=True)
    file.move(destination/file.name)
