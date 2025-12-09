"""downloadsfolder

Module for 'Downloads Folder' code-along
"""
from typing import Self
from pathlib import Path
from pftp.codealong import CodeAlong, CodeAlongWriter, CodeAlongTester

class DownloadsFolder(CodeAlong):

    def __init__(self) -> Self:
        super().__init__("Fortune Teller",
            sections=[
                self.downloads_0,
                self.downloads_1,
                self.downloads_2,
            ]
        )

    def downloads_0(self) -> None:
        """Clean up on aisle 'Downloads'"""

        from pathlib import Path

        downloads_folder = Path("downloads")

        for file in downloads_folder.iterdir():
            print(file)

    def downloads_1(self) -> None:
        """Clean up on aisle 'Downloads'"""

        from pathlib import Path

        # Make fake downloads folder
        path = Path("./downloads")
        path.mkdir(parents=True, exist_ok=True)

        # Clean downloads folder
        downloads_folder = Path("downloads")

        for file in downloads_folder.iterdir():
            print(file)

    def downloads_2(self) -> None:
        """Clean up on aisle 'Downloads'"""

        from pathlib import Path
        import random

        # Make fake downloads folder
        path = Path("./downloads")
        path.mkdir(parents=True, exist_ok=True)
        # Add fake files
        filetypes = [".mp4", ".docx", ".txt", ".wav", ".xlsx", ".pdf"]
        num_files = 10
        for i in range(num_files):
            path.touch(f"fake_{i}.{random.choice(filetypes)}")

        # Clean downloads folder
        downloads_folder = Path("downloads")

        for file in downloads_folder.iterdir():
            print(file)

if __name__ == "__main__":
    tester = CodeAlongTester()
    tester.test_for_errors(DownloadsFolder())

    writer = CodeAlongWriter()
    output = Path("./docs/3-Downloads-Folder/downloadsfolder")
    writer.write(output, DownloadsFolder())