import json
from nose.tools import raises
import responses
import requests
import unittest

import uinames
import uinames.models as models
import uinames.utils as utils


class APIFunctionality(unittest.TestCase):
    """
    This testcase tests the end-to-end functionality of the library, ensuring
    that the correct exceptions are thrown for erroneous inputs, and that
    the correct class instances are being returned for successful inputs.
    """

    def test_generate_random_identity(self):
        person = uinames.generate_random_identity()
        self.assertEqual(person.__class__, models.Person)

    def test_generate_random_identities(self):
        people = uinames.generate_random_identities()
        self.assertEqual(people.__class__, models.People)

    # amount parameter

    @raises(requests.exceptions.HTTPError)
    def test_amount_lower_out_of_bound(self):
        uinames.generate_random_identities(0)

    def test_amount_lower_bound(self):
        people = uinames.generate_random_identities(1)
        self.assertEqual(people.__class__, models.People)

    def test_amount_within_bounds(self):
        people = uinames.generate_random_identities(250)
        self.assertEqual(people.__class__, models.People)

    def test_amount_upper_bounds(self):
        people = uinames.generate_random_identities(500)
        self.assertEqual(people.__class__, models.People)

    @raises(requests.exceptions.HTTPError)
    def test_amount_upper_out_of_bound(self):
        uinames.generate_random_identities(501)

    # gender parameter

    def test_gender_male(self):
        person = uinames.generate_random_identities(gender="male")
        self.assertEqual(person.__class__, models.People)

    def test_gender_female(self):
        person = uinames.generate_random_identities(gender="female")
        self.assertEqual(person.__class__, models.People)

    @raises(requests.exceptions.HTTPError)
    def test_gender_invalid(self):
        uinames.generate_random_identities(gender="invalid_gender")

    # region parameter

    def test_region_valid(self):
        person = uinames.generate_random_identities(region="canada")
        self.assertEqual(person.__class__, models.People)

    @raises(requests.exceptions.HTTPError)
    def test_region_invalid(self):
        uinames.generate_random_identities(region="invalid-region")

    # minlen parameter

    def test_minlen_valid(self):
        person = uinames.generate_random_identities(minlen=10)
        self.assertEqual(person.__class__, models.People)

    # maxlen parameter

    def test_maxlen_valid(self):
        person = uinames.generate_random_identities(maxlen=10)
        self.assertEqual(person.__class__, models.People)

    # ext parameter

    def test_ext(self):
        person = uinames.generate_random_identities(ext=True)
        self.assertEqual(person.__class__, models.People)


class BasicWrapperFunctionality(unittest.TestCase):
    """
    This testcase tests the functionality of the generate_random_identity
    function.
    """

    @responses.activate
    def setUp(self):
        url = "https://uinames.com/api/"
        data = json.load(open("tests/fixtures/person.json"))
        response = responses.add(responses.GET, url, json=data, status=200,
                                 content_type="application/json")
        self.person = uinames.generate_random_identity()
        # basic assertions
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, url)

    def test_name(self):
        self.assertEqual(self.person.name, "Aaron")

    def test_surname(self):
        self.assertEqual(self.person.surname, "Carter")

    def test_gender(self):
        self.assertEqual(self.person.gender, "male")

    def test_region(self):
        self.assertEqual(self.person.region, "New Zealand")

    @raises(utils.PropertyUnavailable)
    def test_property_not_present(self):
        self.person.property_not_present


class AdvancedWrapperFunctionality(unittest.TestCase):
    """
    This testcase tests the functionality of the generate_random_identities
    function.
    """

    @responses.activate
    def setUp(self):
        url = "https://uinames.com/api/?amount=10&ext=True"
        data = json.load(open("tests/fixtures/people.json"))
        response = responses.add(responses.GET, url, json=data, status=200,
                                 content_type="application/json",
                                 match_querystring=True)
        self.people = uinames.generate_random_identities(10, ext=True)
        self.person = self.people.data[0]
        # basic assertions
        self.assertEqual(len(responses.calls), 1)

    def test_multiple_results(self):
        self.assertEqual(len(self.people.data), 10)

    def test_name(self):
        self.assertEqual(self.person.name, "Ronja")

    def test_surname(self):
        self.assertEqual(self.person.surname, "Bagge")

    def test_gender(self):
        self.assertEqual(self.person.gender, "female")

    def test_region(self):
        self.assertEqual(self.person.region, "Sweden")

    def test_age(self):
        self.assertEqual(self.person.age, 32)

    def test_title(self):
        self.assertEqual(self.person.title, "mrs")

    def test_phone(self):
        self.assertEqual(self.person.phone, "(656) 718 3112")

    def test_birthday(self):
        self.assertEqual(self.person.birthday, {"dmy": "24/01/1985",
                                                "mdy": "01/24/1985",
                                                "raw": 475431301})

    def test_email(self):
        self.assertEqual(self.person.email, "ronja-bagge@example.com")

    def test_password(self):
        self.assertEqual(self.person.password, "Bagge85_@")

    def test_credit_card(self):
        self.assertEqual(self.person.credit_card, {"expiration": "3/19",
                                                   "number": "2115-8343-4559-1249",
                                                   "pin": 2085, "security": 143})

    def test_photo(self):
        self.assertEqual(self.person.photo,
                         "https://uinames.com/api/photos/female/24.jpg")

    @raises(utils.PropertyUnavailable)
    def test_property_not_present(self):
        self.person.property_not_present
