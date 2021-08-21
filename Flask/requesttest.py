import requests

url = "http://localhost/api"

test_data = {
    "hp": 200,
    "age": 1,
    "km": 50000,
    "model": 'A3',
    "gearing_type": "Automatic",
    "fuel":"electric",
    "body_color":"Brown"
}

response = requests.get(url)
#response = requests.post(url, data=test_data )

print(response.text)