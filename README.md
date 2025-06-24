
# SaaS News Scraper API

This is a Python-based web application that scrapes articles from [TheSaaSNews](https://www.thesaasnews.com), enriches them with sentiment analysis using Hugging Face, and serves the data via a FastAPI backend. Data is stored in a local SQLite database.

---

## 🚀 Features

- 🔎 Scrapes article headline, URL, date, summary, and category
- 📈 Enriches data with sentiment analysis (Positive/Negative)
- 💾 Stores data using SQLAlchemy and SQLite
- 🌐 REST API built using FastAPI
- 🧹 Clean, modular, object-oriented architecture

---
## 🐳 Docker Support

You can run this project using Docker:

### Build the image
```bash
docker build -t saas-news-api .


## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- BeautifulSoup
- Hugging Face API (sentiment model)
- SQLite (via `saasnews.db`)

---

## 📦 Installation

1. **Clone or unzip** the project folder.

2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the root directory:

```env
HUGGINGFACE_TOKEN=your_huggingface_token_here
```

You can get a free token here: https://huggingface.co/settings/tokens

---

## 🧪 Running the Application

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

Then open your browser at:  
📍 `http://127.0.0.1:8000/docs` (Swagger UI)

---

## 🧾 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/articles/scrape` | Scrapes articles and stores them in the database |
| `GET`  | `/articles` | Returns all articles; supports filtering by `category` and `date` |
| `GET`  | `/article/{id}` | Returns a single article by ID |
| `GET`  | `/article-statistics` | Returns total articles per category |

---

## 🧠 Optional Enhancements (Implemented or Suggested)

- [x] Sentiment enrichment via Hugging Face
- [x] Modular `Scraper` class
- [ ] `APIIntegration` class (can be added)
- [ ] Async scraping (bonus)
- [ ] Docker containerization (bonus)

---

## 👤 Author

Nitin Mahar  
Python Intern Candidate  
Contact: nitintnk5@gmail.com

---

## 📜 License

This project is for educational and evaluation purposes under internship assessment.
