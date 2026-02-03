import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='blogdb'
    )
    if conexion.is_connected():
        print("Conectado a blogdb")
        conexion.close()
except Exception as fail:
    print(f"Error:{fail}")