"""
This script takes in a locations latitude and logitude, and 
plots an azithumal equidistant projection map of the world centered around that location.
"""
import matplotlib.pyplot as plt
import cartopy

def plot_map(lat, lon):
    """
    Plots an azithumal equidistant projection map of the world centered around the given location.
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1, projection=cartopy.crs.AzimuthalEquidistant(central_longitude=lon, central_latitude=lat))
    ax.stock_img()
    ax.coastlines()
    plt.show()

if __name__ == "__main__":
    plot_map(0, 0)