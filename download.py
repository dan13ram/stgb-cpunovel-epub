import os
import requests
from bs4 import BeautifulSoup

# Specify the folder where files will be saved
output_folder = "stgb_chapters"

# Create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through chapter numbers from 1 to 711
for chapter_num in range(650, 712):
    # Construct the URL for each chapter
    URL = f"https://cpunovel.com/stgb-chapter-{chapter_num}"
    
    # Fetch the content from the URL
    page = requests.get(URL)
    
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(page.content, "html.parser")
    
    # Remove all <script> elements
    for script in soup.find_all("script"):
        script.decompose()
    
    # Find the specific content you want to extract
    result = soup.find("div", class_="epcontent entry-content")
    
    if result:  # Check if the content is found
        # Create a file name for each chapter
        file_name = f"chapter_{int(chapter_num):03}.html"
        
        # Construct the full path to save the file
        file_path = os.path.join(output_folder, file_name)
        
        # Open a file in write mode
        with open(file_path, "w", encoding="utf-8") as file:
            # Write the prettified HTML content to the file
            file.write(result.prettify())
        
        # Notify that the file has been created
        print(f"HTML content of chapter {chapter_num} saved to {file_path}")
    else:
        print(f"Content not found for chapter {chapter_num}")

