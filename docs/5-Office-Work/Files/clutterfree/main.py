"""clutterfree

This module sorts files in a folder.

Useful for,ganizing your downloads folder.
"""
from pathlib import Path
from enum import Enum
from collections import Counter
from pprint import pprint

class FileCategory(Enum):
    AUDIO = "audio"
    IMAGE = "image"
    TEXT = "text"
    VIDEO = "video"
    OFFICE = "office"
    MISC = "misc"
    FOLDER = "folder"

def count_file_extensions(dir: Path) -> Counter:
    """Gets a list of unique file extensions in directory"""
    files_exts = [p.suffix for p in dir.iterdir()]
    return Counter(files_exts)

def file_category(file: Path) -> FileCategory:
    """Returns file category given file extension"""
    extension = file.suffix.lstrip(".")
    if extension in ("odt", "pptx", "ppt", "docx", "xls", "xlsx", "odp", "pdf", "key", "pages"):
            return FileCategory.OFFICE
    elif extension in ("mp3", "wav", "flac"):
        return FileCategory.AUDIO
    elif extension in ("webm", "mov", "mp4", "avi"):
        return FileCategory.VIDEO
    elif extension in ("py", "js", "txt", "json", "csv", "html", "css"):
        return FileCategory.TEXT
    elif extension in ("bmp", "png", "jpeg", "tiff", "jpg", "gif"):
        return FileCategory.IMAGE
    elif file.is_dir() or extension in ("zip"):
        return FileCategory.FOLDER
    else:
        return FileCategory.MISC
        
def move_file(file: Path) -> None:
    """Moves a file to a directory named after the category of the file"""
    category_dir = file.parent/Path(file_category(file).value)
    category_dir.mkdir(exist_ok=True)
    file.rename(category_dir/file.name)
    
def main() -> None:
    root = Path("downloads")
    pprint(count_file_extensions(root))
    for file in root.iterdir():
        move_file(file)
    # TODO: Handle the case where the script is run repeatedly

if __name__ == "__main__":
    main()