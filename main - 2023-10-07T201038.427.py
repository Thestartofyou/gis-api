import requests

def query_gis_api(location, property_type, api_key):
    """
    Query a GIS API to find commercial-zoned properties.

    Args:
        location (str): The location (e.g., "Billerica, Massachusetts").
        property_type (str): The type of property to search for (e.g., "commercial").
        api_key (str): The API key for authentication.

    Returns:
        list: A list of commercial-zoned properties.
    """
    api_url = "https://example-gis-api.com/query"
    params = {
        "location": location,
        "property_type": property_type,
        "api_key": api_key
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()  # Assuming the API returns JSON data
        commercial_properties = data.get("commercial_properties", [])
        return commercial_properties
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def main():
    location = "Billerica, Massachusetts"
    property_type = "commercial"
    api_key = "your_api_key_here"  # Replace with your API key

    commercial_properties = query_gis_api(location, property_type, api_key)

    if commercial_properties:
        print("Commercial-zoned properties in Billerica:")
        for property_info in commercial_properties:
            print(f"- {property_info}")
    else:
        print("No commercial properties found.")

if __name__ == "__main__":
    main()
