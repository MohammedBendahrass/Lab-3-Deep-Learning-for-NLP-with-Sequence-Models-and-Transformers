import requests
from bs4 import BeautifulSoup
import re

def scrape_arabic_text_from_kolalkotob():
    url = "url"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all text content from the website
    all_text = soup.find_all(text=True)

    # Regular expression to match Arabic text
    arabic_text_pattern = re.compile(r"[\u0600-\u06FF]+")

    # Extract and filter only Arabic text
    arabic_text = []
    for text in all_text:
        matches = arabic_text_pattern.findall(text)
        if matches:
            arabic_text.append(" ".join(matches))

    return arabic_text

def save_arabic_text_to_file(arabic_text, filename="file_name.txt"):
    if not arabic_text:
        print("No Arabic text found to save.")
        return
    
    with open(filename, "w", encoding="utf-8") as file:
        for line in arabic_text:
            file.write(line + "\n")
    print(f"Saved Arabic text to {filename}")

def main():
    print("Scraping Arabic text from URL ...")
    arabic_text = scrape_arabic_text_from_kolalkotob()
    if arabic_text:
        print(f"Found {len(arabic_text)} Arabic text segments.")
        save_arabic_text_to_file(arabic_text)
    else:
        print("No Arabic text was found on the website.")

if __name__ == "__main__":
    main()
