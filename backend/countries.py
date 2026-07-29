COUNTRY_CODES: dict[str, str] = {
    "norway": "no",
    "sweden": "se",
    "united kingdom": "gb",
    "netherland": "nl",
    "switzerland": "ch",
    "belgium": "be",
    "germany": "de",
    "austria": "at",
    "france": "fr",
    "italy": "it",
    "portugal": "pt",
    "spain": "es",
}


def get_country_code(country_name: str) -> str:
    country = country_name.lower()
    if country not in COUNTRY_CODES:
        raise ValueError(f"'{country_name}' is not a supported country yet.")
    return COUNTRY_CODES[country]
