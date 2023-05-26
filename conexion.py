import pymysql


def obtener_conexion():
    return pymysql.connect(host='us-cdbr-east-06.cleardb.net',
                                user='b42ce11279450b',
                                password='8e63aaf9',
                                db='heroku_4cf2e481dd1ef90',port=3306)