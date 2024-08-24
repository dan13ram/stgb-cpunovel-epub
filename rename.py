import os

# Specify the folder where files are located
folder = "stgb_chapters"

# Loop through files and rename them
for filename in os.listdir(folder):
    if filename.startswith("chapter_") and filename.endswith(".html"):
        chapter_num = filename[8:-5]  # Extract the chapter number
        new_filename = f"chapter_{int(chapter_num):03}.html"  # Add leading zeros
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))

print("Files renamed successfully.")

