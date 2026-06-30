def analyze_threat(
    virustotal_score,
    abuseipdb_score,
    alienvault_score,
    malicious,
    suspicious,
    reputation,
    ioc_type
):
    """
    ThreatLens Intelligence Engine

    Combines VirusTotal, AbuseIPDB and AlienVault
    into one intelligent ThreatLens assessment.
    """

    # ----------------------------
    # Handle Missing Scores
    # ----------------------------

    if abuseipdb_score is None:
        abuseipdb_score = 0

    if alienvault_score is None:
        alienvault_score = 0

    # ----------------------------
    # ThreatLens Score V2
    # ----------------------------

    if ioc_type == "ip":

        threatlens_score = round(

            (virustotal_score * 0.5)

            +

            (abuseipdb_score * 0.3)

            +

            (alienvault_score * 0.2)

        )

    else:

        threatlens_score = round(

            (virustotal_score * 0.7)

            +

            (alienvault_score * 0.3)

        )

    # ----------------------------
    # Intelligent Threat Decision
    # ----------------------------

    # High confidence malicious overrides

    if virustotal_score >= 90 and malicious >= 10:

      status = "Malicious"

    elif abuseipdb_score >= 90:

      status = "Malicious"

    elif alienvault_score >= 80:

      status = "Malicious"

    # Normal ThreatLens score

    elif threatlens_score <= 20:

      status = "Safe"

    elif threatlens_score <= 50:

      status = "Low Risk"

    elif threatlens_score <= 80:

      status = "Suspicious"

    else:

      status = "Malicious"

    # ----------------------------
    # Confidence Score
    # ----------------------------

    confidence = 90

    if malicious > 5:
        confidence += 5

    if suspicious > 5:
        confidence += 3

    if reputation > 20:
        confidence += 2

    confidence = min(confidence, 100)

    # ----------------------------
    # Summary & Recommendation
    # ----------------------------

    if status == "Safe":

        summary = (
            "ThreatLens found no significant indicators of malicious activity across the analyzed intelligence sources."
        )

        recommendation = (
            "No immediate action is required. Continue routine monitoring."
        )

    elif status == "Low Risk":

        summary = (
            "ThreatLens detected a small number of low-risk indicators. The IOC should be monitored for any future changes."
        )

        recommendation = (
            "Monitor the IOC and allow access only if it is required."
        )

    elif status == "Suspicious":

        summary = (
            "ThreatLens identified multiple suspicious indicators from one or more threat intelligence sources."
        )

        recommendation = (
            "Investigate this IOC before trusting or allowing communication."
        )

    else:

        summary = (
            "ThreatLens considers this IOC highly malicious based on combined threat intelligence from multiple security sources."
        )

        recommendation = (
            "Immediately block this IOC, investigate affected systems, and initiate incident response procedures."
        )

    # ----------------------------
    # Final Result
    # ----------------------------

    return {

        "status": status,

        "confidence": confidence,

        "threatlens_score": threatlens_score,

        "summary": summary,

        "recommendation": recommendation

    }