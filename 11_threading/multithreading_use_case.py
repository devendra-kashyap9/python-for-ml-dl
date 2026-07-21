'''
Real World Example: MultiThreading for I/O bound task.
Scenario: Web Scrapping
Web scrapping often involves making numerous requests to fetch web pages. These tasks are I/O
bound because they spend a lot of time waiting for responses from servers.
Multithreading cam significantly improves the performance by allowing multiple web pages to be fetched
concurrently.
'''

import requests
import threading
from bs4 import BeautifulSoup

# List of URLs
urls = [
    "https://docs.langchain.com/oss/python/langchain/quickstart",
    "https://docs.langchain.com/oss/python/langchain/knowledge-base",
    "https://docs.langchain.com/oss/python/langgraph/overview"
]

# Browser headers
# 📌 Might NOT needed for WINDOWS
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    )
}

def fetch_content(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)

        print(f"\nURL: {url}")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            print(f"Fetched {len(text)} characters")

            # Print first 300 characters
            print("Preview:")
            print(text[:300])
            print("-" * 60)

        else:
            print(f"Failed to fetch page. HTTP {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}")
        print(e)


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\n✅ All webpages fetched successfully!")