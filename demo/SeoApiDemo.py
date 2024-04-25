import os

import requests
import json

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("AHREFS_API_KEY")

url = "https://api.ahrefs.com/v3/site-explorer/domain-rating"

params = {
  'date': '2023-12-01',
  'target': 'https://chat.openai.com/'
}
headers = {
  'Authorization': 'Bearer ' + API_KEY,
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, params=params)

print(response.text)