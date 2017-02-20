from location import Location


class LocationList:
    """
    IClass using for aggregating the instances of class Location.
    """
    list_of_locations = []

    def add_location(self, location):
        """
        The method to append to the class attribute "list_of_locations" instances of the "Location" class.
        """
        self.list_of_locations.append(location)

    def voivodeship_name(self):
        """
        The method to finding the name of a current VOIVODESHIP in the CSV file.
        Returns:
            string
        """

        for location in self.list_of_locations:
            if location.voivodeship_id != "" and location.county_id == "":
                name_of_the_voivodeship = location.name.upper()
                return name_of_the_voivodeship

    def list_statistics(self):
        """
        The method to count the occurrences of the specific types of locations
        Returns:
            integer
        """


    for location in self.list_of_locations:
        if location.voivodeship_id != "" and location.county_id == "":
            number_of_voivodeships += 1
            voivodeship_name = location.type
        if location.county_id != "":
            number_of_different_counties.add(location.county_id)
            different_counties_name = "powiaty*"
        if location.community_type_id == "1":
            number_of_urban_communities += 1
            urban_community_name = location.type
        if location.community_type_id == "2":
            number_of_rural_communities += 1
            rural_community_name = location.type
        if location.community_type_id == "3":
            number_of_urban_rural_communities += 1
            urban_rural_community_name = location.type
        if location.community_type_id == "5":
            number_of_villages += 1
            village_name = location.type
        if location.community_type_id == "4":
            number_of_towns += 1
            town_name = location.type
        if type_of_location == "miasto na prawach powiatu":
            number_of_cities += 1
            city_name = location.type
        if location.community_type_id == "9":
            number_of_delegatures += 1
            delegature_name = location.type


        number_of_all_locations = (number_of_voivodeships + len(number_of_different_counties) + number_of_urban_communities +
        number_of_rural_communities + number_of_urban_rural_communities + number_of_villages +
        number_of_towns + number_of_delegatures)

        dict_voivodeships = {voivodeship_name: number_of_voivodeships}
        dict_different_counties = {different_counties_name: len(number_of_different_counties)}
        dict_urban_communities = {urban_community_name: number_of_urban_communities}
        dict_rural_communities = {rural_community_name: number_of_rural_communities}
        dict_urban_rural_communities = {urban_rural_community_name: number_of_urban_rural_communities}
        dict_villages = {village_name: number_of_villages}
        dict_towns = {town_name: number_of_towns}
        dict_cities = {city_name: number_of_cities}
        dict_delegatures = {delegature_name: number_of_delegatures}

        # NOTE: Stack the dictionaries all together in a tuple.
        tuple_of_all_dictionaries = (dict_voivodeships, dict_different_counties, dict_urban_communities, dict_rural_communities,
        dict_urban_rural_communities, dict_villages, dict_towns, dict_cities, dict_delegatures)

        # NOTE: Save the values and keys from all of the dictionaries in the dedicated list.
        all_locations_items = []

    for one_dictionary in tuple_of_all_dictionaries:
        for key, value in one_dictionary.items():
        # Add collection of string-type items as tuple to the list of tuples "all_locations_items".
            all_locations_items.extend([(str(value), key)])
        return (number_of_all_locations, all_locations_items)


    def city_with_longest_name(self):
        """
        The method to count the name length of all the CITIES from
        the database and get the longest name (by default: top 3).

        Returns:
        list of tuples (with strings)
        """

    all_locations_names_dictionaries = []

        for location in self.list_of_locations:
            if location.community_type_id == "4":
        name_length = len(location.name)
        name = location.name
        # Make a dictionaries with the "name" and "name_length" of the current location as the VALUES.
        dict_location_name = {"Name": name, "Name length": name_length}
        all_locations_names_dictionaries.append(dict_location_name)

    # NOTE: Sort the gained dictionaries in DESCENDING ORDER by their keys ("Name length").
        sorted_list = sorted(all_locations_names_dictionaries, key=operator.itemgetter("Name length"), reverse=True)

    # NOTE: Get the first three longest names from the list (with the number of characters: letters, spaces and "-").
        longest_names = []
        for number, location in enumerate(sorted_list, 1):
            # Count only the top 3 longest city names.
            if number < 4:
            # Add values of the following keys as a tuple to the list of tuples "the_longest_names".
            longest_names.extend([(location.get("Name"), location.get("Name length"))])
        return longest_names


    def largest_county(self):
        """
        The method to find the county names with
        the largest number of communities in it.

        Returns:
        list with tuple (with strings)
        """
    # NOTE: Create the list which contains the dictionaries of all counties from the CSV file.
    list_of_all_counties_dict = []

        for location in self.list_of_locations:
        # Take into consideration only the following location types: "County" and "City with county rights".
        if location.county_id != "" and location.community_id == "":
        # Create the dictionary for the current county based on its "county_id" and "name" as VALUES.
        list_of_all_counties_dict.append({"ID": location.county_id, "Name": location.name, "Communities": 0}) # Set the counter to 0.

        # NOTE: Count the number of individual communities of any type in the all following counties.
        for county_dict in list_of_all_counties_dict:
        # Count the occurances of any communities for the current county.
        any_type_of_community_in_county = []
        for location in self.list_of_locations:
        # Match the "ID" of the current county from "list_of_all_counties_dict" to the "county_id" of the communities in "list_of_locations".
        if location.county_id == county_dict.get("ID"):
        # Take into consideration any type of the following communities: "Urban" (1), "Rural" (2) and "Urban-Rural" (3).
        if location.community_type_id in ("1", "2", "3"):
        any_type_of_community_in_county.append(location) # Count the found communities as the objects.

        # Update the default number (0) of "Communities" for the current county by calculated number of all communities in it.
        county_dict["Communities"] += len(any_type_of_community_in_county)

        # NOTE: Get the dictionary with the largest amount of the "Communities" in it from the "list_of_all_counties_dict".
        the_largest_county = max(list_of_all_counties_dict, key=operator.itemgetter("Communities"))

        # NOTE: Return only the specific VALUES of the largest county: its "Name" and number of "Communities".
        final_county_data = []
        final_county_data.extend([("powiat {}".format(the_largest_county.get("Name")), the_largest_county.get("Communities"))])

            return final_county_data


        def locations_of_multiple_types(self):
            """
            The method to find the location names which are occurring more than once
            (which automatically means that they represents many types of locations).

            Returns:
            list of tuples (with strings)
            """
        # NOTE: Get the names of all locations from the CSV file.
        list_of_any_occurrences = []

        for location in self.list_of_locations:
            list_of_any_occurrences.append(location.name)

        # NOTE: Get the names of locations which are occurring more than once.
        list_of_multiple_occurrences = []

        for name in set(list_of_any_occurrences):
            occurrence = list_of_any_occurrences.count(name)
            location_dict = ({"Name": name, "Occurrence": occurrence})
            if location_dict.get("Occurrence") > 1:
                list_of_multiple_occurrences_dict.append({"Name": name, "Occurrence": occurrence})

        # NOTE: Sort the list of dictionaries twice: (1st) by DESCENDING ORDER for the "Occurrence" and (2nd) by ASCENDING ORDER for the "Name".
        multi_dict_list = list_of_multiple_occurrences_dict # Shorten the (already) unnecessarily long name.
        double_sorted_list = sorted(multi_dict_list, key=lambda multi_dict_list: (-multi_dict_list["Occurrence"], multi_dict_list["Name"].lower()))

        final_multiple_data = []
        for dictionary in double_sorted_list:
            final_multiple_data.append((dictionary.get("Name"), dictionary.get("Occurrence")))
        return final_multiple_data

        def advanced_search(self, searched_phrase):
            """
            The method to find the substring (from input) among
            the list of all location names from the CSV file.

            Returns:
            list of tuples (with strings)
            """
        found_name = []
        for location in self.list_of_locations:
            if searched_phrase in location.name.lower():
                found_name.append({"Name": location.name, "Type": location.type})

        double_sorted_list = sorted(found_name, key=lambda found_name: (found_name["Name"].lower(), found_name["Type"].lower()))

        found_data = []
        for dictionary in double_sorted_list:
            found_data.append((dictionary.get("Name"), dictionary.get("Type")))
        return found_data


