import os, sys, django
from io import BytesIO

# Django imports
from django.urls import path
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from django.db.models.functions import ExtractMonth
from django.db import models

# Reportlab Imports
from rlextra.graphics.quickchart import QuickChart
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY,TA_LEFT,TA_CENTER,TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus.tables import Table
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, TableStyle)
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.graphics.shapes import *
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import getStringIO
from reportlab import rl_config
from reportlab.graphics import *
from reportlab.lib.colors import purple, PCMYKColor, black, pink, green, blue
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.legends import LineLegend
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.validators import Auto
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.pdfbase.pdfmetrics import stringWidth, EmbeddedType1Face, registerTypeFace, Font, registerFont
from reportlab.graphics.charts.axes import XValueAxis, YValueAxis, AdjYValueAxis, NormalDateXValueAxis

# Load settings file located in the administracion subfolder
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")
django.setup()
from administracion.models import *

path(
    'password_reset/',
    auth_views.PasswordResetView.as_view(),
    name='admin_password_reset',
),
path(
    'password_reset/done/',
    auth_views.PasswordResetDoneView.as_view(),
    name='password_reset_done',
),
path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(),
    name='password_reset_confirm',
),
path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(),
    name='password_reset_complete',
),

def createPDFOnBrowser(path):
    with open(path, "rb") as f:
        data = f.read()
    return HttpResponse(data, content_type='application/pdf')

def ticket(request, idTicket):
    generatedTicket = internalTicket(idTicket)
    return createPDFOnBrowser('internalTicket000.pdf')

def report(request, reportYear):
    generatedReport = internalReport(reportYear)
    return createPDFOnBrowser('internalReport000.pdf')

class internalTicket():
    def __init__(self, idTicket):

        # Retrive object products from models
        objProductos = Producto.objects.all()
        objCategorias = Categoria.objects.all()
        objFolios = Folio.objects.all()
        objVentas = Venta.objects.all()

        # Retrieve values of idTicket
        folioSelecto = Folio.objects.get(id = idTicket)

        # Create the PDF object, using the response object as its "file."
        canvasResponse = canvas.Canvas("internalTicket000.pdf", pagesize=A4)

        # Header
        canvasResponse.setLineWidth(.3)

        canvasResponse.setFont('Helvetica', 22)
        canvasResponse.drawString(30, 750, 'Comercial')
        canvasResponse.setFont('Helvetica', 22)
        canvasResponse.drawString(30, 730, 'Valmir')
        canvasResponse.setFont('Helvetica-Bold', 12)

        fecha = str(folioSelecto.Fecha.day) + '/' + str(folioSelecto.Fecha.month) + '/' + str(folioSelecto.Fecha.year) 
        canvasResponse.drawString(480, 750, fecha)

        # Start X, Start Y, End X, End Y
        canvasResponse.line(460, 747, 560, 747)

        # Table header
        styles = getSampleStyleSheet()
        stylesHeader = styles['Normal']
        stylesHeader.alignment = TA_CENTER
        stylesHeader.fontsize = 10

        # Informacion del ticket
        productID = Paragraph('''ID''', stylesHeader)
        productName = Paragraph('''Nombre''', stylesHeader)
        productPrice = Paragraph('''Precio''', stylesHeader)
        quantity = Paragraph('''Cantidad''', stylesHeader) 

        # Se crea la lista de listas con la que se representara el ticket
        ventaTicket = []
        ventaTicket.append([productID, productName, productPrice, quantity])

        styles = getSampleStyleSheet()
        stylesTable = styles['BodyText']
        stylesTable.alignment = TA_CENTER
        stylesTable = fontsize = 7

        # Inicializa altura para empezar a escribir
        high = 650

        total = 0

        for prodInd in folioSelecto.Productos.all():
            objVentaEscogida = Venta.objects.get(folio=folioSelecto.id, producto=prodInd.id)

            dictVentaIndividual = dict()
            dictVentaIndividual['id'] = prodInd.id
            dictVentaIndividual['name'] = prodInd.Nombre
            dictVentaIndividual['price'] = prodInd.Precio
            dictVentaIndividual['quantity'] = objVentaEscogida.Cantidad

            total += float(prodInd.Precio * objVentaEscogida.Cantidad)

            # Se agrega la informacion de las ventas a la lista
            this_venta = [dictVentaIndividual['id'], dictVentaIndividual['name'], dictVentaIndividual['price'], dictVentaIndividual['quantity']]
            ventaTicket.append(this_venta)
            high = high - 18


        # Add total
        ventaTicket.append(["", "","", ""])
        ventaTicket.append(["", "","Total", str(total)])

        #  Se dibuja el contorno de la tabla
        width, heigth = A4
        table = Table(ventaTicket, colWidths = [1.9 * cm, 9.5 * cm, 1.9 * cm, 1.9 * cm])
        table.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))

        table.wrapOn(canvasResponse, width, heigth)
        table.drawOn(canvasResponse, 30, high)
        canvasResponse.showPage()

        # Save PDF
        canvasResponse.save()

class internalReport(_DrawingEditorMixin, Drawing):
    def __init__(self, year=2018, width = 800, height = 400, *args, **kw):
        # Initialize chart
        Drawing.__init__(self, width, height,*args,**kw)

        self._add(self, QuickChart(), name = 'chart', validate = None, desc = None)

        # Properties of chart
        self.chart.titleText = ('Ventas totales del ' + str(year))
        self.chart.chartType = 'linechart_markers'
        self.chart.width = width
        self.chart.height = height
        self.chart.xTitleText = 'Mes'
        self.chart.yTitleText = 'Pesos mexicanos'
        self.chart.seriesNames = ('Ventas')

        # Data and category names, to be filled in the report section
        self.chart.data = [[]]
        self.chart.categoryNames = []

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

            if folio.Fecha.year == year:
                # Retrive the month number and convert it to string
                monthNumber = folio.Fecha.month
                monthWord = self.numberToWordMonth(monthNumber)

                # If the month is already in the dictionary, add the value, if not, create
                # the entry for such month
                if monthNumber in dicMonthlyEarnings.keys():
                    dicMonthlyEarnings[monthNumber] = dicMonthlyEarnings[monthNumber] + float(folio.Pago_Total)
                else:
                    dicMonthlyEarnings[monthNumber] = float(folio.Pago_Total)

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
            monthWord = self.numberToWordMonth(key)
            dataEarnings[0].append(dicMonthlyEarnings[key])
            dataMonths.append(str(monthWord))

        # Update values of data and categoryNames
        # Save the document in PDF Format
        self.chart.data = dataEarnings
        self.chart.categoryNames = dataMonths
        self.height = height
        self.width = width

        # Save PDF in disk
        self.save(formats = ['pdf'], outDir = '.', fnRoot = None)

    # Method that receives a month in numbers and return a string with the name of the month
    def numberToWordMonth(self, monthNumber):
        monthsDictionary = dict()
        monthsDictionary[1] = 'Ene'
        monthsDictionary[2] = 'Feb'
        monthsDictionary[3] = 'Mar'
        monthsDictionary[4] = 'Abr'
        monthsDictionary[5] = 'May'
        monthsDictionary[6] = 'Jun'
        monthsDictionary[7] = 'Jul'
        monthsDictionary[8] = 'Ago'
        monthsDictionary[9] = 'Sep'
        monthsDictionary[10] = 'Oct'
        monthsDictionary[11] = 'Nov'
        monthsDictionary[12] = 'Dic'
        try:
            return monthsDictionary[monthNumber]
        except:
            print("Month not valid")