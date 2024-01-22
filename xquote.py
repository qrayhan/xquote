import random
import requests
from bs4 import BeautifulSoup

def get_quote():
    url = "https://www.goodreads.com/quotes/tag/inspirational"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quoteText")
    quotes_text = [quote.text.strip().split("\n")[0] for quote in quotes]
    return random.choice(quotes_text)

def authenticate_x_api(x_api_key, x_api_secret):
    # Add code to authenticate with X API using the provided credentials
    # Example code:
    auth_url = "https://api.x.com/auth"
    data = {
        "api_key": x_api_key,
        "api_secret": x_api_secret
    }
    response = requests.post(auth_url, data=data)
    if response.status_code == 200:
        print("Authentication successful")
    else:
        print("Authentication failed")

def post_on_x(quote):
    # Add code to post the quote on X
    # Example code:
    post_url = "https://api.x.com/post"
    data = {
        "quote": quote
    }
    response = requests.post(post_url, data=data)
    if response.status_code == 200:
        print("Quote posted successfully")
    else:
        print("Failed to post quote")

def post_quote_on_x(quote):
    # Add your X API credentials here
    x_api_key = "YOUR_X_API_KEY"
    x_api_secret = "YOUR_X_API_SECRET"

    # Authenticate with X API
    authenticate_x_api(x_api_key, x_api_secret)

    # Post the quote on X
    post_on_x(quote)

quote = get_quote()
post_quote_on_x(quote)