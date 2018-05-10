# General imports from Django
import os, sys, django
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
django.setup()
from administracion.models import *

# Set path to outside of the project folder (probably Desktop)
# Want: Must change so it receives a path in the user computer
os.chdir('../../../')

class monthlyReport(_DrawingEditorMixin, Drawing):
	def __init__(self, width = 800, height = 400, Year=2018, *args, **kw):
		# Initialize chart
		Drawing.__init__(self,width,height,*args,**kw)
		self._add(self, QuickChart(), name = 'chart', validate = None, desc = None)

		# Properties of chart
		self.chart.titleText = ('Ventas totales del ' + str(Year))
		self.chart.chartType = 'linechart_markers'
		self.chart.width = width
		self.chart.height = height
		self.chart.xTitleText = 'Mes'
		self.chart.yTitleText = 'Pesos mexicanos'
		self.chart.seriesNames = ('Ventas')

		# Data and category names, to be filled in the report section
		self.chart.data = [[]]
		self.chart.categoryNames = []

	# Method that creates the report
	def createReport(self, nameOfFile = "Reporte_Ventas_", year=2018):

		# Name of  file
		nameOfFile = (nameOfFile + str(year) + ".pdf")

		# Dictionary that maps a month (key) to a sum of earning (value) in such month
		dicMonthlyEarnings = dict()

		# Retrive object products from models
		objProductos = Producto.objects.all()
		objCategorias = Categoria.objects.all()
		objFolios = Folio.objects.all()
		objVentas = Venta.objects.all()

		# Iterate each folio and for each one retrieve the month of purchase, this will
		# be added in the dictionary of earning per month.
		for folio in objFolios:
			# Retrive the month number and convert it to string
			monthNumber = folio.Fecha.month
			monthWord = self.numberToWordMonth(monthNumber)

			# If the month is already in the dictionary, add the value, if not, create
			# the entry for such month
			if monthWord in dicMonthlyEarnings.keys():
				dicMonthlyEarnings[monthWord] = dicMonthlyEarnings[monthWord] + float(folio.Pago_Total)
			else:
				dicMonthlyEarnings[monthWord] = float(folio.Pago_Total)

		# Iterate the dictionary of earnings and pass the values to a list of data to be plotted
		# Append an empty list since it is required for plotting
		dataEarnings = []
		dataEarnings.append([])

		# List of months
		dataMonths = []

		# Get the sorted keys of the dictionary
		keylist = sorted(dicMonthlyEarnings.keys())

		# For each key add the earning and the month
		for key in keylist:
			dataEarnings[0].append(dicMonthlyEarnings[key])
			dataMonths.append(str(key))

		# Update values of data and categoryNames
		# Save the document in PDF Format
		self.chart.data = dataEarnings
		self.chart.categoryNames = dataMonths

		# Save report in PDF
		self.save(formats = ['pdf'], outDir = '.', fnRoot = None)

		try:
			os.rename("monthlyReport000.pdf", nameOfFile)
		except:
			pass

	# Method that receives a month in numbers and return a string with the name of the month
	def numberToWordMonth(self, monthNumber):
		monthsDictionary = dict()
		monthsDictionary[1] = 'Enero'
		monthsDictionary[2] = 'Febrero'
		monthsDictionary[3] = 'Marzo'
		monthsDictionary[4] = 'Abril'
		monthsDictionary[5] = 'Mayo'
		monthsDictionary[6] = 'Junio'
		monthsDictionary[7] = 'Julio'
		monthsDictionary[8] = 'Agosto'
		monthsDictionary[9] = 'Septiembre'
		monthsDictionary[10] = 'Octubre'
		monthsDictionary[11] = 'Noviembre'
		monthsDictionary[12] = 'Diciembre'
		try:
			return monthsDictionary[monthNumber]
		except:
			print("Month not valid")

if __name__=="__main__":
	report = monthlyReport()
	report.createReport()