import threading
import requests
from bs4 import BeautifulSoup

def scrape_news():
    # Example scraping function
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract news titles
    headlines = [a.text for a in soup.find_all('a', class_='storylink')]
    print("Scraped headlines:", headlines)

def start_scraping():
    thread = threading.Thread(target=scrape_news)
    thread.daemon = True
    thread.start()
