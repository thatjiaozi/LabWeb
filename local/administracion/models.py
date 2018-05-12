from django.db import models
from urllib.parse import urlparse
import os
import random
import time
import psycopg2
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

# Create your models here.

class Categoria(models.Model):
    Nombre = models.CharField(max_length = 40, blank=False, null=False)

    def __str__(self):
        return self.Nombre

    class Meta:
        ordering = ('id',)

    def delete(self):
        super(Categoria, self).delete()
        self.update_db()

    def save(self):
        super(Categoria, self).save()
        self.update_db()

    def update_db(self):
        try:
            database_url = urlparse(os.getenv('HEROKU_URL'))
            conn_string = "dbname=%s user=%s host=%s password=%s" % (database_url.path[1:], database_url.username, database_url.hostname, database_url.password)
            conn = psycopg2.connect(conn_string)
            cur = conn.cursor()
            cur.execute("DELETE FROM catalog_categoria")

            instancias = Categoria.objects.all().order_by('id')

            count = 0
            for instancia in instancias:
                cur.execute("INSERT INTO catalog_categoria VALUES(%i, '%s')" % (count, instancia.Nombre))
                count = count+1


            conn.commit()
        except psycopg2.Error as e:
            print('error connecting to heroku')
            print(e.pgerror)
            print(e.diag.message_detail)

class Producto(models.Model):
    Nombre = models.CharField(max_length = 70)
    Descripcion = models.CharField(max_length = 300, default = 'none')
    Imagen = models.CharField(max_length = 300, default = '')
    Precio = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
    En_Existencia = models.IntegerField(default = 0)
    Categorias = models.ManyToManyField(Categoria)
    Codigo = models.CharField(max_length = 128)

    def __str__(self):
        return self.Nombre

    def delete(self):
        super(Producto, self).delete()
        self.update_db()


    def update_db(self):
        try:
            database_url = urlparse(os.getenv('HEROKU_URL'))
            conn_string = "dbname=%s user=%s host=%s password=%s" % (database_url.path[1:], database_url.username, database_url.hostname, database_url.password)
            conn = psycopg2.connect(conn_string)
            cur = conn.cursor()
            cur.execute("DELETE FROM catalog_producto")
            cur.execute("DELETE FROM \"catalog_producto_Categorias\"")

            instancias = Producto.objects.all()

            count = 0
            for instancia in instancias:
                cur.execute("INSERT INTO catalog_producto VALUES(%i, '%s', '%s', %f, %i, '%s')" % (count, instancia.Nombre, instancia.Descripcion, instancia.Precio, instancia.En_Existencia, instancia.Codigo))
                if instancia.Nombre == self.Nombre:
                    categorias = self.Categorias
                else :
                    categorias = instancia.Categorias

                for categoria in categorias.all():
                    cur.execute("SELECT * from catalog_categoria where \"Nombre\" = '%s' order by id" % (categoria.Nombre))
                    db_rows = cur.fetchall()
                    id_cat = db_rows[0][0]

                    cur.execute("INSERT INTO \"catalog_producto_Categorias\" VALUES(%i, %i, %i)" %(random.randint(1, 10000) + int(time.time()), count, id_cat))
                count = count+1


            conn.commit()
        except psycopg2.Error as e:
            print('error connecting to heroku')
            print(e.pgerror)
            print(e.diag.message_detail)

    class Meta:
        ordering = ('id',)

class Folio(models.Model):
    Fecha = models.DateTimeField()
    Productos = models.ManyToManyField(Producto, through='Venta')

    @property
    def Pago_Total(self):
        accum = 0
        for producto in self.Productos.all():
            accum += Venta.objects.get(folio=self.id, producto=producto.id).Cantidad * producto.Precio
        return accum

    def __str__(self):
        return 'Folio ' + str(self.id) + ': ' + '$' + str(self.Pago_Total) + ' MXN'

    class Meta:
        ordering = ('id',)

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    folio = models.ForeignKey(Folio, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.producto) + ' - ' + str(self.folio)

    class Meta:
        ordering = ('id',)

def on_transaction_commit(func):
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))
    return inner


@receiver(post_save, sender=Producto)
@on_transaction_commit
def producto_post_save(sender, instance, created, **kargs):
        try:
            database_url = urlparse(os.getenv('HEROKU_URL'))
            conn_string = "dbname=%s user=%s host=%s password=%s" % (database_url.path[1:], database_url.username, database_url.hostname, database_url.password)
            conn = psycopg2.connect(conn_string)
            cur = conn.cursor()
            cur.execute("DELETE FROM catalog_producto")
            cur.execute("DELETE FROM \"catalog_producto_Categorias\"")

            instancias = Producto.objects.all()

            count = 0
            for instancia in instancias:
                cur.execute("INSERT INTO catalog_producto VALUES(%i, '%s', '%s', %f, %i, '%s')" % (count, instancia.Nombre, instancia.Descripcion, instancia.Precio, instancia.En_Existencia, instancia.Codigo))
                categorias = instancia.Categorias

                for categoria in categorias.all():
                    cur.execute("SELECT * from catalog_categoria where \"Nombre\" = '%s' order by id" % (categoria.Nombre))
                    db_rows = cur.fetchall()
                    id_cat = db_rows[0][0]

                    cur.execute("INSERT INTO \"catalog_producto_Categorias\" VALUES(%i, %i, %i)" %(random.randint(1, 10000) + int(time.time()), count, id_cat))
                count = count+1


            conn.commit()
        except psycopg2.Error as e:
            print('error connecting to heroku')
            print(e.pgerror)
            print(e.diag.message_detail)

