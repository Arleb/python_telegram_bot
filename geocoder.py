from googleplaces import GooglePlaces, types
from settings import API_TOKEN

# 1) Specifying api_token
# 2) Setting searching parameters
# 3) Getting data by using loop
def geocoder(current_position):

    places = tuple()

    google_places = GooglePlaces(API_TOKEN)
    query_result = google_places.nearby_search(language='ru',
                                               lat_lng={'lat': current_position[0], 'lng': current_position[1]},
                                               radius=1000,
                                               types=[types.TYPE_PARKING])

    try:

        for place in query_result.places:
            place.get_details()
            places = (place.name,
                      place.vicinity)

        return places

    except Exception:

        print("error")
