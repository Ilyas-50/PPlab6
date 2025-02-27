import os
path = "."
items = os.listdir(path)

directories = []
files = []

for item in items:
    if os.path.isdir(item):
        directories.append(item)
    if os.path.isfile(item):  
        files.append(item)

print("Directories:", directories)
print("Files:", files)
print("All:", items)
