import folium

m = folium.Map(location=[36.003583, 138.000791],
               zoom_start=7,
               attr='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors')

with open('geocoding_list.csv', 'r', encoding='utf-8') as fp:
    reader = csv.reader(fp)
    header = next(reader)
    for row in reader:
        code = [float(row[1]), float(row[2])]
        folium.Marker(code, popup='<i>{}</i>'.format(row[0])).add_to(m)

m.save('ichinomiya.html')
