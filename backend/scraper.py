
import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://help.jupiter.money/en/"
START_URL = BASE_URL + "articles"

def scrape_articles():
    response = requests.get(START_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    faq_data = []

    for link in soup.select("a.article-list-link"):
        article_url = BASE_URL + link['href']
        article_res = requests.get(article_url)
        article_soup = BeautifulSoup(article_res.text, "html.parser")

        title = article_soup.find("h1").text.strip()
        content = article_soup.find("div", class_="article-body")
        paragraphs = [p.get_text(strip=True) for p in content.find_all("p")]

        answer = " ".join(paragraphs)
        faq_data.append({"question": title, "answer": answer, "url": article_url})

    with open("data/faq_data.json", "w", encoding="utf-8") as f:
        json.dump(faq_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    scrape_articles()
