def map_to_mitre(ioc_type, status, threat_score):
    """
    ThreatLens MITRE ATT&CK Mapping Engine

    Maps detected threats to MITRE ATT&CK tactics
    and techniques based on IOC type and severity.
    """

    if status == "Safe":

        return {

            "mitre_tactics": None,

            "mitre_techniques": None

        }

    # -----------------------------
    # URL
    # -----------------------------

    if ioc_type == "url":

        if threat_score >= 80:

            return {

                "mitre_tactics": [

                    "Initial Access",

                    "Command and Control"

                ],

                "mitre_techniques": [

                    {
                        "id": "T1566",
                        "name": "Phishing"
                    },

                    {
                        "id": "T1071",
                        "name": "Application Layer Protocol"
                    }

                ]

            }

        return {

            "mitre_tactics": [

                "Initial Access"

            ],

            "mitre_techniques": [

                {
                    "id": "T1566",
                    "name": "Phishing"
                }

            ]

        }

    # -----------------------------
    # DOMAIN
    # -----------------------------

    elif ioc_type == "domain":

        return {

            "mitre_tactics": [

                "Command and Control"

            ],

            "mitre_techniques": [

                {
                    "id": "T1071",
                    "name": "Application Layer Protocol"
                }

            ]

        }

    # -----------------------------
    # IP
    # -----------------------------

    elif ioc_type == "ip":

        return {

            "mitre_tactics": [

                "Command and Control",

                "Reconnaissance"

            ],

            "mitre_techniques": [

                {
                    "id": "T1071",
                    "name": "Application Layer Protocol"
                },

                {
                    "id": "T1595",
                    "name": "Active Scanning"
                }

            ]

        }

    # -----------------------------
    # HASHES
    # -----------------------------

    elif ioc_type in ["md5", "sha1", "sha256"]:

        return {

            "mitre_tactics": [

                "Execution",

                "Defense Evasion"

            ],

            "mitre_techniques": [

                {
                    "id": "T1204",
                    "name": "User Execution"
                },

                {
                    "id": "T1027",
                    "name": "Obfuscated Files or Information"
                }

            ]

        }

    return {

        "mitre_tactics": None,

        "mitre_techniques": None

    }