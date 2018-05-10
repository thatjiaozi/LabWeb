# General imports from Django
import os, sys
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from django.db.models.functions import ExtractMonth
from django.db import models

# ReportLabs imports
from rlextra.graphics.quickchart import QuickChart
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin

# Load settings file located in the administracion subfolder
os.chdir('./administracion/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")
from administracion.models import *

# Set path to outside of the project folder (probably Desktop)
# Want: Must change so it receives a path in the user computer
os.chdir('../../../')

class reporte_ventas_mes(_DrawingEditorMixin, Drawing):
	def __init__(self,width = 400, height = 200, *args, **kw):

		#print(objFolios.values_list('Fecha')[0][0].month)
		#print(objFolios.values_list('Fecha')[0][0].Pago_Total)
		#print(gananciasPorMes)
		#folio = objFolios.values_list('venta')[0][0]
		#Venta.objects.get(pk=folio)
		#print(objVentas.values_list('Cantidad')[0][0])
		#self.chart.categoryNames        = ('Enero','Febrero','Marzo','Abril')

		# Dictionary that maps a month (key) to a sum of earning (value) in such month
		monthtlyEarnings = dict()

		# Retrive object products from models
		objProductos = Producto.objects.all()
		objCategorias = Categoria.objects.all()
		objFolios = Folio.objects.all()
		objVentas = Venta.objects.all()

		# Iterate each folio and for each one retrieve the month of purchase
		for folio in objFolios:
			monthNumber = folio.Fecha.month
			monthWord = 

			# If the 
			if monthNumber in monthtlyEarnings.keys():
				monthtlyEarnings[monthNumber] = monthtlyEarnings[monthNumber] + float(folio.Pago_Total)
			else:
				monthtlyEarnings[monthNumber] = float(folio.Pago_Total)

		listCant = []
		listCant.append([])
		for key, value in monthtlyEarnings.items():
			listCant[0].append(value)

		

		listMonths = []
		for key in monthtlyEarnings.keys():
			listMonths.append(str(key))
		

		Drawing.__init__(self,width,height,*args,**kw)

		self._add(self,QuickChart(),name='chart',validate=None,desc=None)
		self.chart.height               = 200
		self.chart.titleText            = 'Ventas totales por mes'
		self.chart.seriesNames          = ('Ventas')
		self.chart.xTitleText           = 'Año'
		self.chart.yTitleText           = 'Pesos mexicanos'
		self.chart.chartType='linechart_markers'
		self.chart.data = listCant
		self.chart.categoryNames = listMonths

	def numberToWordMonth(self):
		try:
			monthsDictionary = dict()
			monthsDictionary[1] = 'Enero'
			monthsDictionary[2] = 'Febrero'
			monthsDictionary[3] = 'Marzo'
			monthsDictionary[4] = 'Abril'
			monthsDictionary[5] = 'Mayo'
			monthsDictionary[6] = 'Junio'
			monthsDictionary[7] = 'Julio'
			monthsDictionary[8] = 'Agosto'
			monthsDictionary[9] = 'Setp'
			monthsDictionary[10] = 'Enero'
			monthsDictionary[11] = 'Enero'
			monthsDictionary[12] = 'Enero'

		except:
			print("Month not valid")

if __name__=="__main__":
	reporte_ventas_mes().save(formats = ['pdf'], outDir = '.', fnRoot = None)