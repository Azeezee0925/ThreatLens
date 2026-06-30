def extract_search_keyword(vt_data):
    """
    ThreatLens Knowledge Engine

    Extracts the best keyword from VirusTotal metadata
    for CVE correlation.
    """

    # -------------------------
    # Get VirusTotal attributes
    # -------------------------

    attributes = vt_data.get("raw_attributes", {})

    classification = attributes.get(
        "popular_threat_classification",
        {}
    )

    # -------------------------
    # 1. Malware Family
    # -------------------------

    names = classification.get(
        "popular_threat_name",
        []
    )

    if names:

        keyword = names[0]["value"]

        return keyword

    # -------------------------
    # 2. Malware Category
    # -------------------------

    categories = classification.get(
        "popular_threat_category",
        []
    )

    if categories:

        keyword = categories[0]["value"]

        return keyword

    # -------------------------
    # 3. Executable Name
    # -------------------------

    file_names = attributes.get(
        "names",
        []
    )

    if file_names:

        return file_names[0]

    # -------------------------
    # 4. File Type
    # -------------------------

    description = attributes.get(
        "type_description"
    )

    if description:

        return description

    # -------------------------
    # Nothing Found
    # -------------------------

    return None