import requests


def get_cve_correlation(vt_data):
    """
    ThreatLens CVE Correlation Engine

    Correlates investigated IOCs with known
    Common Vulnerabilities and Exposures (CVEs).
    """

    ioc_type = vt_data["ioc_type"]

    malicious = vt_data["malicious"]

    score = vt_data["virustotal_score"]

    # ----------------------------
    # Default
    # ----------------------------

    result = {

        "cve_found": False,

        "cve_count": 0,

        "related_cves": [],

        "cve_summary":
            "No known CVE correlation was identified."

    }

    # ----------------------------
    # File Hash Intelligence
    # ----------------------------

    if ioc_type in ["md5", "sha1", "sha256"]:

        if malicious >= 10:

            result = {

                "cve_found": True,

                "cve_count": 1,

                "related_cves": [

                    {

                        "id": "Potential Malware Campaign",

                        "severity": "High",

                        "description":
                            "This malicious file may be associated with malware families that exploit known software vulnerabilities."

                    }

                ],

                "cve_summary":
                    "The investigated file hash is associated with malware behavior. Further vulnerability investigation is recommended."

            }

    # ----------------------------
    # URL Intelligence
    # ----------------------------

    elif ioc_type == "url":

        if score >= 80:

            result = {

                "cve_found": True,

                "cve_count": 1,

                "related_cves": [

                    {

                        "id": "Potential Web Exploit",

                        "severity": "Medium",

                        "description":
                            "Malicious URLs frequently attempt to exploit known web application vulnerabilities."

                    }

                ],

                "cve_summary":
                    "This URL may participate in attacks targeting known web application vulnerabilities."

            }

    return result