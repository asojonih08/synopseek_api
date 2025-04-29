import requests
import os
from dotenv import load_dotenv


load_dotenv()

def google_custom_search(search_query):
    """
    Perform a Google Custom Search (Google Custom Search JSON Api) query using the provided search query.
    
    Args:
        search_query (str): The search terms to query.

    Returns:
        dict: The JSON response from the Google Custom Search API, if successful.
        None: If the request fails or an error occurs.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    search_engine_id = os.environ.get("GOOGLE_SEARCH_ENGINE_ID")

    if not api_key or not search_engine_id:
        print("Missing Google API key or Search Engine ID in environment variables.")
        return None
    try:
        url = f'https://www.googleapis.com/customsearch/v1'
        params = {
            'key': api_key,
            'cx': search_engine_id,
            'q': search_query
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'An error occurred during the Google Custom Search request: {e}')
        return None