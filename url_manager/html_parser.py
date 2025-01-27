from bs4 import BeautifulSoup
import requests

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except requests.RequestException as e:
        return f"Error fetching content: {e}"

if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    print(fetch_and_parse(url))