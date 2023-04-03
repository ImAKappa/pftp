files = [
    "cute-puppies.png",
    "national-security.pdf",
    "pinball3000.exe",
    "mywebsite.html",
    "filematcher.py",
    "mysterious-file.cia",
]

for file in files:
    match file.split("."):
        case [filename, ("png" | "jpg" | "webp" | "svg")]:
            print(f"'{filename}' is an image file")
        case [filename, "html"]:
            print(f"'{filename}' is a website file")
        case [filename, ("exe" | "pkg")]:
            print(f"'{filename}' is an executable")
        case [filename, ("pdf" | "docx")]:
            print(f"'{filename}' is a document file")
        case [filename, "py"]:
            print(f"'{filename}' is Python source code!")
        case _:
            print(f"Not sure what kind of file '{file}' is...")
