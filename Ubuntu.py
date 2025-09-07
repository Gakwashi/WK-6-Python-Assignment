import os
import requests
from urllib.parse import urlparse
from datetime import datetime

# Prompt user for image URL
url = input("Enter the image URL: ").strip()

#  Create directory for fetched images
folder = "Fetched_Images"
os.makedirs(folder, exist_ok=True)

try:
    #  Fetch image from the web
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Respectful error handling

    # Extract filename from URL or generate one
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or "." not in filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}.jpg"

    #  Save image in binary mode
    filepath = os.path.join(folder, filename)
    with open(filepath, "wb") as file:
        file.write(response.content)

    print(f"Image saved successfully as '{filename}' in '{folder}'.")

except requests.exceptions.RequestException as e:
    print("Failed to fetch image. Please check the URL or your connection.")
    print(f"Details: {e}")
except Exception as e:
    print(" An unexpected error occurred while saving the image.")
    print(f"Details: {e}")
