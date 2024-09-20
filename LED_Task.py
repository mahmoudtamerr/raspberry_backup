import requests

url = "https://example.com/api"  # Replace with your server URL
data = {
    'sensor': 'temperature',
    'value': 25.4  # Example data
}

# Send POST request
response = requests.post(url, json=data)

# Check the response from the server
if response.status_code == 200:
    print('Data sent successfully')
else:
    print(f'Failed to send data. Status code: {response.status_code}')
