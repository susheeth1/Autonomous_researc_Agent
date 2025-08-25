import os
import json
from dotenv import load_dotenv
from serpapi import GoogleSearch

print("--- Starting Serper API Direct Test ---")

# Load environment variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv("SERPER_API_KEY")

if not api_key:
    print("ERROR: SERPER_API_KEY not found in .env file.")
else:
    print("API Key loaded successfully.")
    
    # Set the search parameters
    params = {
        "engine": "google",
        "q": "Impact of LLM on job market",
        "api_key": api_key,
    }

    try:
        # Perform the search
        print("Sending request to Serper...")
        search = GoogleSearch(params)
        results = search.get_dict()
        
        # Print the full result
        print("\n--- Full Response from Serper: ---")
        print(json.dumps(results, indent=2))

        # Check for organic results
        if "organic_results" in results and results["organic_results"]:
            print(f"\nSUCCESS: Found {len(results['organic_results'])} search results.")
        else:
            print("\nWARNING: Search succeeded but returned no organic results. Check your Serper account status.")

    except Exception as e:
        print(f"\nERROR: The API call failed. Details: {e}")

print("\n--- Test Complete ---")