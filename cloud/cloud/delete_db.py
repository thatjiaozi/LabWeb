import os
import sys
from urllib.parse import urlparse
import mysql.connector

# Set the configuration to the connection of the database
url = urlparse(os.environ['DATABASE_URL'])
hostname = url.hostname
user = url.username
password = url.password
port = url.port
database = url.path[1:]

# Create the connection
try:
    database_connection = mysql.connector.connect(host=hostname, user=user, passwd=password, db=database)
except mysql.connector.Error as err:
    print("Error while connecting to the database: %d" % err.errno)
else:

    # Put database code here
    cur = database_connection.cursor();
    cur.execute("DELETE FROM catalog_products_categories")
    cur.execute("DELETE FROM catalog_sales_products")
    cur.execute("DELETE FROM catalog_employees")
    cur.execute("DELETE FROM catalog_products")
    cur.execute("DELETE FROM catalog_categories")
    cur.execute("DELETE FROM catalog_sales")
    cur.execute("DELETE FROM catalog_administrators")

    database_connection.commit()
    database_connection.close()
