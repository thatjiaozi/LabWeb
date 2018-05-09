#Autogenerated by ReportLab guiedit do not edit
from rlextra.graphics.quickchart import QuickChart
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin

from django.db import models
import os, sys
os.chdir('./local')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")
os.chdir('../administracion')


from models import Products

class reporte_ventas_mes(_DrawingEditorMixin,Drawing):
	''' 
	Line Chart - with markers & 3 series
	'''
	def __init__(self,width = 400, height = 200, *args, **kw):

		locations = Products.objects.all()
		print (locations)

		Drawing.__init__(self,width,height,*args,**kw)

		self._add(self,QuickChart(),name='chart',validate=None,desc=None)
		self.chart.height               = 200
		self.chart.titleText            = 'Ventas totales por mes'
		self.chart.seriesNames          = ('Ventas')
		self.chart.xTitleText           = 'Año'
		self.chart.categoryNames        = ('Enero','Febrero','Marzo','Abril')
		self.chart.yTitleText           = 'Pesos mexicanos'
		self.chart.chartType='linechart_markers'
		self.chart.data                 = [[18000, 17000, 19000, 20000]]

if __name__=="__main__":
	reporte_ventas_mes().save(formats = ['pdf'], outDir = '.', fnRoot = None)