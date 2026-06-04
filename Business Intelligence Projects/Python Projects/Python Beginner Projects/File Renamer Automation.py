import os

folder = "your_folder_path"

files = os.listdir(folder)

for index, file in enumerate(files):
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, f"file_{index+1}.txt")

    os.rename(old_path, new_path)

print("Files renamed successfully!")