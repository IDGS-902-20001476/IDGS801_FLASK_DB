from db import get_connection

try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call agrega_alumno(%s, %s, %s)',('xx', '321', 'sss')) 
        """ rows=curso.fetchall()     
        print(type(rows))
        for   row in rows:
            print(row)"""
    connection.commit()
    connection.close()

except Exception as ex:
    print('error'+ex)





