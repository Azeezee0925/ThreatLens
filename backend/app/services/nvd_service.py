import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NVD_API_KEY")

BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"


def search_cves(keyword: str):

    headers = {
        "apiKey": API_KEY
    }

    params = {
        "keywordSearch": keyword,
        "resultsPerPage": 5
    }

    try:

        response = requests.get(
            BASE_URL,
            headers=headers,
            params=params,
            timeout=20
        )

        if response.status_code != 200:

            return {
                "error": response.text
            }

        data = response.json()

        vulnerabilities = data.get(
            "vulnerabilities",
            []
        )

        cves = []

        for item in vulnerabilities:

            cve = item["cve"]

            cve_id = cve["id"]

            description = cve["descriptions"][0]["value"]

            published = cve["published"]

            severity = "Unknown"
            cvss = None

            metrics = cve.get("metrics", {})

            if "cvssMetricV31" in metrics:

                metric = metrics["cvssMetricV31"][0]

                severity = metric["cvssData"]["baseSeverity"]

                cvss = metric["cvssData"]["baseScore"]

            elif "cvssMetricV30" in metrics:

                metric = metrics["cvssMetricV30"][0]

                severity = metric["cvssData"]["baseSeverity"]

                cvss = metric["cvssData"]["baseScore"]

            elif "cvssMetricV2" in metrics:

                metric = metrics["cvssMetricV2"][0]

                severity = metric["baseSeverity"]

                cvss = metric["cvssData"]["baseScore"]

            cves.append({

                "id": cve_id,

                "severity": severity,

                "cvss": cvss,

                "published": published,

                "description": description,

                "url": f"https://nvd.nist.gov/vuln/detail/{cve_id}"

            })

        return {

            "cve_found": len(cves) > 0,

            "cve_count": len(cves),

            "related_cves": cves

        }

    except Exception as e:

        return {

            "error": str(e)

        }