"""downloadsfolder

Module for 'Downloads Folder' code-along
"""

from pathlib import Path
from typing import Self

import pftp.codealong as ca


def downloads_0() -> None:
    """Clean up on aisle 'Downloads'"""

    from pathlib import Path

    # Make fake downloads folder
    downloads_folder = Path("./downloads")
    downloads_folder.mkdir(parents=True, exist_ok=True)


def downloads_1() -> None:
    """Clean up on aisle 'Downloads'"""

    from pathlib import Path

    # Make fake downloads folder
    downloads_folder = Path("./downloads")
    downloads_folder.mkdir(parents=True, exist_ok=True)

    # List files
    for file in downloads_folder.iterdir():
        print(file)

def downloads_2() -> None:
    """Clean up on aisle 'Downloads'"""

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

def downloads_3() -> None:
    """Clean up on aisle 'Downloads'"""

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

def downloads_4() -> None:
    """Clean up on aisle 'Downloads'"""

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

if __name__ == "__main__":
    downloads_cleaner = ca.CodeAlong(
        "Downloads Cleaner",
        [
            ca.Snippet(downloads_0, ca.SnippetMetadata()),
            ca.Snippet(downloads_1, ca.SnippetMetadata()),
            ca.Snippet(downloads_2, ca.SnippetMetadata()),
            ca.Snippet(downloads_3, ca.SnippetMetadata()),
            ca.Snippet(downloads_4, ca.SnippetMetadata()),
        ],
    )

    downloads_cleaner.test()
    downloads_cleaner.write(Path("./docs/3-Project-Files/downloadsfolder"))
