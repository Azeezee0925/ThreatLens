# threat_service.py
import os
import base64
import requests
from datetime import datetime
from dotenv import load_dotenv
from app.services.abuseipdb_service import get_abuseipdb_data

load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

if not API_KEY:
    raise ValueError("VirusTotal API Key not found.")


def investigate_ioc(ioc: str, ioc_type: str):

    if ioc_type == "ip":
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}"

    elif ioc_type == "domain":
        url = f"https://www.virustotal.com/api/v3/domains/{ioc}"

    elif ioc_type == "url":
        url_id = base64.urlsafe_b64encode(ioc.encode()).decode().strip("=")
        url = f"https://www.virustotal.com/api/v3/urls/{url_id}"

    else:
        return {"error": "Unsupported IOC type"}

    headers = {
        "x-apikey": API_KEY
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        if response.status_code == 200:

            data = response.json()
            attributes = data["data"]["attributes"]
            analysis = attributes["last_analysis_stats"]

            malicious = analysis["malicious"]
            suspicious = analysis["suspicious"]
            harmless = analysis["harmless"]

            reputation = attributes.get("reputation", 0)
            country = attributes.get("country", "Unknown")
            asn = attributes.get("asn", "Unknown")
            owner = attributes.get("as_owner", "Unknown")

            timestamp = attributes.get("last_analysis_date")

            if timestamp:
                last_analysis = datetime.fromtimestamp(
                    timestamp
                ).strftime("%Y-%m-%d %H:%M:%S UTC")
            else:
                last_analysis = "Unknown"

            virustotal_score = min(
                (malicious * 10) + (suspicious * 5),
                100
            )

            if malicious > 0:
                summary = (
                    "This IOC has been flagged as malicious by security vendors. "
                    "It is recommended to avoid interacting with this resource."
                )
            elif suspicious > 0:
                summary = (
                    "This IOC has been marked as suspicious by security vendors. "
                    "Exercise caution and perform additional verification before trusting this resource."
                )
            else:
                summary = (
                    "This IOC appears safe based on current VirusTotal analysis. "
                    "No malicious or suspicious detections were reported by security vendors."
                )

            if ioc_type == "ip":
                abuse_data = get_abuseipdb_data(ioc)
                abuseipdb_score = abuse_data["abuse_confidence_score"]
                threatlens_score = round(
                    (virustotal_score + abuseipdb_score) / 2
                )
            else:
                abuse_data = None
                abuseipdb_score = None
                threatlens_score = virustotal_score

            if threatlens_score <= 20:
                status = "Safe"
            elif threatlens_score <= 50:
                status = "Low Risk"
            elif threatlens_score <= 80:
                status = "Suspicious"
            else:
                status = "Malicious"

            response_data = {
                "ioc": ioc,
                "ioc_type": ioc_type,

                "status": status,
                "virustotal_score": virustotal_score,
                "abuseipdb_score": abuseipdb_score,
                "threatlens_score": threatlens_score,
                "summary": summary,

                "malicious": malicious,
                "suspicious": suspicious,
                "harmless": harmless,

                "reputation": reputation,
                "country": country,
                "asn": asn,
                "owner": owner,
                "last_analysis_date": last_analysis
            }

            if abuse_data:
                response_data.update({
                    "abuse_confidence_score": abuse_data["abuse_confidence_score"],
                    "total_reports": abuse_data["total_reports"],
                    "country_code": abuse_data["country_code"],
                    "isp": abuse_data["isp"],
                    "domain": abuse_data["domain"]
                })

            return response_data

        return {
            "error": response.json(),
            "status_code": response.status_code
        }

    except requests.exceptions.Timeout:
        return {"error": "Request timed out while connecting to VirusTotal."}

    except requests.exceptions.ConnectionError:
        return {"error": "Unable to connect to VirusTotal. Please check your internet connection."}

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
