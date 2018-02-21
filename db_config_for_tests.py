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

    database_connection.close();
