class Location(object):
    """Class for locations used alongside the met office API.
    Stores information regarding a specific location's name 
    and attributes
    """

    def __init__(self, data):
        self.data = data


    def print_data(self):
        print self.data
    
    def get_name(self):
        return self.data['name']

    def get_elevation(self):
        return self.data['elevation']

    def get_id(self):
        return self.data['id']

    def get_latitude(self):
        return self.data['latitude']

    def get_longitude(self):
        return self.data['longitude']

    def get_region(self):
        return self.data['region']

    def get_obsSource(self):
        return self.data['obsSource']
    
    def get_nationalPark(self):
        return self.data['nationalPark']


