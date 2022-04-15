from actor import Actor

class Event:
    """A coded event."""
    
    def __init__(self, id, date, 
        actor1_name, actor1_country_code, actor1_known_group_code, actor1_known_ethnic_code, actor1_religion_codes, actor1_type_codes,
        actor1_geo_type,
        actor2_name, actor2_country_code, actor2_known_group_code, actor2_known_ethnic_code, actor2_religion_codes, actor2_type_codes,
        action_country_codelat, long, feature_d):
        self.id = id
        self.date = date
        self.actor1 = Actor(actor1_name, actor1_country_code, actor1_known_group_code, actor1_known_ethnic_code,
            actor1_religion_codes, actor1_type_codes)
        self.actor2 = Actor(actor2_name, actor2_country_code, actor2_known_group_code, actor2_known_ethnic_code,
            actor2_religion_codes, actor2_type_codes)