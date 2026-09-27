"""downloads_0

Clean up on aisle 'Downloads'
"""

from pathlib import Path

# Make fake downloads folder
downloads_folder = Path("./downloads")
downloads_folder.mkdir(parents=True, exist_ok=True)
