import requests
import json

url = "https://api.ahrefs.com/v3/site-explorer/domain-rating"

params = {
  'date': '2023-12-01',
  'target': 'https://chat.openai.com/'
}
headers = {
  'Authorization': 'Bearer rkrc2Jzzhz8GeLnaGDXYgGt9xwcrYmi_G1frajAl',
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, params=params)

print(response.text)