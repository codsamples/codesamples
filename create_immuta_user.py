import requests
import json

# Set the URL and API key for your Immuta instance
base_url = "https://your.immuta.instance/api"
api_key = "your-api-key"

# Set the headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Set the group ID and user ID
group_id = 1
user_id = 2

# Set the action to add or remove the user from the group
action = "add"  # can be "add" or "remove"

# Set the data for the API request
data = {
    "userId": user_id,
    "groupIds": [group_id]
}

# Make the API request to add or remove the user from the group
if action == "add":
    response = requests.post(f"{base_url}/groups/{group_id}/users", headers=headers, json=data)
elif action == "remove":
    response = requests.delete(f"{base_url}/groups/{group_id}/users/{user_id}", headers=headers)

# Print the response from the API
print(response.json())
