import requests
from typing import List, Dict, Any, Optional

def get_polls(skip: int = 0, limit: int = 10) -> Optional[List[Dict[str, Any]]]:
    """
    Fetches paginated poll data from the /polls endpoint.

    Args:
        skip (int): The number of items to skip for pagination.
        limit (int): The maximum number of items to return.

    Returns:
        Optional[List[Dict[str, Any]]]: A list of poll objects from the API, 
                                         or None if an error occurs.
    """
    url = "http://localhost:8000/polls"
    params = {
        "skip": skip,
        "limit": limit
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    print("Fetching polls with default pagination (skip=0, limit=10):")
    polls_data = get_polls()
    
    if polls_data:
        for poll in polls_data:
            print(f"  - ID: {poll.get('id')}, Question: {poll.get('question')}")
    else:
        print("Could not fetch polls.")

    print("\nFetching polls with custom pagination (skip=5, limit=5):")
    custom_polls_data = get_polls(skip=5, limit=5)

    if custom_polls_data:
        for poll in custom_polls_data:
            print(f"  - ID: {poll.get('id')}, Question: {poll.get('question')}")
    else:
        print("Could not fetch polls with custom pagination.")
