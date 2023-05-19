import requests

BASE_URL = "https://app.tmetric.com/api/v3"
API_KEY = ""

headers = {"Authorization": "Bearer " + API_KEY}
response = requests.get(
    f"{BASE_URL}/user",
    headers=headers,
)
print(response.json().get("id", "Not Found"))
