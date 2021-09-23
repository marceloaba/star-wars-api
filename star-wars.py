"""
This program loads data from the Star Wars API to fulfil the following code challenge:
"given a partial or full vehicle name or model, return a list of vehicles with names of
pilots associated with that vehicle, plus a list of vehicle names with no associated pilot."

Author: Marcelo Monteiro da Silva
JobInterview: Net2Phone Canada
Date: 22/09/2021
Version: 1.0
"""

# import libraries
import json
from urllib.request import urlopen


# Star Wars API URL with vehicle route
url_vehicle_template = "https://swapi.dev/api/vehicles/?search={0}"


def load_data(url):
    """
    This function loads all data from the user and returns a json object
    :param url: URL from the API to load data
    :return: returns a json object
    """
    response = urlopen(url)
    result_json = json.loads(response.read())
    return result_json


def get_pilot_name(url):
    """
    This function loads the pilot name from the api url with pilot id
    :param url: from the pilot to load the name
    :return: a string with pilot's name
    """
    response = urlopen(url)
    result_json = json.loads(response.read())
    return result_json['name']


def get_vehicle_info(vehicle_name):
    """
    This function searches for Star Wars vehicles in the API and returns a json array with only the requested
    key/values such as, count, vehicle's name and pilots' name. It also organizes the dictionary into two groups,
    one with vehicles that has pilots name and other with vehicles without pilots name.
    with pilots and without pilots.
    :param vehicle_name: Name that will be used in the search for vehicles, it does not need to be exact
    :return: Returns a json object with all the keys and values.
    """
    # Uses the function to load data and format the URL appending the name to be searches using the API route
    # If the name of the vehicle have spaces between words, the space will be replaced by %20 to perform the GET method
    result_json = load_data(url_vehicle_template.format(vehicle_name.replace(" ", "%20")))
    # This dictionary will be populated with all necessary date and converted to json to be returned
    new_dict = {
                "count": result_json['count'],
                "with_pilots": [],
                "without_pilots": []
                }

    # list of relevant keys to be loaded from the API result
    relevant_key_list = ('name', 'pilots')
    # Counter used to loop through each key element
    count = 0
    # Loop through the results to pop the irrelevant keys from the dictionary
    for result in result_json['results']:
        all_keys = dict(result)
        for key in result_json['results'][count]:
            if key not in relevant_key_list:
                all_keys.pop(key)

        # If array pilot is not empty, add the pilot's name to the dictionary key 'with_pilots'
        if len(all_keys['pilots']) != 0:
            for pilot_name in all_keys['pilots']:
                # Get pilot's name from the pilot URL
                all_keys['pilots'] = get_pilot_name(pilot_name)
            new_dict['with_pilots'].append(all_keys)
        # If array pilot is empty, add name of the vehicles to the key 'with_pilots' and removes pilot's array
        else:
            all_keys.pop('pilots')
            new_dict['without_pilots'].append(all_keys['name'])
        # Increment the count by 1
        count += 1

    # Dumps the dictionary into json and print
    print(json.dumps(new_dict))


# Run the program
if __name__ == "__main__":
    # Search vehicles by name
    get_vehicle_info("Bike")
