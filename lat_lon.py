from shapely import wkb
import binascii


def get_lat_lon_from_wkb(wkb_hex: str) -> tuple:
    wkb_bytes = binascii.unhexlify(wkb_hex)
    geom = wkb.loads(wkb_bytes)
    centroid = geom.centroid
    longitude, latitude = centroid.x, centroid.y
    return (latitude, longitude)


lat, long = get_lat_lon_from_wkb(
    "0106000020E61000000100000001030000000100000005000000F6285C8FC27A6140E4326E6AA0734140F6285C8FC27A6140EC51B81E857341401F85EB51B87A6140EC51B81E857341401F85EB51B87A6140E4326E6AA0734140F6285C8FC27A6140E4326E6AA0734140")

print(lat, long)
