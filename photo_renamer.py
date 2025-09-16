import os
from datetime import datetime

def rename_photos(folder_path, prefix="photo"):
    today = datetime.now().strftime("%Y%m%d")

    # Get all image files in folder
    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    # Sort files by creation/modification time
    files.sort(key=lambda x: os.path.getctime(os.path.join(folder_path, x)))

    for count, filename in enumerate(files, start=1):
        # get file extension
        _, ext = os.path.splitext(filename)

        # new name with prefix, date, and counter
        new_name = f"{prefix}_{today}_{count}{ext}"

        # old path and new path
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)

        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

# Example usage
folder = r"C:\Users\YourName\Pictures\Test"   # Change path
rename_photos(folder, prefix="vacay")
