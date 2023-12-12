from pathlib import Path

print("File Path",Path(__file__).absolute())
print("Path of Directory",Path().absolute())
print("Path of Root",Path().absolute().parent)