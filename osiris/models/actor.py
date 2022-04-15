class Actor:
    """An individual or organization or state actor."""
    
    def __init__(self, name, country_code, known_group_code, known_ethnic_code,
        religion_codes:list, type_codes:list):
        self.name = name
        self.country_code = country_code
        self.known_group_code = known_group_code
        self.known_ethnic_code = known_ethnic_code
        self.religion_codes = religion_codes
        self.type_codes = type_codes
