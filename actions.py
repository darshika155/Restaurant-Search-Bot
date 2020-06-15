from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from typing import Dict, Any, Union

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, UserUtteranceReverted, Restarted
import zomatopy
import itertools
import json
import smtplib

d_email_rest = []
from email.message import EmailMessage
import re


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f1850f4670dc87b33a2da56ff4786b48"}
        self.zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        location_detail = self.zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]
        cuisines_dict = {'american': 1, 'chinese': 25, 'mexican': 73, 'italian': 55, 'north indian': 50, 'south indian':85}
        response = self.zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)))

        d = json.loads(response)
        response = ""
        if d['results_found'] == 0:
            response = "no results"
        else:
            x = {}
            (lower, upper) = (0, 299.9) if price == "Lesser than Rs. 300" else (
                (300, 699.9) if price == "Rs. 300 to 700" else (
                    (700, 10000) if price == "More than 700" else (("Price range not specified!", 0))))
            if lower == "Price range not specified!":
                response = ""
            else:
                restaurant_budget = [restaurant_s for restaurant_s in d['restaurants'] if
                                     ((restaurant_s['restaurant']['average_cost_for_two'] > lower) and (
                                             restaurant_s['restaurant']['average_cost_for_two'] < upper))]
                # Sort the results according to the restaurant's rating
                restaurant_budget_rating_sorted = sorted(
                    restaurant_budget, key=lambda k: float(k['restaurant']['user_rating']['aggregate_rating']),
                    reverse=True)
                if len(restaurant_budget_rating_sorted) == 0:
                    response = "no results found try with some other price"
                else:
                    response = response + " Showing you top rated restaurants: \n"
                    restaurant_budget_rating_top5 = restaurant_budget_rating_sorted[:5]
                    global d_email_rest
                    d_email_rest = restaurant_budget_rating_sorted[:10]
                    count = 0
                    for restaurant in restaurant_budget_rating_top5:
                        count+=1
                        response = response + str(count) + ". " + restaurant['restaurant']['name'] + " in " + \
                                   restaurant['restaurant']['location']['address'] + " has been rated " + str(
                            restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n"

        if response == "":
            response = "no results"

        dispatcher.utter_message(response)
        return [SlotSet('location', loc), SlotSet('cuisine', cuisine)]


class ActionCitySearch(Action):
    def name(self):
        return 'action_city_search'

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "f1850f4670dc87b33a2da56ff4786b48"}
        self.zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        ret = self.check_city_validity(loc)
        if ret == 'Invalid City Name! Please enter another City' or ret == 'We do not operate in that area yet':
            dispatcher.utter_message(ret)
            return [UserUtteranceReverted()]
        else:
            return

    def check_city_validity(self, city_name=""):

        cities_map = {"kovai": "Coimbatore", "new delhi": "Delhi NCR", "cochin": "Kochi", "calcutta": "Kolkata",
                      "calicut": "Kozhikode", 'mangaluru': "Mangalore", "mysuru": "Mysore", "pataliputra": "Patna",
                      "pondicherry": "Puducherry", "tirupur": "Tiruppur", "benaras": "Varanasi", "banaras": "Varanasi",
                      "vizag": "Visakhapatnam", "bangalore": "Bengaluru", "chennai": "Chennai", "madras": "Chennai",
                      "Bombay": "mumbai", "Trivandrum": "thiruvananthapuram", "tiruchirapalli": "Trichy",
                      "Tiruchirapalli": "Trichy", "Bokaro Steel City": "Bokaro", "Bhilai": "Durg Bhilai",
                      "Purulia Prayagraj": "Purulia"}

        Cities = {"Ahmedabad": 11, "Bengaluru": 4, "Chennai": 7, "Delhi NCR": 1, "Hyderabad": 6, "Kolkata": 2,
                  "Mumbai": 3, "Pune": 5, "Agra": 34, "Ajmer": 11303, "Aligarh": 11379, "Amravati": 11335,
                  "Amritsar": 22,
                  "Asansol": 11423, "Aurangabad": 25, "Bareilly": 11343, "Belgaum": 11382, "Bhavnagar": 11384,
                  "Bhopal": 26,
                  "Bhubaneswar": 29, "Bikaner": 11346, "Bilaspur": 11325, "Bokaro": 11385, "Chandigarh": 12,
                  "Coimbatore": 30,
                  "Cuttack": 11289, "Dehradun": 35, "Dhanbad": 11387, "Durg Bhilai": 11345, "Durgapur": 11388,
                  "Erode": 11350,
                  "Firozabad": 11541, "Gorakhpur": 11311, "Gulbarga": 11403, "Guntur": 11339, "Gwalior": 11337,
                  "Guwahati": 21,
                  "Hamirpur": 11768, "Hubli": 11375, "Dharwad": 11374, "Indore": 14, "Jabalpur": 11336, "Jaipur": 10,
                  "Jalandhar": 11306,
                  "Jammu": 11307, "Jamnagar": 11321, "Jamshedpur": 11338, "Jhansi": 11352, "Jodhpur": 11301,
                  "Kakinada": 11401, "Kannur": 11772, "Kanpur": 23, "Kochi": 9, "Kolhapur": 11334, "Kollam": 11472,
                  "Kozhikode": 11296,
                  "Kurnool": 11391, "Ludhiana": 20, "Lucknow": 8, "Madurai": 11295, "Malappuram": 11775,
                  "Mathura": 11392, "Goa": 13, "Mangalore": 31, "Meerut": 11329, "Moradabad": 11393, "Mysore": 36,
                  "Nagpur": 33,
                  "Nanded": 11395, "Nashik": 16, "Nellore": 11396, "Patna": 40, "Puducherry": 37, "Purulia": 11859,
                  "Raipur": 11310,
                  "Rajkot": 11294, "Rajahmundry": 11402, "Ranchi": 27, "Rourkela": 11358, "Salem": 11331,
                  "Sangli": 11431,
                  "Shimla": 19, "Siliguri": 11327, "Solapur": 11397, "Srinagar": 11076, "Surat": 38,
                  "Thiruvananthapuram": 11290,
                  "Thrissur": 11298, "Trichy": 11332, "Tiruppur": 11368, "Ujjain": 11316, "Bijapur": 11480,
                  "Vadodara": 32,
                  "Varanasi": 39, "Vijayawada": 11300, "Visakhapatnam": 28, "Vellore": 11330, "Warangal": 11372}

        if city_name == None:
            return 'Invalid City Name! Please enter another City'

        if city_name.lower() in cities_map.keys():
            city_name = cities_map[city_name.lower()]
            return city_name
        else:
            if self.zomato.check_city_ID(city_name) == None:
                return 'Invalid City Name! Please enter another City'
            else:
                (id, name) = self.zomato.check_city_ID(city_name)
                if id not in Cities.values():
                    return 'We do not operate in that area yet'
                else:
                    return city_name


class ActionVerifyCuisine(Action):

    def name(self):
        return "action_verify_cuisine"

    def run(self, dispatcher, tracker, domain):
        cuisines = ['chinese', 'mexican', 'italian', 'american', 'south indian', 'north indian']
        error_msg = "Sorry!! The cuisine is not supported. Please re-enter."
        cuisine = tracker.get_slot('cuisine')
        try:
            cuisine = cuisine.lower()
        except (RuntimeError, TypeError, NameError, AttributeError):
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None)]
        if cuisine in cuisines:
            return
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('cuisine', None)]


class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')
        match = re.match(r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", to_email)
        if not match:
            dispatcher.utter_message("Email id not valid.. Please enter a valid email address! ")
            return [UserUtteranceReverted()]
        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global d_email_rest
        email_rest_count = len(d_email_rest)

        # Construct the email 'subject' and the contents.
        d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(
            loc).capitalize()

        if email_rest_count == 0:
            d_email_msg = "Hi there! \n \nSorry we couldn't find any restaurants in your search preferences!!"
        else:
            d_email_msg = "Hi there! \n \nHere are the " + d_email_subj + ":" + "\n" + "\n" + "\n"
            count = 0
            for restaurant in d_email_rest:
                count+=1
                d_email_msg = d_email_msg + str(count)+ ". "+ restaurant['restaurant']['name'] + " in " + \
                              restaurant['restaurant']['location']['address'] + " has been rated " + str(
                    restaurant['restaurant']['user_rating']['aggregate_rating']) + " and the average cost for two people : " + str(
                    restaurant['restaurant']['average_cost_for_two']) + "\n" + "\n"

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        # s = smtplib.SMTP('localhost')
        s.starttls()
        s.login("foodie.discover.restaurants@gmail.com", "Foodie!@#$")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "foodie.discover.restaurants@gmail.com"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
        return [Restarted()]


class ActionDontSendEmail(Action):
    def name(self):
        return "action_dont_send_mail"

    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        dispatcher.utter_message('Okay goodbye. Bon Appetit!')
        return [Restarted()]
