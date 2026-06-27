def analyze_threat(
    virustotal_score,
    abuseipdb_score,
    malicious,
    suspicious,
    reputation,
    ioc_type
):
    """
    ThreatLens Intelligence Engine

    Combines intelligence from multiple sources and returns
    ThreatLens's final assessment.
    """

    # ----------------------------
    # Calculate ThreatLens Score
    # ----------------------------

    if ioc_type == "ip":

        threatlens_score = round(
            (virustotal_score + abuseipdb_score) / 2
        )

    else:

        threatlens_score = virustotal_score

    # ----------------------------
    # Decide Status
    # ----------------------------

    if threatlens_score <= 20:

        status = "Safe"

    elif threatlens_score <= 50:

        status = "Low Risk"

    elif threatlens_score <= 80:

        status = "Suspicious"

    else:

        status = "Malicious"

    # ----------------------------
    # Confidence
    # ----------------------------

    confidence = 90

    if malicious > 5:
        confidence += 5

    if suspicious > 5:
        confidence += 3

    confidence = min(confidence, 100)

    # ----------------------------
    # Summary
    # ----------------------------

    if status == "Safe":

        summary = (
            "ThreatLens found no significant indicators of malicious activity."
        )

        recommendation = (
            "No immediate action is required. Continue routine monitoring."
        )

    elif status == "Low Risk":

        summary = (
            "Some low-risk indicators were detected. Additional verification is recommended."
        )

        recommendation = (
            "Monitor the IOC before allowing unrestricted access."
        )

    elif status == "Suspicious":

        summary = (
            "Multiple indicators suggest suspicious behavior."
        )

        recommendation = (
            "Investigate this IOC before trusting it."
        )

    else:

        summary = (
            "ThreatLens considers this IOC to be highly dangerous."
        )

        recommendation = (
            "Block this IOC immediately and investigate affected systems."
        )

    return {

        "status": status,

        "confidence": confidence,

        "threatlens_score": threatlens_score,

        "summary": summary,

        "recommendation": recommendation
    }