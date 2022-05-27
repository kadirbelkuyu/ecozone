
import os 
import folium
from folium import plugins
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import matplotlib.pyplot as plt 
import webbrowser
from IPython.display import display

class getMap:
    def __init__(self):
        # Import data from EarthPy
        self.data = et.data.get_data('colorado-flood')

        # Set working directory to earth-analytics
        os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))
    def getmap():
        m = folium.Map(location=[37.871540, 32.498914],
                    tiles = 'Stamen Terrain',zoom_start=12, height=500)

        # Add marker for Boulder, CO
        folium.Marker(
            location=[37.871540, 32.498914], # coordinates for the marker
            popup='Earth Lab at CU Boulder', # pop-up label for the marker
            icon=folium.Icon()
        ).add_to(m)
        folium.TileLayer('openstreetmap').add_to(m)
        return m