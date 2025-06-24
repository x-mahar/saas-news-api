from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Article(Base):
    __tablename__='articles'

    id = Column(Integer, primary_key =True, index = True)
    headline = Column(String, nullable =False)
    url = Column(String, nullable= False, unique= True)
    publication_date = Column(DateTime, nullable= False)
    category = Column(String, nullable= True)
    sentiment = Column(String, nullable= True) #for future use
    summary= Column(String, nullable=True)

class ArticleStatistics(Base):
    __tablename__='article_statistics'

    id=Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False, unique= True)
    total_articles = Column(Integer, default=0)

