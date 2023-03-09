from geopy import Nominatim
def get_place_name(lat, lon):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse(f"{lat}, {lon}")
    return location.address

# Example usage
place_name = get_place_name(40.748817, 113.985428)
print(place_name)
