import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_resource(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = os.path.join(folder_path, os.path.basename(urlparse(url).path))
        with open(file_name, "wb") as file:
            file.write(response.content)
        return file_name
    return None

def download_website(base_url, start, end):
    for i in range(start, end+1):
        url = f"{base_url}{i}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            folder_name = f"downloaded_websites/website_{i}"
            os.makedirs(folder_name, exist_ok=True)
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Download all resources (images, stylesheets, scripts, etc.)
            for tag in soup.find_all(['img', 'link', 'script'], src=True):
                resource_url = urljoin(url, tag['src'])
                local_path = download_resource(resource_url, folder_name)
                if local_path:
                    tag['src'] = os.path.relpath(local_path, folder_name)
                else:
                    print(f"Failed to download resource: {resource_url}")

            # Save the modified HTML content
            with open(os.path.join(folder_name, "index.html"), "w", encoding="utf-8") as file:
                file.write(str(soup))

            print(f"Downloaded: {url}")
        else:
            print(f"Failed to download: {url}")

# Replace these values with your actual base URL and the range of websites you want to download
base_url = "https://flamecomics.com/the-ancient-sovereign-of-eternity-chapter-"
start_range = 241
end_range = 255

download_website(base_url, start_range, end_range)
