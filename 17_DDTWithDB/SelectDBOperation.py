# insert , update, delete

import pymysql

try:
    con=pymysql.connect(host="localhost",port=3306,user="root",passwd="ruchika0505",database="youtube")
    curs=con.cursor()  # create curosor
    curs.execute("select * from students")  #execute query through cursor

    for row in curs:
        print(row[0],row[1],row[2])

    con.close()  # close connection
except:
    print("Connection unsuccessful...")

print("Finished.....")