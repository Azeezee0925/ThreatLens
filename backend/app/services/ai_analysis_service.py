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

    abuse_score = data.get("abuse_confidence_score")
    alien_score = data.get("alienvault_score")
    pulse_count = data.get("pulse_count", 0)

    status = data["status"]

    # ---------------------------------
    # Intelligence Sources Used
    # ---------------------------------

    sources = ["VirusTotal"]

    if abuse_score is not None:
        sources.append("AbuseIPDB")

    if alien_score is not None:
        sources.append("AlienVault OTX")

    if len(sources) == 1:
        source_text = sources[0]

    elif len(sources) == 2:
        source_text = f"{sources[0]} and {sources[1]}"

    else:
        source_text = ", ".join(sources[:-1]) + f" and {sources[-1]}"

    # ---------------------------------
    # Executive Summary
    # ---------------------------------

    summary = (
        f"The investigated {ioc_type.upper()} ({ioc}) was analyzed using "
        f"{source_text}. ThreatLens correlated the available threat intelligence "
        f"and calculated an overall threat score of {score}/100."
    )

    # ---------------------------------
    # Risk Assessment
    # ---------------------------------

    if status == "Safe":

        risk = (
            "Current threat intelligence indicates a low probability "
            "of malicious activity."
        )

    elif status == "Low Risk":

        risk = (
            "Some suspicious indicators were identified. Continued "
            "monitoring is recommended."
        )

    elif status == "Suspicious":

        risk = (
            "Multiple threat indicators suggest potentially malicious "
            "behavior requiring further investigation."
        )

    else:

        risk = (
            "Strong evidence from multiple threat intelligence sources "
            "indicates malicious activity."
        )

    # ---------------------------------
    # Key Findings
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
    # AI Recommendation
    # ---------------------------------

    if status == "Safe":

        recommendation = (
            "No immediate action is required. Continue routine monitoring."
        )

    elif status == "Low Risk":

        recommendation = (
            "Monitor this IOC closely and verify its legitimacy before allowing production use."
        )

    elif status == "Suspicious":

        recommendation = (
            "Investigate affected systems, review related logs, and monitor for further suspicious activity."
        )

    else:

        recommendation = (
            "Immediately block this IOC, isolate affected systems, initiate incident response procedures, "
            "and perform a forensic investigation."
        )

    return {

        "executive_summary": summary,

        "risk_assessment": risk,

        "key_findings": findings,

        "ai_recommendation": recommendation

    }