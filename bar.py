from pandas import read_csv
import matplotlib.pyplot as plt 
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages



class get_barchar():
	def __init__(self):
		self.bar_path = "veri/HavaKaliteMean.csv"
		self.df = read_csv(self.bar_path)
		self.df.columns = ["Istasyon","PM10",'SO2','NO2','NOX','O3','CO']

	def plotsbar(self):
		self.pp = PdfPages('static/rap/bar.pdf')

		self.cols = ["PM10",'SO2','NO2','NOX','O3','CO']
		self.colors=["goldenrod","red","green","blue","gray","yellow"]

		try:
			for self.sutun in range(len(self.cols)):
				sns.set_style('darkgrid')
				fig, ax = plt.subplots(figsize=(9,4))
				self.df = self.df.sort_values([self.cols[self.sutun]]).reset_index(drop=True)
				sns.barplot(x='Istasyon', y=str(self.cols[self.sutun]),data = self.df,color= self.colors[self.sutun], label=str(self.cols[self.sutun]))
				plt.rcParams["font.weight"] = "bold"
				plt.xlabel('Istasyon',size=15)
				plt.ylabel(str(self.cols[self.sutun]),size=15)
				self.pp.savefig(plt.gcf())

		finally:
			self.pp.close()





