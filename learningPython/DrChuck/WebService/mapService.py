import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyA42g-QnX4ssSyiXqPQ7pRNI_KN5QFjhjU"

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address' : address})

    print("Retrieving" , url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data) , 'character')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('========Failure To Retrieve ========')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat' , lat , 'lng' , lng)
    location = js['results'][0]['formatted_address']
    print(location)
 
