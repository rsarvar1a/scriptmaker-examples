import json
import os
import requests


url = "https://www.bloodstar.xyz/p/AlexS/Fall_of_Rome/script.json"
edition = "fall-of-rome"


# If you could use domain_dev, you could just use scriptmaker directly instead...
domain_dev = "http://localhost:3000" 
domain_prd = "https://scriptmaker.fly.dev"
domain = domain_prd

#
# Upload a brew
#

response = requests.post(f"{domain}/api/brew", json = {
    "source": {
        "url": url,
        "edition": edition,
        "make": ['script']
    }
})

if not response.ok:
    # Might be a good time to open a GitHub issue
    print(response.status_code, response.content.decode())
    exit(1)

brew = response.json()
print(json.dumps(brew, indent=2))

#
# Save brew to known IDs
#

my_brews_path = "my_brews.json"

if not os.path.exists(my_brews_path):
    with open(my_brews_path, "w") as f:
        f.write(json.dumps([]))

with open(my_brews_path) as f:
    my_brews = json.load(f)

my_brews.append(brew)

with open(my_brews_path, "w") as f:
    f.write(json.dumps(my_brews, indent=2))