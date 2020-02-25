import tweepy
import folium
from geopy.geocoders import Nominatim


def get_location(user_input):
    auth = tweepy.auth.OAuthHandler('ZK2vNGkhFIK6zVV0ZumVvu5TC', \
                                    'MWLX6TesvOcGfYHnXcnBgKsPilY0ucWiiEf9XOjYGA6edJ1Bd9')
    auth.set_access_token('1231334784745472001-ldiUoZ1dfZXOr75k2qui8jz0Be5sSm', \
                          'TXSI9oDk2gOhlRy73lNs5WpltJo3RFj6gifZjb9ZpIt1A')
    api = tweepy.API(auth)
    users = tweepy.Cursor(api.friends, screen_name=user_input).items()
    return html_map(users)


def html_map(followers):
    user_dict = dict()

    for user in followers:
        locator = Nominatim(user_agent='Name')
        try:
            location = locator.geocode(user.location)
            location = (location.latitude, location.longitude)
            if not location in user_dict:
                user_dict[location] = user.screen_name
            else:
                user_dict[location] = user_dict[location] + '\n' + user.screen_name
        except:
            print(user.screen_name)
            continue

    kart = folium.Map()
    seam = folium.FeatureGroup(name="Friends")

    for place in user_dict:
        seam.add_child(folium.Marker(location=[place[0], place[1]],
                                     popup=user_dict[place],
                                     icon=folium.Icon(color='orange'
                                                      )))


    kart.add_child(seam)
    return kart._repr_html_()



