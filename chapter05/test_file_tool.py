from tools import open_file

print("Executed File Command (Open File):", open_file("notes.txt"))
print("Missing file:", open_file("missing.txt"))
print("Outside data folder:", open_file("../.env"))