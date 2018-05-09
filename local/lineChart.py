#Autogenerated by ReportLab guiedit do not edit
import os, sys
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from django.db.models.functions import ExtractMonth
from django.db import models

from rlextra.graphics.quickchart import QuickChart
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin




print(os.getcwd())
os.chdir('./local/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")
os.chdir('../administracion/')

from administracion.models import *

class reporte_ventas_mes(_DrawingEditorMixin,Drawing):
	''' 
	Line Chart - with markers & 3 series
	'''
	def __init__(self,width = 400, height = 200, *args, **kw):

		objProductos = Producto.objects.all()
		objCategorias = Categoria.objects.all()
		objFolios = Folio.objects.all()
		objVentas = Venta.objects.all()


		dictAcum = dict()
		#print(objFolios.values_list('Fecha')[0][0].month)

		#print(objFolios.values_list('Fecha')[0][0].Pago_Total)
		for folio in objFolios:
			mes = folio.Fecha.month
			if(mes in dictAcum.keys()):
				dictAcum[mes] = dictAcum[mes] + float(folio.Pago_Total)
			else:
				dictAcum[mes] = float(folio.Pago_Total)

		print(dictAcum)
		#folio = objFolios.values_list('venta')[0][0]
		#Venta.objects.get(pk=folio)
		#print(objVentas.values_list('Cantidad')[0][0])


		Drawing.__init__(self,width,height,*args,**kw)

		self._add(self,QuickChart(),name='chart',validate=None,desc=None)
		self.chart.height               = 200
		self.chart.titleText            = 'Ventas totales por mes'
		self.chart.seriesNames          = ('Ventas')
		self.chart.xTitleText           = 'Año'
		#self.chart.categoryNames        = ('Enero','Febrero','Marzo','Abril')
		self.chart.yTitleText           = 'Pesos mexicanos'
		self.chart.chartType='linechart_markers'
		
		listCant = []
		listCant.append([])
		for key, value in dictAcum.items():
			listCant[0].append(value)

		self.chart.data = listCant

		listMonths = []
		for key in dictAcum.keys():
			listMonths.append(str(key))
		self.chart.categoryNames = listMonths


if __name__=="__main__":
	reporte_ventas_mes().save(formats = ['pdf'], outDir = '.', fnRoot = None)