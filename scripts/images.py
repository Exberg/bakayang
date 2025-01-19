import os
import re
import shutil
import fnmatch

# Paths
posts_dir = "/Users/patrickyang/Documents/bakayang-blog/bakayang/src/content/posts"
attachments_dir = "/Users/patrickyang/Documents/Obsidian/Rainbell/attachments"
static_images_dir = "/Users/patrickyang/Documents/bakayang-blog/bakayang/public/images"

# Function to find images case-insensitively
def find_image_case_insensitive(image_name, search_dir):
    for root, _, files in os.walk(search_dir):
        for file in files:
            if fnmatch.fnmatch(file.lower(), image_name.lower()):
                return os.path.join(root, file)
    return None

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # Step 2: Find all image links in the format ![[image.png]] or ![[image.png|200x300]]
        images = re.findall(r'!\[\[([^\|\]]+)(?:\|((\d+)(x(\d+))?))?\]\]', content)
        print("Found images:", images)

        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image, dimensions, width, _, height in images:
            if dimensions:  # Dimensions are specified
                if height:  # Width and height
                    html_image = f'<img src="/images/{image}" width="{width}" height="{height}">'
                else:  # Only width
                    html_image = f'<img src="/images/{image}" width="{width}">'
            else:  # No dimensions
                html_image = f'<img src="/images/{image}">'

            # Debugging: Print replacement details
            print(f"Replacing: ![[{image}|{dimensions}]] with {html_image}")

            # Escape the image name and dimensions in the regex
            content = re.sub(
                rf'!\[\[{re.escape(image)}(\|{re.escape(dimensions)})?\]\]', html_image, content
            )

            # Step 4: Resolve image source path
            image_source = find_image_case_insensitive(image, attachments_dir)

            # If the image wasn't found, log and skip it
            if not image_source:
                print(f"Image not found (case-sensitive or subfolder issue): {image}")
                continue

            image_dest = os.path.join(static_images_dir, image)

            # Ensure the static_images_dir exists
            os.makedirs(static_images_dir, exist_ok=True)

            # Debugging: Log paths
            print(f"Checking source path: {image_source}")
            print(f"Destination path: {image_dest}")

            # Step 5: Check if the image exists before copying
            if not os.path.exists(image_source):
                print(f"File not found: {image_source}")
                continue  # Skip if the file doesn't exist
            else:
                print(f"File exists: {image_source}")

            # Step 6: Copy the image to the Hugo public/images directory
            try:
                print(f"Copying: {image_source} to {image_dest}")
                shutil.copy(image_source, image_dest)
            except FileNotFoundError as e:
                print(f"File not found error for {image}: {e}")
            except PermissionError as e:
                print(f"Permission error for {image}: {e}")
            except Exception as e:
                print(f"Unexpected error copying {image}: {e}")

        # Step 7: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

        print("Updated content written to:", filepath)

print("Markdown files processed and images copied successfully.")
