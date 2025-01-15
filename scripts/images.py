import os
import re
import shutil

# Paths
posts_dir = "/Users/patrickyang/Documents/bakayang-blog/bakayang/src/content/posts"
attachments_dir = "/Users/patrickyang/Documents/Obsidian/Rainbell/ctf-writeups-main/ctf-images"
static_images_dir = "/Users/patrickyang/Documents/bakayang-blog/bakayang/public/images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r") as file:
            content = file.read()

        # Step 2: Find all image links in the format ![[image.png|600x500]] or ![[image.png|600]]
        images = re.findall(r'!\[\[([^|]+)\|((\d+)(x(\d+))?)\]\]', content)

        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image, dimensions, width, _, height in images:
            if height:  # Width and height specified
                html_image = f'<img src="/images/{image}" width="{width}" height="{height}">'
            else:  # Only width specified
                html_image = f'<img src="/images/{image}" width="{width}">'

            # Replace the markdown image syntax with the HTML image tag
            content = re.sub(fr'!\[\[{image}\|{dimensions}\]\]', html_image, content)

            # Step 4: Copy the image to the Hugo public/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
