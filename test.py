from shapely.geometry import Polygon, MultiPolygon
import binascii

# Define coordinates for a square polygon (You can modify coordinates as per your needs)
coords = [(139.9531751, 35.74516919), (139.959, 35.74516919),
          (139.959, 35.740), (139.9531751, 35.740)]

# Create a Polygon
polygon = Polygon(coords)

# Create a MultiPolygon
multi_poly = MultiPolygon([polygon])

# Get WKB binary
wkb_multi_poly = multi_poly.wkb

# Convert to a hexadecimal string
hex_string = binascii.hexlify(wkb_multi_poly).decode()

print("Hexadecimal WKB String for the MultiPolygon:", hex_string)
