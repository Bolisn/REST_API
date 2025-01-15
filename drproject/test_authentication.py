import requests

# Get a token by authenticating with the superuser credentials
response = requests.post('http://127.0.0.1:8000/api/token/', data={'username': 'admin', 'password': '12345'})

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    token = response.json()['token']
    
    # Use the token to authenticate a request to the /items endpoint
    response = requests.get('http://127.0.0.1:8000/items/', headers={'Authorization': f'Token {token}'})
    print(response.json())
else:
    print(f"Failed to retrieve token. Status code: {response.status_code}")