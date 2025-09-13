import requests
import json

def register_user(username, password):
    """
    Registers a user by making a POST request to the /register endpoint.

    Args:
        username (str): The desired username.
        password (str): The desired password.

    Returns:
        requests.Response: The response object from the API.
    """
    url = "http://localhost:8000/register"
    payload = {
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    new_user = "test_user"
    new_pass = "a_secure_password"
    
    print(f"Attempting to register user: {new_user}")
    response = register_user(new_user, new_pass)
    
    if response:
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("User registered successfully!")
            print("Response JSON:", response.json())
        else:
            print("Failed to register user.")
            print("Response:", response.text)
