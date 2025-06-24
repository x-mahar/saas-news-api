from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from datetime import datetime
from db_manager import SessionLocal, init_db
from models import Article
from controller import ArticleController

app = FastAPI()
init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "API is running. Visit /docs to access the Swagger UI."}

@app.post("/articles/scrape")
def scrape_and_store(db: Session = Depends(get_db)):
    controller = ArticleController(db)
    return controller.scrape_and_store_articles()

@app.get("/articles")
def get_articles(
    category: Optional[str] = Query(None),
    date: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Article)

    if category:
        query = query.filter(Article.category.ilike(f"%{category}%"))

    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d")
            query = query.filter(Article.publication_date >= parsed_date)
        except:
            return {"error": "Invalid date format. Use YYYY-MM-DD."}

    return query.all()

@app.get("/article/{article_id}")
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter_by(id=article_id).first()
    if not article:
        return {"error": "Article not found."}
    return article

@app.get("/article-statistics")
def get_article_statistics(db: Session = Depends(get_db)):
    stats = (
        db.query(Article.category, func.count().label("total"))
        .group_by(Article.category)
        .all()
    )
    return [{"category": category, "total_articles": total} for category, total in stats]
