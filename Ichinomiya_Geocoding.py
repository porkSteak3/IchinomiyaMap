import csv
import googlemaps

#GoogleMaps API Key
api_key = '***'
gmaps = googlemaps.Client(key=api_key)

# read csv
geo_loc = list([['site','lat','lon']])
with open('一宮一覧.csv', 'r', encoding='utf-8') as fp:
    reader = csv.reader(fp)
    header = next(reader)
    for row in reader:
        results = gmaps.geocode(row[1])
        for result in results:
            addr = result['formatted_address']
            location = result['geometry']['location']
            lat = location['lat']
            lng = location['lng']
            geo_loc.append([row[1], lat, lng])

with open('geocoding_list.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    for line in geo_loc:
        writer.writerow(line)
