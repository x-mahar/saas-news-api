from scraper import Scraper
from api_integration import APIIntegration
from models import Article
from sqlalchemy.orm import Session

class ArticleController:
    def __init__(self, db: Session):
        self.scraper = Scraper()
        self.api = APIIntegration()
        self.db = db

    def scrape_and_store_articles(self):
        articles = self.scraper.scrape_articles()
        stored = 0

        for art in articles:
            sentiment = self.api.analyze_sentiment(art["summary"])
            if self.db.query(Article).filter_by(url=art["url"]).first():
                continue

            article = Article(
                headline=art["headline"],
                url=art["url"],
                summary=art["summary"],
                publication_date=art["publication_date"],
                category=art["category"],
                sentiment=sentiment
            )
            self.db.add(article)
            stored += 1

        self.db.commit()
        return {"message": f"{stored} new articles stored.", "total": len(articles)}
