import os

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY,TA_LEFT,TA_CENTER,TA_RIGHT
from reportlab.lib.pagesizes import A4, cm
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

from django.http import HttpResponse

this_path = os.getcwd() + '/tickets'


# Create the HttpResponse headers with PDF
# response = HttpResponse(content_type='application/pdf')
# response['Content-Disposition'] = 'attachment; filename=TicketGenerado.pdf'

# Create the PDF Object, using the BytesIO object as its file.
# buffer = BytesIO()
c = canvas.Canvas("ticketPruebaChido.pdf", pagesize=A4)

# Header
c.setLineWidth(.3)
c.setFont('Helvetica', 22)
c.drawString(30, 750, 'Comercial')

c.setFont('Helvetica', 22)
c.drawString(30, 730, 'Valmir')

c.setFont('Helvetica-Bold', 12)
c.drawString(480, 750, '03/04/2018')

# Start X, Start Y, End X, End Y
c.line(460, 747, 560, 747)

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

table.wrapOn(c, width, heigth)
table.drawOn(c, 30, high)
c.showPage()

# Save PDF
c.save()