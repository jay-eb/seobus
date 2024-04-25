import os

import requests
import json

from dotenv import load_dotenv

url = "https://api.originality.ai/api/v1/scan/ai"

load_dotenv()

API_KEY = os.environ.get("ORIGINALITY_API_KEY")

payload = json.dumps({
  "content": "The Galaxy S23 launch may be far behind us, but Samsung likely has plenty more to announce in 2023. That's if history repeats itself. Should Samsung stick to its annual routine, we can expect to see new foldable phones and wearable devices in August. The company also previewed new designs for bendable phones and tablets earlier this year, hinting that the company may be planning to expand beyond the Z Fold and Z Flip in the near future. Though Samsung regularly releases new products across many categories, including TVs, home appliances and monitors, I'm most interested in where its mobile devices are headed. Samsung is one of the world's largest smartphone manufacturers by market share, meaning it has more influence than most other tech companies on the devices we carry in our pockets each day. Wearables have also become a large part of how Samsung intends to differentiate its phones from those of other Android device makers. It's a strategy to create a web of products that keep people hooked, much like Apple's range of devices.",
  "title": "optional title",
  "aiModelVersion": "1",
  "storeScan": "false"
})
headers = {
  'X-OAI-API-KEY': API_KEY,
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
