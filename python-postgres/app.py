import time
import random
from flask import Flask
import os
import socket
import sys

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

db_name = 'pg'
db_user = 'raghav'
db_pass = 'secK#et'
db_host = 'dbserver'
db_port = '5432'

# Connect to the database
db_string = 'postgres://{}:{}@{}:{}/{}'.format(
    db_user, db_pass, db_host, db_port, db_name)
app = Flask(__name__)

hostAddress = ""

def add_new_row(engine,num,addr):
    # Insert a new number into the 'pg_data' table.

    ctime = int(round(time.time() * 1000))
    insertQuery = "INSERT INTO pg_data (count,address,currenttime) VALUES ("+str(num)+","+"'"+addr+"'"+","+ str(ctime) +");"
    #engine.execute("INSERT INTO pg_data (count,address,currenttime) VALUES ("+str(num) + "," +str(addr)+","+
              ## str(int(round(time.time() * 1000))) + ");")
    engine.execute(insertQuery)
    print('record inserted: ')


def get_last_row(engine):
    # Retrieve the address and count inserted inside the
    selectQuery = "SELECT count FROM pg_data WHERE currenttime >= (SELECT max(currenttime) FROM pg_data) LIMIT 1";

    ##query = "SELECT count FROM pg_data WHERE" + \
        ##"currenttime >= (SELECT max(currenttime) FROM pg_data)" + "LIMIT 1"
    result_set = engine.execute(selectQuery)
    for (r) in result_set:
        print('record: ')
        return r[0]

@app.route("/")
def runapp():
    visits = "NO Data"
    host = socket.getfqdn(socket.gethostname())
    hostAddr = socket.gethostbyname(socket.gethostname())
    hostAddress = hostAddr
    try:  # Connect to the database
     db = create_engine(db_string)
     db.connect()
     data = get_last_row(db)
     if data is None:    
       data=1
     else:
       data = data + 1
     visits = data
     add_new_row(db,data,hostAddress)
    except SQLAlchemyError as e:
     print(type(e))
     error = str(e)
     visits = "NO DataBase Available"
     ##return error

    print 'Content-type: text/html\n\n'
    uname = os.getenv("NAME", "world")
   

    html = "<h3>Hello {name}!</h3>" \
        "<b>Hostname:</b>{hostname}<br/>" \
        "<b>Host-Address:</b>{hostaddr}<br/>" \
        "<b>Visits:</b>{visits}"
    return html.format(name=uname, hostname=host, hostaddr=hostAddr, visits=visits)


if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=8090)
    app.run(host='0.0.0.0', port=8090)



