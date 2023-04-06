"""zippy

This module provides functions for zipping and unzipping a collection of folders
"""

from pathlib import Path
import uuid
import shutil
from zipfile import ZipFile

def empty_dir(dir: Path) -> None:
    shutil.rmtree(dir)
    dir.mkdir()

def new_fake_folders(root: Path, n: int) -> None:
    """Generates fake folders in root"""
    for _ in range(n):
        folder = root/Path(f"some-folder-{uuid.uuid4()}")
        folder.mkdir()
        file = folder/Path(f"my-file-{uuid.uuid4()}.txt")
        file.write_text("This is a fake file!")

def zip_all_folders(root: Path) -> None:
    """Zips all folders in the `root` directory"""
    for file in root.iterdir():
        if file.is_dir():
            shutil.make_archive(root/file.name, "zip", file)

def remove_unzipped(root: Path) -> None:
    """Removes all unzipped folders"""
    for file in root.iterdir():
        if file.is_dir():
            shutil.rmtree(file)

def extract_all_folders(root: Path) -> None:
    """Extracts all zip archives"""
    for file in root.iterdir():
        if file.suffix == ".zip":
            with ZipFile(file, "r") as zip_ref:
                zip_ref.extractall(root/file.stem)

def remove_zipped_folders(root: Path) -> None:
    """Removes zip archives in a folder"""
    for file in root.iterdir():
        if file.suffix == ".zip":
            file.unlink()

def main() -> None:
    root = Path("fakedata")
    root.mkdir(exist_ok=True)
    empty_dir(root)
    new_fake_folders(root, n=100)
    zip_all_folders(root)
    remove_unzipped(root)
    extract_all_folders(root)
    remove_zipped_folders(root)

if __name__ == "__main__":
    main()