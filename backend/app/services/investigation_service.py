from app.services.ioc_detector import detect_ioc_type
from app.services.virustotal_service import investigate_ioc
from app.services.abuseipdb_service import get_abuseipdb_data
from app.services.alienvault_service import get_alienvault_data
from app.services.threatlens_engine import analyze_threat
from app.services.ai_analysis_service import generate_ai_analysis


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
    # Final Response
    # -----------------------------
    response = {

    **vt_data,

    **threat,

    **alien_data

    }

    if abuse_data:

       response.update(abuse_data)

# -----------------------------
# ThreatLens AI Analysis
# -----------------------------

    ai_analysis = generate_ai_analysis(response)

    response.update(ai_analysis)

    return response