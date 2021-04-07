'''
Flight Distance calulator
I can tell you the fligt distance
between 2 given cities
Provide me the long & lat values
And I am happy to help
'''
from geopy.distance import great_circle

class DistanceCalculator():
    
    '''
    Hey Use Me for calculating the distance
    between two cities providing lat and lon
    value
    '''

    def __init__(self, lat1, lon1, lat2, lon2):
        
        self.city1_lat = self.convert_lon_lat_to_its_actual_int_value_depending_upon_angle(lat1)
        self.city1_lon = self.convert_lon_lat_to_its_actual_int_value_depending_upon_angle(lon1)
        self.city2_lat = self.convert_lon_lat_to_its_actual_int_value_depending_upon_angle(lat2)
        self.city2_lon = self.convert_lon_lat_to_its_actual_int_value_depending_upon_angle(lon2)
        self.distance  = ""
    
    @staticmethod
    def convert_lon_lat_to_its_actual_int_value_depending_upon_angle(value):
        
        '''
        longitude with angle to West are -ve
        Latitude  with angle to south are -ve
        '''
        
        if "W" in value or "S" in value:
            return -float(value.split(" ")[0])
        
        return float(value.split(" ")[0])
    
    def calculate_distance(self):

        city_1 = (self.city1_lat, self.city1_lon)
        city_2 = (self.city2_lat, self.city2_lon)
        dicstance_in_miles = great_circle(city_1, city_2).miles
        self.distance      = format(dicstance_in_miles * 1.609344, ".2f")

    
def main():

    city1_lat, city1_lon = input("City 1: ").split(",")
    city2_lat, city2_lon = input("City 2: ").split(",")

    dc = DistanceCalculator(city1_lat, city1_lon.lstrip(), city2_lat, city2_lon.lstrip())

    dc.calculate_distance()
    print(f"Output: City 1 and City 2 are {dc.distance} km apart")

main()