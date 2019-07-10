from unittest import TestCase
from airports import Airports

class TestAiports(TestCase):
    class Airport():
        sid_location = Airports().find_airport_sid("LPPT")
        star_location = Airports().find_airport_star("LPPT")
        unkown_file_location = Airports().find_airport_sid("A0AA")
        sid_file_to_read = None
        #def __init__():
        #    pass

    airport = Airport()

    def test_find_airport_sid_exists(self):
        self.assertEqual(self.airport.sid_location, 'airac/sids/LPPT.txt')

    def test_find_airport_star_exists(self):
        self.assertEqual(self.airport.star_location, 'airac/stars/LPPT.txt')

    def test_find_airport_none(self):
        self.assertIsNone(self.airport.unkown_file_location)

    def test_open_airport_file(self):
        sid_file = Airports().open_airport_file(self.airport.sid_location)
        self.assertIsNotNone(sid_file)

    def test_get_airport_sids(self):
        sid_file = Airports().open_airport_file(self.airport.sid_location)
        self.assertIsNotNone(Airports().get_airport_sids(sid_file))

    def test_parse_sid(self):
        sid_file = Airports().open_airport_file(self.airport.sid_location)
        sid_sections = Airports().get_airport_sids(sid_file)

        for section in sid_sections:
            self.assertIsNotNone(Airports().parse_sid(section))       
    
    def test_get_neighbours_from_airport(self):
        sid_file = Airports().open_airport_file(self.airport.sid_location)
        sid_sections = Airports().get_airport_sids(sid_file)
        for section in sid_sections:
            sid_parsed = Airports().parse_sid(section)
            sid = Airports().get_neighbours_from_airport(sid_parsed)
        #print(sid)
    