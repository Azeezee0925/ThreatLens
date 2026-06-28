import os
import base64
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

if not API_KEY:
    raise ValueError("VirusTotal API Key not found.")


def investigate_ioc(ioc: str, ioc_type: str):

    # -------------------------
    # Build VirusTotal URL
    # -------------------------

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

    elif ioc_type in ["md5", "sha1", "sha256"]:

        url = f"https://www.virustotal.com/api/v3/files/{ioc}"

    else:

        return {
            "error": "Unsupported IOC type"
        }

    headers = {
        "x-apikey": API_KEY
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        if response.status_code != 200:

            return {
                "error": response.json(),
                "status_code": response.status_code
            }

        data = response.json()

        attributes = data["data"]["attributes"]

        analysis = attributes["last_analysis_stats"]

        malicious = analysis.get("malicious", 0)
        suspicious = analysis.get("suspicious", 0)
        harmless = analysis.get("harmless", 0)

        reputation = attributes.get(
            "reputation",
            0
        )

        country = attributes.get(
            "country",
            "Unknown"
        )

        asn = attributes.get(
            "asn",
            "Unknown"
        )

        owner = attributes.get(
            "as_owner",
            "Unknown"
        )

        timestamp = attributes.get(
            "last_analysis_date"
        )

        if timestamp:

            last_analysis = datetime.fromtimestamp(
                timestamp
            ).strftime("%Y-%m-%d %H:%M:%S UTC")

        else:

            last_analysis = "Unknown"

        virustotal_score = min(
            (malicious * 10) +
            (suspicious * 5),
            100
        )

        return {

            "ioc": ioc,

            "ioc_type": ioc_type,

            "virustotal_score": virustotal_score,

            "malicious": malicious,

            "suspicious": suspicious,

            "harmless": harmless,

            "reputation": reputation,

            "country": country,

            "asn": asn,

            "owner": owner,

            "last_analysis_date": last_analysis

        }

    except requests.exceptions.Timeout:

        return {
            "error": "VirusTotal timeout."
        }

    except requests.exceptions.ConnectionError:

        return {
            "error": "Unable to connect to VirusTotal."
        }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }