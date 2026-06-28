def map_to_owasp(ioc_type, status, threat_score):
    """
    ThreatLens OWASP Top 10 Mapping Engine
    """

    if status == "Safe":

        return {
            "owasp_category": None,
            "owasp_description": None
        }

    # --------------------------
    # URL
    # --------------------------

    if ioc_type == "url":

        if threat_score >= 80:

            return {
                "owasp_category": [
                    "A03:2021 - Injection",
                    "A10:2021 - Server-Side Request Forgery (SSRF)"
                ],
                "owasp_description":
                    "Malicious URLs are commonly associated with injection attacks and server-side request forgery."
            }

        return {
            "owasp_category": [
                "A03:2021 - Injection"
            ],
            "owasp_description":
                "The URL exhibits suspicious behavior consistent with application-layer attacks."
        }

    # --------------------------
    # DOMAIN
    # --------------------------

    elif ioc_type == "domain":

        return {
            "owasp_category": [
                "A07:2021 - Identification and Authentication Failures"
            ],
            "owasp_description":
                "Malicious domains are frequently used for phishing and credential theft."
        }

    # --------------------------
    # IP
    # --------------------------

    elif ioc_type == "ip":

        return {
            "owasp_category": [
                "A07:2021 - Identification and Authentication Failures",
                "A05:2021 - Security Misconfiguration"
            ],
            "owasp_description":
                "Malicious IPs commonly participate in brute-force attacks, botnets and exploitation attempts."
        }

    # --------------------------
    # HASHES
    # --------------------------

    elif ioc_type in ["md5", "sha1", "sha256"]:

        return {
            "owasp_category": [
                "A06:2021 - Vulnerable and Outdated Components",
                "A05:2021 - Security Misconfiguration"
            ],
            "owasp_description":
                "Malicious files often exploit outdated software or insecure system configurations."
        }

    return {
        "owasp_category": None,
        "owasp_description": None
    }