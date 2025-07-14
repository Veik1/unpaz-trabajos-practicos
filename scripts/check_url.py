import re
import requests

def extract_links_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return re.findall(r'href="(https?://[^"]+)"', content)

def check_links(links):
    print("Revisando links...\n")
    for url in links:
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if status == 404:
                print(f"Error 404 Not Found: {url}")
            else:
                print(f"OK: {url} (Status: {status})")
        except requests.RequestException as e:
            print(f"Error con {url}: {e}")


if __name__ == "__main__":
    links = extract_links_from_md('README.md')
    check_links(links)