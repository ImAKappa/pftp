"""downloads_4

Clean up on aisle 'Downloads'
"""

import random
from pathlib import Path

downloads_folder = Path("./downloads4")
downloads_folder.mkdir(parents=True, exist_ok=True)

# Define categories
categories = {
    "docs": {".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"},
    "audio": {".wav", ".mp3", ".aac", ".flac", ".m4a"},
    "video": {".mp4", ".mkv", ".mov", ".avi", ".wmv"},
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "apps": {".exe", ".msi", ".app", ".dmg"},
}

# Create mapping from filetype to category
extension_to_category = {}
for category, extensions in categories.items():
    for e in extensions:
        extension_to_category[e] = category

# Randomly generate test files
num_files = 100
filetypes = list(extension_to_category.keys())
for i in range(num_files):
    file = downloads_folder/f"fake_{i}{random.choice(filetypes)}"
    file.touch()

# Organize
for file in downloads_folder.iterdir():
    group = extension_to_category.get(file.suffix, None)
    if group is None:
        continue
    destination = Path(f"{file.parent}/{group}")
    destination.mkdir(parents=True, exist_ok=True)
    file.move(destination/file.name)
