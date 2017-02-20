
class Location:

    def __init__(self, voivodeship, county, commune, commune_type, name, types):
        """Class creates location objects"""
        self.voivodeship = voivodeship
        self.county = county
        self.commune = commune
        self.commune_type = commune_type
        self.name = name
        self.type = types
