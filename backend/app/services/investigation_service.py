from app.services.ioc_detector import detect_ioc_type
from app.services.virustotal_service import investigate_ioc
from app.services.abuseipdb_service import get_abuseipdb_data
from app.services.alienvault_service import get_alienvault_data
from app.services.ThreatLens_engine import analyze_threat
from app.services.ai_analysis_service import generate_ai_analysis
from app.services.owasp_mapper import map_to_owasp
from app.services.knowledge_engine import extract_search_keyword
from app.services.nvd_service import search_cves
from app.services.mitre_mapper import map_to_mitre
from app.database.database import SessionLocal
from app.database.crud import save_investigation
from app.database.alert_crud import save_alert


def investigate(ioc: str):

    # -----------------------------
    # Detect IOC Type
    # -----------------------------
    ioc_type = detect_ioc_type(ioc)

    if not ioc_type:
        return {
            "error": "Unsupported IOC type."
        }

    # -----------------------------
    # VirusTotal
    # -----------------------------
    vt_data = investigate_ioc(ioc, ioc_type)

    if "error" in vt_data:
        return vt_data

    # -----------------------------
    # AbuseIPDB
    # -----------------------------
    if ioc_type == "ip":

        abuse_data = get_abuseipdb_data(ioc)

        abuse_score = abuse_data.get(
            "abuse_confidence_score",
            0
        )

    else:

        abuse_data = {}

        abuse_score = None

    # -----------------------------
    # AlienVault
    # -----------------------------
    alien_data = get_alienvault_data(
        ioc,
        ioc_type
    )

    if "error" in alien_data:

        alien_data = {

            "alienvault_score": 0,
            "pulse_count": 0,
            "reputation": 0,
            "country": None

        }

    # -----------------------------
    # ThreatLens AI Engine
    # -----------------------------
    threat = analyze_threat(

        virustotal_score=vt_data["virustotal_score"],

        abuseipdb_score=abuse_score,

        alienvault_score=alien_data["alienvault_score"],

        malicious=vt_data["malicious"],

        suspicious=vt_data["suspicious"],

        reputation=vt_data["reputation"],

        ioc_type=ioc_type

    )

    # -----------------------------
    # CVE Correlation
    # -----------------------------
    keyword = extract_search_keyword(vt_data)

    if keyword:

        print(f"\nThreatLens Keyword -> {keyword}\n")

        cve_data = search_cves(keyword)

    else:

        cve_data = {

            "cve_found": False,
            "cve_count": 0,
            "related_cves": []

        }

    # -----------------------------
    # Build Response
    # -----------------------------
    response = {

        **vt_data,

        **threat,

        **alien_data,

        **cve_data

    }

    if abuse_data:

        response.update(abuse_data)

    # -----------------------------
    # AI Analysis
    # -----------------------------
    ai_analysis = generate_ai_analysis(response)

    response.update(ai_analysis)

    # -----------------------------
    # OWASP Mapping
    # -----------------------------
    owasp = map_to_owasp(

        ioc_type=ioc_type,

        status=response["status"],

        threat_score=response["threatlens_score"]

    )

    response.update(owasp)
    
    # -----------------------------
    # MITRE ATT&CK Mapping
    # -----------------------------

    mitre = map_to_mitre(

      ioc_type=ioc_type,

      status=response["status"],

      threat_score=response["threatlens_score"]

    )

    response.update(mitre)

    # -----------------------------
    # Remove Internal Data
    # -----------------------------
    response.pop("raw_attributes", None)

    # -----------------------------
    # Save Investigation
    # -----------------------------
    db = SessionLocal()

    try:

     save_investigation(

        db,

        response

    )

    finally:

      db.close()
      
    # -----------------------------
    # Save Alert (High Risk Only)
    # -----------------------------
    if response["threatlens_score"] >= 80:

     save_alert(

        db,

        response

    )

    # -----------------------------
    # Return Final Response
    # -----------------------------
    return response