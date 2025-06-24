from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin
import requests
import re

class Scraper:
    def __init__(self, base_url="https://www.thesaasnews.com/news"):
        self.base_url = base_url
        print("📰 Scraper initialized...")

    def scrape_articles(self):
        print("🔍 Starting article scrape...")
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = []
        article_cards = soup.select("a.blog-listing-snippet")

        for i, card in enumerate(article_cards, 1):
            try:
                article_data = self._parse_article(card, i)
                if article_data:
                    articles.append(article_data)
            except Exception as e:
                print(f"❌ Error in article #{i}: {e}")
                continue

        return articles

    def _parse_article(self, card, index):
        title_el = card.select_one("h2")
        summary_el = card.select_one("p")
        href = card.get("href")

        if not (title_el and href):
            return None

        title = title_el.get_text(strip=True)
        summary = summary_el.get_text(strip=True)[:150] + "..." if summary_el else ""
        url = urljoin(self.base_url, href)

        # Fetch detail page
        detail_res = requests.get(url)
        detail_soup = BeautifulSoup(detail_res.text, "html.parser")

        pub_date = self._extract_date(detail_soup)
        category = self._extract_category(detail_soup)

        print(f"{index}. {title} — {url}")

        return {
            "headline": title,
            "url": url,
            "summary": summary,
            "publication_date": pub_date,
            "category": category
        }

    def _extract_date(self, soup):
        date_el = soup.select_one("span.blog-authored_on")
        if not date_el:
            return None
        raw = date_el.get_text(strip=True)
        cleaned = re.sub(r"(\d{1,2})(st|nd|rd|th)", r"\1", raw)
        try:
            return datetime.strptime(cleaned, "%B %d, %Y")
        except Exception as e:
            print("Date parse error:", e)
            return None

    def _extract_category(self, soup):
        cat_el = soup.select_one("a.article-category")
        return cat_el.get_text(strip=True) if cat_el else "General"
