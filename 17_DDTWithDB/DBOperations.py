# insert , update, delete---

insert_query = "insert into students values(104,'Kim',89)"
update_query = "update students set sname='Mary' where sid=104"
delete_query = "delete from students where sid=104"

import pymysql

try:
    con = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="ruchika0505",
        database="youtube")

    curs = con.cursor()  # create cursor
    # curs.execute(delete_query)
    curs.execute(insert_query)  #execute query through cursor
    con.commit()  # commit transaction
    con.close()
    print("Finished.....")

except:
    print("Connection unsuccessful...")
