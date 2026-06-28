def generate_ai_analysis(data):
    """
    ThreatLens AI Analysis Engine

    Generates an intelligent threat summary,
    risk assessment and remediation guidance.
    """

    score = data["threatlens_score"]
    ioc = data["ioc"]
    ioc_type = data["ioc_type"]

    malicious = data["malicious"]
    suspicious = data["suspicious"]

    vt_score = data["virustotal_score"]

    abuse_score = data.get("abuse_confidence_score", 0) or 0

    alien_score = data.get("alienvault_score", 0) or 0

    pulse_count = data.get("pulse_count", 0) or 0

    status = data["status"]

    # ---------------------------------
    # Executive Summary
    # ---------------------------------

    summary = (
        f"The investigated {ioc_type} ({ioc}) "
        f"was analyzed using VirusTotal, AbuseIPDB "
        f"and AlienVault OTX. "
        f"ThreatLens calculated an overall threat "
        f"score of {score}/100."
    )

    # ---------------------------------
    # Risk Assessment
    # ---------------------------------

    if status == "Safe":

        risk = (
            "Current threat intelligence indicates a low "
            "probability of malicious activity."
        )

    elif status == "Low Risk":

        risk = (
            "Some suspicious indicators were identified. "
            "Continued monitoring is recommended."
        )

    elif status == "Suspicious":

        risk = (
            "Multiple threat indicators suggest potentially "
            "malicious behavior requiring investigation."
        )

    else:

        risk = (
            "Strong evidence from multiple intelligence "
            "sources indicates malicious activity."
        )

    # ---------------------------------
    # Intelligence Findings
    # ---------------------------------

    findings = []

    findings.append(
        f"VirusTotal Score: {vt_score}/100"
    )

    findings.append(
        f"Malicious Vendors: {malicious}"
    )

    findings.append(
        f"Suspicious Vendors: {suspicious}"
    )

    if abuse_score is not None:

        findings.append(
            f"AbuseIPDB Score: {abuse_score}/100"
        )

    if alien_score is not None:

        findings.append(
            f"AlienVault Score: {alien_score}/100"
        )

    if pulse_count:

        findings.append(
            f"AlienVault Threat Pulses: {pulse_count}"
        )

    # ---------------------------------
    # Remediation
    # ---------------------------------

    if status == "Safe":

        recommendation = (
            "No immediate action is required. "
            "Continue routine monitoring."
        )

    elif status == "Low Risk":

        recommendation = (
            "Monitor this IOC and verify before allowing "
            "production use."
        )

    elif status == "Suspicious":

        recommendation = (
            "Investigate affected systems, collect logs, "
            "and verify related activity."
        )

    else:

        recommendation = (
            "Immediately block this IOC, isolate affected "
            "systems, initiate incident response and "
            "perform forensic analysis."
        )

    return {

        "executive_summary": summary,

        "risk_assessment": risk,

        "key_findings": findings,

        "ai_recommendation": recommendation

    }