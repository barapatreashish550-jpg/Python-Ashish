import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

latitudes = [34.05, 35.68, -33.86, 51.50, 19.07]
longitudes = [-118.24, 139.69, 151.21, -0.12, 72.87]

plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.coastlines()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)

plt.scatter(longitudes, latitudes, transform=ccrs.PlateCarree())

plt.title("Earthquake Locations on World Map")

plt.show()