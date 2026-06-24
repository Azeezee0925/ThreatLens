import os
import base64
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the VirusTotal API Key
API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

# Stop the application if the API Key is missing
if not API_KEY:
    raise ValueError("VirusTotal API Key not found.")


def investigate_ioc(ioc: str, ioc_type: str):

    # Create the VirusTotal URL based on IOC type
    if ioc_type == "ip":
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}"

    elif ioc_type == "domain":
        url = f"https://www.virustotal.com/api/v3/domains/{ioc}"

    elif ioc_type == "url":

        url_id = (
            base64.urlsafe_b64encode(
                ioc.encode()
            )
            .decode()
            .strip("=")
        )

        url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

    else:
        return {
            "error": "Unsupported IOC type"
        }

    # Create request headers
    headers = {
        "x-apikey": API_KEY
    }

    try:

        # Send GET request to VirusTotal
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        # Check whether the request was successful
        if response.status_code == 200:

            # Convert JSON into Python Dictionary
            data = response.json()

            # Extract the attributes section
            attributes = data["data"]["attributes"]

            # Extract analysis statistics
            analysis = attributes["last_analysis_stats"]

            # Threat statistics
            malicious = analysis["malicious"]
            suspicious = analysis["suspicious"]
            harmless = analysis["harmless"]

            # Additional information
            reputation = attributes.get("reputation", 0)
            country = attributes.get("country", "Unknown")
            asn = attributes.get("asn", "Unknown")
            owner = attributes.get("as_owner", "Unknown")
            last_analysis = attributes.get(
                "last_analysis_date",
                "Unknown"
            )

            # Decide Threat Status
            if malicious > 0:
                status = "Malicious"

            elif suspicious > 0:
                status = "Suspicious"

            else:
                status = "Safe"

            # Calculate Threat Score
            threat_score = min(
                (malicious * 10) + (suspicious * 5),
                100
            )

            # Return ThreatLens response
            return {
                "ioc": ioc,
                "ioc_type": ioc_type,

                "status": status,
                "threat_score": threat_score,

                "malicious": malicious,
                "suspicious": suspicious,
                "harmless": harmless,

                "reputation": reputation,
                "country": country,
                "asn": asn,
                "owner": owner,

                "last_analysis_date": last_analysis
            }

        # Return the error received from VirusTotal
        return {
            "error": response.json(),
            "status_code": response.status_code
        }

    except requests.exceptions.Timeout:
        return {
            "error": "Request timed out while connecting to VirusTotal."
        }

    except requests.exceptions.ConnectionError:
        return {
            "error": "Unable to connect to VirusTotal. Please check your internet connection."
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }