import os
from bs4 import BeautifulSoup

# Specify the folder where the HTML files are located
folder = "stgb_chapters"

# Loop through all files in the folder
for filename in os.listdir(folder):
    if filename.endswith(".html"):
        # Construct the full file path
        file_path = os.path.join(folder, filename)

        # Open and read the HTML file
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")


        # Generate the title based on the filename (e.g., "Chapter 1" from "chapter_001.html")
        chapter_title = filename.replace("_", " ").replace(".html", "").title()

        # Create an <h1> tag with the chapter title
        title_tag = soup.new_tag("h1")
        title_tag.string = chapter_title

        # Insert the <h1> tag at the very beginning
        # soup.insert(0, title_tag)

        # Find the <div> tag containing the content
        div_tag = soup.find("div", class_="epcontent entry-content")
        if div_tag:
            # Move all contents of the <div> tag outside of it and then remove the <div> tag
            # div_contents = div_tag.extract()  # Extract the div tag along with its contents
            # # soup.append(div_contents.contents)  # Append its contents directly to the soup
            # for content in div_contents:
            #     soup.append(content)
            # div_tag.decompose()  # Remove the div tag itself

            # Create a list to store the contents of the div
            # div_contents = list(div_tag.contents)
            # 
            # # Remove the div tag itself
            # div_tag.decompose()
            # 
            # # Append the contents of the div directly to the soup
            # for element in div_contents:
            #     soup.append(element)
            div_tag.insert_before(title_tag)


        # Save the modified HTML back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(str(soup.prettify()))

        print(f"Title added and div tag removed from {filename}")

print("All files have been processed.")

