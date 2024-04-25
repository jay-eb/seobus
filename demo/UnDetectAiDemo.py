import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("UNDETECTABLE_API_KEY")

url = "https://api.undetectable.ai"


def submit():
    submit_url = url + '/submit'
    payload = json.dumps({
        "content": "要将一个列表添加到另一个列表中，你可以使用列表的 extend() 方法或者直接使用加号 + 运算符。这两种方法的效果是一样的，它们都会将一个列表中的元素添加到另一个列表的末尾。",
        "readability": "High School",
        "purpose": "General Writing",
        "strength": "More Human"
    })
    headers = {
        'api-key': API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", submit_url, headers=headers, data=payload)

    print(response.text)


# should save id returned for retrieve use
def retrieve():
    retrieve_url = url + "/document"

    payload = json.dumps({
        "id": "1714045631235x447305408134080830"
    })
    headers = {
        'api-key': API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", retrieve_url, headers=headers, data=payload)

    print(json.loads(response.text))


if __name__ == '__main__':
    retrieve()