
import os 
import folium
from folium import plugins
import rioxarray as rxr
import earthpy as et
import earthpy.spatial as es
import matplotlib.pyplot as plt 
import webbrowser
import pandas as pd
from IPython.display import display


class getMap:
		def __init__(self):
				# Import data from EarthPy
				self.data = et.data.get_data('colorado-flood')

				# Set working directory to earth-analytics
				#os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))
				
		def getmap():
				path = "20_202106_guzergah.csv"
				databus= pd.read_csv(path, sep=";")
				databus.ENLEM = databus.ENLEM.str.replace(".","")

				databus.BOYLAM = databus.BOYLAM.str.replace(".","")


				databus.ENLEM = databus.ENLEM.astype(float)
				databus.BOYLAM = databus.BOYLAM.astype(float)

				databus.ENLEM = databus.ENLEM/1000000
				databus.BOYLAM = databus.BOYLAM/1000000



				# Import data from EarthPy
				data = et.data.get_data('colorado-flood')

				# Set working directory to earth-analytics
				#os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))

				m = folium.Map(location=[37.871540, 32.498914], 
											 tiles = 'Stamen Terrain',zoom_start=12, position='relative')

				# Add marker for Boulder, CO
				#folium.Marker(
				#    location=[37.871540, 32.498914], # coordinates for the marker
				#    popup='Earth Lab at CU Boulder', # pop-up label for the marker
				#    icon=folium.Icon() ).add_to(m)

				for num in databus.ANA_HAT_NO.unique():
						databus1 = databus.loc[databus.ANA_HAT_NO==num]
						databus1 = databus1.reset_index(drop=True)
						kord = []
						for point in range(len(databus1)):
								kord.append(tuple([databus1.ENLEM[point], databus1.BOYLAM[point]]))
						folium.PolyLine(kord,opacity=0.03,color="black").add_to(m)


				#for point in range(0,len(databus1),15):
				#    folium.Marker(location=[databus1.ENLEM[point], databus1.BOYLAM[point]], # coordinates for the marker
				 #                               popup='Earth Lab at CU Boulder', # pop-up label for the marker
					#                              icon=folium.Icon() ).add_to(m)
						
						
						
				#folium.TileLayer('openstreetmap').add_to(m)
				markers = folium.FeatureGroup(name="Hava Kalitesi Kontrol Noktaları").add_to(m)
				folium.Marker(location=[37.870010,32.517043],
							popup="Karatay 1",
							icon=folium.Icon(color="green")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[37.870010,32.517043],
				color='green', weight=1,
				fill=True, opacity=0.5).add_to(markers)



				folium.Marker(location=[37.844698,32.513969],
											popup="Karatay 2",
											icon=folium.Icon(color="red")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[37.844698,32.513969],
				color='red', weight=1,
				fill=True, opacity=0.5).add_to(markers)



				folium.Marker(location=[37.917843,32.505660],
											popup="Selçuklu",
											icon=folium.Icon(color="black")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[37.917843,32.505660],
				color='black', weight=1,
				fill=False,).add_to(markers)



				folium.Marker(location=[38.013184,32.520520],
											popup="Bosna",
											icon=folium.Icon(color="gray")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[38.013184,32.520520],
				color='gray', weight=1,
				fill=False,).add_to(markers)


				folium.Marker(location=[37.860659,32.470254],
											popup="Meram",
											icon=folium.Icon(color="orange")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[37.860659,32.470254],
				color='orange', weight=1,
				fill=False,).add_to(markers)


				folium.Marker(location=[37.907138,32.459662],
											popup="Erenköy",
											icon=folium.Icon(color="darkgreen")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[37.907138,32.459662],
				color='darkgreen', weight=1,
				fill=True, opacity=1,).add_to(markers)



				folium.Marker(location=[37.903952,32.527440],
											popup="Karkent",
											icon=folium.Icon(color="beige")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[37.903952,32.527440],
				color='beige', weight=1,
				fill=False,).add_to(markers)


				folium.Marker(location=[37.883034,32.485458],
											popup="Merkez Trafik",
											icon=folium.Icon(color="pink")).add_to(markers)

				folium.Circle(
				radius=1500,
				location=[37.883034,32.485458],
				color='pink', weight=1.5,
				fill=False,).add_to(markers)

				
				


				folium.Marker(location=[38.357237,31.419943],
											popup="Akşehir",
											icon=folium.Icon(color="lightblue")).add_to(markers)


				folium.Circle(
				radius=3000,
				location=[38.357237,31.419943],
				color='lightblue', weight=1,
				fill=True, opacity=0.6).add_to(markers)

				
				folium.Marker(location=[38.514783,32.459111],
											popup="Sarayönü",
											icon=folium.Icon(color="purple")).add_to(markers)

				
				

				folium.Circle(
				radius=2500,
				location=[38.514783,32.459111],
				color='purple', weight=1,
				fill=True, opacity=0.6).add_to(markers)

				
				
				folium.LayerControl().add_to(m)

				return m