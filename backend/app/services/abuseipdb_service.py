import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read AbuseIPDB API Key
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

# Stop application if key is missing
if not API_KEY:
    raise ValueError("AbuseIPDB API Key not found.")


def get_abuseipdb_data(ip):

    # AbuseIPDB endpoint
    url = "https://api.abuseipdb.com/api/v2/check"

    # Request headers
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    # Request parameters
    params = {
        "ipAddress": ip
    }

    try:

        # Send GET request
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=15
        )

        # Check if request was successful
        if response.status_code == 200:

            # Convert JSON into Python dictionary
            data = response.json()

            # Extract AbuseIPDB data section
            abuse_data = data["data"]

            # Return only useful fields
            return {
                "abuse_confidence_score":
                    abuse_data.get(
                        "abuseConfidenceScore",
                        0
                    ),

                "total_reports":
                    abuse_data.get(
                        "totalReports",
                        0
                    ),

                "country_code":
                    abuse_data.get(
                        "countryCode",
                        "Unknown"
                    ),

                "isp":
                    abuse_data.get(
                        "isp",
                        "Unknown"
                    ),

                "domain":
                    abuse_data.get(
                        "domain",
                        "Unknown"
                    )
            }

        # Return API error
        return {
            "error": response.json(),
            "status_code": response.status_code
        }

    except requests.exceptions.Timeout:
        return {
            "error":
                "Request timed out while connecting to AbuseIPDB."
        }

    except requests.exceptions.ConnectionError:
        return {
            "error":
                "Unable to connect to AbuseIPDB. Check your internet connection."
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }