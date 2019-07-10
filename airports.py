import glob

class Airports():
    """"""

    def find_airport_sid(self, icao):
        search_result = glob.glob("airac/sids/{}.txt".format(icao))

        if len(search_result) > 0:
            return search_result[0]
        else:
            return None
    
    def find_airport_star(self, icao):
        search_result = glob.glob("airac/stars/{}.txt".format(icao))

        if len(search_result) > 0:
            return search_result[0]
        else:
            return None

    def open_airport_file(self, file_location):
        with open(file_location, 'r') as file:
            return file.read()


    def get_airport_sids(self, file):
        return file.split('\n\n')

    def parse_sid(self, sid_section):
        sid_parsed = sid_section.split('\n')
        return sid_parsed

    def get_neighbours_from_airport(self, sid_parsed):
        airport_sid = []
        to_decode = sid_parsed[0].split('|')
        sid = to_decode[3]
        print("SID:", sid)
        if sid in airport_sid:
            pass
        else:
            airport_sid.append(sid)
        print("List:", airport_sid)
        return airport_sid
