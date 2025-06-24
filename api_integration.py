import os
import requests
from dotenv import load_dotenv

load_dotenv()

class APIIntegration:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
        self.token = os.getenv("HUGGINGFACE_TOKEN")

        if not self.token:
            raise ValueError("Missing Hugging Face API token in .env file")

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }

    def analyze_sentiment(self, text: str) -> str:
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json={"inputs": text}
            )
            response.raise_for_status()
            result = response.json()

            if isinstance(result, list) and len(result) > 0 and 'label' in result[0]:
                return result[0]['label']
            return "NEUTRAL"

        except Exception as e:
            print(f"Sentiment API error: {e}")
            return "UNKNOWN"
