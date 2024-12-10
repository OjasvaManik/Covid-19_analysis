import os
import requests

def download_csv(url, save_path):
    """Download a CSV file from a URL."""
    if not os.path.exists("data"):
        os.makedirs("data")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"File downloaded successfully and saved to {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
