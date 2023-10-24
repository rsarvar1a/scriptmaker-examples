
import json
import requests


domain_dev = "http://localhost:3000" 
domain_prd = "https://scriptmaker.fly.dev"
domain = domain_prd

#
# Search query
#

script_name = "Fall of"

query = {
    "conditions": [
        {
            "condition": "name",
            "input": script_name
        }
    ],
    "order": [
        {
            "order_by": "name",
            "ascending": True
        },
        {
            "order_by": "date",
            "ascending": False
        }
    ],
    "limit": {
        "count_per_page": 25,
        "page_number": 1
    }
}

#
# Print rows
#

response = requests.post(f"{domain}/api/search", json=query);

if response.ok:
    print(json.dumps(response.json()['brews'], indent=2))
else:
    print(response.status_code, response.content.decode())