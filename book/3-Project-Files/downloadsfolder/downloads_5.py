"""downloads_5

Clean up on aisle 'Downloads'
"""

import random
from pathlib import Path

downloads_folder = Path(r"C:\Users\alexk\Downloads")
downloads_folder.mkdir(parents=True, exist_ok=True)

# Define groups
groups = {
    "docs": {".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"},
    "audio": {".wav", ".mp3", ".aac", ".flac", ".m4a"},
    "video": {".mp4", ".mkv", ".mov", ".avi", ".wmv"},
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "apps": {".exe", ".msi", ".app", ".dmg"},
}

# Create mapping from filetype to group
extension_to_group = {}
for group, extensions in groups.items():
    for e in extensions:
        extension_to_group[e] = group

# Organize
for file in downloads_folder.iterdir():
    group = extension_to_group.get(file.suffix, None)
    if group is None:
        continue
    destination = Path(f"{file.parent}/{group}")
    destination.mkdir(parents=True, exist_ok=True)
    file.move(destination/file.name)
