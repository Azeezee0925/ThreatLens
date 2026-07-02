def analyze_threat(
    virustotal_score,
    abuseipdb_score,
    alienvault_score,
    malicious,
    suspicious,
    reputation,
    ioc_type
):

    if abuseipdb_score is None:
        abuseipdb_score = 0

    if alienvault_score is None:
        alienvault_score = 0

    # ----------------------------
    # Weighted ThreatLens Score
    # ----------------------------

    if ioc_type == "ip":

        threatlens_score = round(
            (virustotal_score * 0.50) +
            (abuseipdb_score * 0.30) +
            (alienvault_score * 0.20)
        )

    else:

        threatlens_score = round(
            (virustotal_score * 0.80) +
            (alienvault_score * 0.20)
        )

    # ----------------------------
    # Intelligent Threat Decision
    # ----------------------------

    # VirusTotal always has highest priority
    if malicious >= 5 or virustotal_score >= 80:

        status = "Malicious"

    elif malicious >= 1 or suspicious >= 5:

        status = "Suspicious"

    elif abuseipdb_score >= 75:

        status = "Suspicious"

    # AlienVault alone should NEVER make a trusted domain malicious
    elif alienvault_score >= 80 and virustotal_score > 20:

        status = "Low Risk"

    elif threatlens_score <= 20:

        status = "Safe"

    elif threatlens_score <= 40:

        status = "Low Risk"

    elif threatlens_score <= 70:

        status = "Suspicious"

    else:

        status = "Malicious"

    # ----------------------------
    # Confidence
    # ----------------------------

    confidence = 85

    if malicious > 0:
        confidence += 8

    if suspicious > 0:
        confidence += 4

    if virustotal_score > 0:
        confidence += 3

    confidence = min(confidence, 100)

    # ----------------------------
    # Summary
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
            "ThreatLens detected minor indicators requiring observation, but no strong evidence of malicious activity."
        )

        recommendation = (
            "Continue monitoring and investigate only if additional indicators appear."
        )

    elif status == "Suspicious":

        summary = (
            "ThreatLens detected multiple suspicious indicators that should be investigated before trusting this IOC."
        )

        recommendation = (
            "Investigate this IOC before allowing communication."
        )

    else:

        summary = (
            "ThreatLens found strong evidence indicating malicious activity across multiple intelligence sources."
        )

        recommendation = (
            "Immediately block this IOC and begin incident response procedures."
        )

    return {

        "status": status,

        "confidence": confidence,

        "threatlens_score": threatlens_score,

        "summary": summary,

        "recommendation": recommendation

    }