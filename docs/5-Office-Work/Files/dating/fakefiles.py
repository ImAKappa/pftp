"""fakefiles

This module generates fake files for testing
"""

import faker
from pathlib import Path
import shutil

def new_fake_files(fake: faker.Faker, root: Path, n: int) -> None:
    for _ in range(n):
        file = root/Path(fake.file_name())
        file.write_text("This is a fake file!")

def new_fake_folders(root: Path, n: int) -> list[Path]:
    for i in range(n):
        dir = root/Path(f"fakefolder-{i}")
        dir.mkdir(exist_ok=True)

def empty_dir(dir: Path) -> None:
    shutil.rmtree(dir)
    dir.mkdir()

def main() -> None:
    fake = faker.Faker()
    root = Path("fakedata")
    empty_dir(root)
    new_fake_files(fake, root, n=22)
    new_fake_folders(root, n=5)
        
if __name__ == "__main__":
    main()