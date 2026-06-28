import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALIENVAULT_API_KEY")

if not API_KEY:
    raise ValueError("AlienVault API Key not found.")


def get_alienvault_data(ioc: str, ioc_type: str):

    # -------------------------
    # Build AlienVault URL
    # -------------------------

    if ioc_type == "ip":

        url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ioc}/general"

    elif ioc_type == "domain":

        url = f"https://otx.alienvault.com/api/v1/indicators/domain/{ioc}/general"

    elif ioc_type == "url":

        encoded_url = (
            base64.b64encode(
                ioc.encode()
            )
            .decode()
        )

        url = f"https://otx.alienvault.com/api/v1/indicators/url/{encoded_url}/general"

    elif ioc_type in ["md5", "sha1", "sha256"]:

        url = f"https://otx.alienvault.com/api/v1/indicators/file/{ioc}/general"

    else:

        return {
            "error": "Unsupported IOC type"
        }

    # -------------------------
    # Headers
    # -------------------------

    headers = {
        "X-OTX-API-KEY": API_KEY,
        "Accept": "application/json"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:

            return {
                "alienvault_score": 0,
                "pulse_count": 0,
                "reputation": 0,
                "country": None
            }

        data = response.json()

        # -------------------------
        # Extract Data
        # -------------------------

        pulse_info = data.get(
            "pulse_info",
            {}
        )

        pulse_count = pulse_info.get(
            "count",
            0
        )

        reputation = data.get(
            "reputation",
            0
        )

        geo = data.get(
            "geo",
            {}
        )

        country = geo.get(
            "country_name",
            None
        )

        # -------------------------
        # Calculate AlienVault Score
        # -------------------------

        alienvault_score = min(
            pulse_count * 10,
            100
        )

        # -------------------------
        # Return Clean Data
        # -------------------------

        return {

            "alienvault_score": alienvault_score,

            "pulse_count": pulse_count,

            "reputation": reputation,

            "country": country

        }

    except requests.exceptions.Timeout:

        return {
            "error": "AlienVault timeout."
        }

    except requests.exceptions.ConnectionError:

        return {
            "error": "Unable to connect to AlienVault."
        }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }