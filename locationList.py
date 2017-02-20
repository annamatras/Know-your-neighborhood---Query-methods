from location import Location


class LocationList:
    """Create class container for locations objects"""
    locations = []

    @staticmethod
    def get_voivodeship():
        """Create voivodeship object"""
        return LocationList.locations[0].name

    @staticmethod
    def add_location(data):
        """Method add location object to locations list
        return:
               list of location objects
        """
        for item in data:
            location = Location(item[0], item[1], item[2], item[3], item[4], item[5])
            LocationList.locations.append(location)

    @staticmethod
    def list_statistics():
        """Method count objects by types and returns list
        return:
               list of all statistics
        """
        statistics = {}
        stats_listed = []
        for item in LocationList.locations:
            if item.type not in statistics:
                statistics[item.type] = 1
            else:
                statistics[item.type] += 1
            if item.type == "miasto na prawach powiatu":
                statistics["powiat"] += 1
        for key, value in statistics.items():
            stats_listed.append([str(value), key])
        return stats_listed

    @staticmethod
    def display_three_cities_with_longest_names():
        """Method count lenght of cities names and find longest
        return:
               list of cities with longest names
        """
        cities = []
        three_cities = []
        for item in LocationList.locations:
            if item.commune_type == "4":
                cities.append(item.name)
        cities = sorted(cities, key=lambda x: len(x), reverse=True)
        three_cities.append([cities[0], [cities[1]], [cities[2]]])
        # three_cities.append([cities[1]])
        # three_cities.append([cities[2]])
        return three_cities

    @staticmethod
    def display_county_name_with_most_communes():
        """Method count county with most types of communes
        return:
               list of county
        """
        counties = []
        for item in LocationList.locations:
            if item.commune == "" and not item.county == "":
                counties.append(item)
        amount = [-1] * len(counties)
        n = 0
        for county in counties:
            for item in LocationList.locations:
                if item.county == county.county and (item.commune_type == "1" or item.commune_type == "2"
                                                     or item.commune_type == "3" or item.commune_type == "4"
                                                     or item.commune_type == "5"):
                    amount[n] += 1
            n += 1
        county_and_commune_amount = []
        x = 0
        for item in counties:
            county_and_commune_amount.append([item.name, amount[x]])
            x += 1
        county_and_commune_amount = sorted(county_and_commune_amount, key=lambda i: i[1], reverse=True)
        county_and_commune_amount[0] = county_and_commune_amount[0][0], str(county_and_commune_amount[0][1])
        return [county_and_commune_amount[0]]

    @staticmethod
    def display_locations_within_more_than_one_category():
        """Method count locations with more then one type
        return:
               list of locations
        """
        name_and_commune = []
        for item in LocationList.locations:
            name_and_commune.append([item.name, item.commune])
        every = []
        repeating = []
        for item in name_and_commune:
            if item in every:
                repeating.append(item)
            else:
                every.append(item)
        one_from_repeating = []
        for data in repeating:
            if data not in one_from_repeating:
                one_from_repeating.append(data)
        to_display_in_table = []
        n = 1
        for stuff in one_from_repeating:
            to_display_in_table.append([str(n), stuff[0]])
            n += 1
        return to_display_in_table

    @staticmethod
    def advanced_search():
        """Method allows user searching list by phrase
        return:
               list of location with searching phrase
        """
        search_list = []
        search = input("Name location: ")
        search = search.lower()
        for item in LocationList.locations:
            if search in item.name:
                search_list.append([item.name, item.type])
            elif search.title() in item.name:
                search_list.append([item.name, item.type])
        search_list = sorted(search_list, key=lambda x: x[0].lower())
        return search_list


