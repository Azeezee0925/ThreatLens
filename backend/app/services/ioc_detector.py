import ipaddress
import re


def detect_ioc_type(ioc: str):

    ioc = ioc.strip()

    # ------------------------
    # IPv4 Address
    # ------------------------
    try:
        ipaddress.ip_address(ioc)
        return "ip"
    except ValueError:
        pass

    # ------------------------
    # URL
    # ------------------------
    if ioc.startswith("http://") or ioc.startswith("https://"):
        return "url"

    # ------------------------
    # MD5
    # ------------------------
    if re.fullmatch(r"[A-Fa-f0-9]{32}", ioc):
        return "md5"

    # ------------------------
    # SHA1
    # ------------------------
    if re.fullmatch(r"[A-Fa-f0-9]{40}", ioc):
        return "sha1"

    # ------------------------
    # SHA256
    # ------------------------
    if re.fullmatch(r"[A-Fa-f0-9]{64}", ioc):
        return "sha256"

    # ------------------------
    # Domain
    # ------------------------
    domain_pattern = (
        r"^(?!:\/\/)"
        r"[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$"
    )

    if re.fullmatch(domain_pattern, ioc):
        return "domain"

    return None