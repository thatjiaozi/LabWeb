import os
from django.urls import path
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views as auth_views


from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY,TA_LEFT,TA_CENTER,TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus.tables import Table
from reportlab.platypus import (
    BaseDocTemplate, 
    PageTemplate, 
    Frame, 
    Paragraph,
    TableStyle
)

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

def ticket(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ticketVenta.pdf"'

    # Create the PDF object, using the response object as its "file."
    canvasResponse = canvas.Canvas(response)

    # Header
    canvasResponse.setLineWidth(.3)
    canvasResponse.setFont('Helvetica', 22)
    canvasResponse.drawString(30, 750, 'Comercial')

    canvasResponse.setFont('Helvetica', 22)
    canvasResponse.drawString(30, 730, 'Valmir')

    canvasResponse.setFont('Helvetica-Bold', 12)
    canvasResponse.drawString(480, 750, '03/04/2018')

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
    ticket = []
    ticket.append([productID, productName, productPrice, quantity])

    styles = getSampleStyleSheet()
    stylesTable = styles['BodyText']
    stylesTable.alignment = TA_CENTER
    stylesTable = fontsize = 7

    # Inicializa altura para empezar a escribir
    high = 650

    # Se declaran las ventas
    ventas = [
        {'id' : '1', 'name' : 'Tupper', 'price' : '$130', 'quantity' : '3'},
        {'id' : '2', 'name' : 'Cuchara', 'price' : '$10', 'quantity' : '2'},
        {'id' : '2', 'name' : 'Vaso', 'price' : '$40', 'quantity' : '4'},
    ]

    # Se agrega la informacion de las ventas a la lista
    for venta in ventas:
        this_venta = [venta['id'], venta['name'], venta['price'], venta['quantity']]
        ticket.append(this_venta)
        high = high - 18

    #  Se dibuja el contorno de la tabla
    width, heigth = A4
    table = Table(ticket, colWidths = [1.9 * cm, 9.5 * cm, 1.9 * cm, 1.9 * cm])
    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))

    table.wrapOn(canvasResponse, width, heigth)
    table.drawOn(canvasResponse, 30, high)
    canvasResponse.showPage()

    # Save PDF
    canvasResponse.save()

    return response

# General imports from Django
import os, sys, django
from django.db.models.functions import Cast
from django.db.models.fields import DateField
from django.db.models.functions import ExtractMonth
from django.db import models

# ReportLabs imports
from rlextra.graphics.quickchart import QuickChart
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin

from reportlab.graphics.shapes import *
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import getStringIO
from reportlab import rl_config

from reportlab.graphics import *

# Load settings file located in the administracion subfolder
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.py")
django.setup()
from administracion.models import *

class monthlyReport(_DrawingEditorMixin, Drawing):
    def __init__(self, width = 800, height = 400, Year=2018, nameOfFile = "Reporte_Ventas_", *args, **kw):
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


        # Name of  file
        nameOfFile = (nameOfFile + str(Year) + ".pdf")

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
        self.height = height
        self.width = width

        self.save(formats = ['pdf'], outDir = '.', fnRoot = None)

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

def printTestPdf(request):
  return printPdf('monthlyReport000.pdf')

def printPdf(path):
    with open(path, "rb") as f:
        data = f.read()
    return HttpResponse(data, content_type='application/pdf')

def reporte(request):


    return printTestPdf(request)