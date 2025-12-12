import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Country coordinates (approximate central points)
coords = {
    "Russia": (100, 60),
    "Germany": (10, 51),
    "Georgia": (43.5, 42),
    "Azerbaijan": (47.5, 40.5),
    "Ethiopia": (39.5, 9),
    "Somalia": (46, 6),
    "Uganda": (32, 1.5),
    "Kenya": (37, 0.5),
    "Democratic Republic of the Congo": (23, -3),
    "Zambia": (28, -13),
    "Zimbabwe": (30, -19),
    "Ghana": (-1, 7.5),
    "Turkey": (35, 39),
    "Rwanda": (30, -2),
}

# Create a world map with Basemap
fig = plt.figure(figsize=(20, 10))
m = Basemap(projection="robin", lon_0=0, resolution="c")

# Draw map details
m.drawcoastlines(linewidth=0.8)
m.drawcountries(linewidth=0.6)
m.fillcontinents(color="lightgray", lake_color="lightblue")
m.drawmapboundary(fill_color="lightblue")

# Draw lat/lon grid
m.drawparallels(range(-90, 91, 30), labels=[1,0,0,0], fontsize=8)
m.drawmeridians(range(-180, 181, 60), labels=[0,0,0,1], fontsize=8)

# Mark countries
for country, (lon, lat) in coords.items():
    x, y = m(lon, lat)
    m.plot(x, y, "ro", markersize=6)
    plt.text(x+500000, y+300000, country, fontsize=8, color="black")

# Save as JPEG
output_path = "/mnt/data/world_map_with_countries.jpeg"
plt.savefig(output_path, format="jpeg", dpi=300, bbox_inches="tight")
plt.close()

output_path
